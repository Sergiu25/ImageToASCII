from flask import Flask, render_template, request, send_file
from PIL import Image
import os
import io
import base64

app = Flask(__name__)


def image_to_ascii(image, width=100, chars=" .:-=+*#%@"):
    # Convert to grayscale
    img = image.convert('L')

    # Calculate new dimensions
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio * 0.5)

    # Resize image
    img = img.resize((width, height))

    # Create ASCII art
    ascii_art = []

    # Get pixel data
    pixels = list(img.getdata())

    # Convert to 2D array
    pixel_matrix = []
    for i in range(0, len(pixels), width):
        pixel_matrix.append(pixels[i:i + width])

    # Process each pixel
    for y in range(height):
        row = []
        for x in range(width):
            brightness = pixel_matrix[y][x]
            char_index = int((brightness / 255) * (len(chars) - 1))
            row.append(chars[len(chars) - 1 - char_index])
        ascii_art.append(''.join(row))

    return '\n'.join(ascii_art)


def create_html_ascii_art(ascii_art):
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>ASCII Art</title>
    <style>
        body {{
            background-color: #000000;
            color: #FFFFFF;
            font-family: 'Courier New', monospace;
            font-size: 8px;
            line-height: 9px;
            letter-spacing: 0;
            white-space: pre;
        }}
    </style>
</head>
<body>
{ascii_art}
</body>
</html>
    """
    return html


@app.route('/', methods=['GET', 'POST'])
def index():
    ascii_result = None
    original_image = None

    if request.method == 'POST':
        # Check if image was uploaded
        if 'image' in request.files:
            image_file = request.files['image']
            if image_file.filename != '':
                # Read the width parameter
                width = int(request.form.get('width', 100))

                # Read the character set
                char_set = request.form.get('chars', " .:-=+*#%@")

                # Open the image
                img = Image.open(image_file)

                # Convert to ASCII
                ascii_result = image_to_ascii(img, width, char_set)

                # Create a base64 version of the original image
                buffered = io.BytesIO()
                img.save(buffered, format="JPEG")
                original_image = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return render_template('index.html', ascii_result=ascii_result, original_image=original_image)


@app.route('/download', methods=['POST'])
def download():
    ascii_art = request.form.get('ascii_art', '')

    # Create HTML version
    html_content = create_html_ascii_art(ascii_art)

    # Create a temporary file
    with open('temp_ascii_art.html', 'w') as f:
        f.write(html_content)

    # Also save as text
    with open('temp_ascii_art.txt', 'w') as f:
        f.write(ascii_art)

    # Return the file for download (HTML version)
    return send_file('temp_ascii_art.html', as_attachment=True, download_name='ascii_art.html')


if __name__ == '__main__':
    app.run(debug=True)