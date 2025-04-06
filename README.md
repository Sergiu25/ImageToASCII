# ImageToASCII
ImageToASCII is a website built using HTML and CSS for the frontend, and Python with the Flask framework for the backend.

The first version of the program was a simple script where I manually provided the image path, and it would generate an HTML page with the ASCII result and a .txt file with the output. But after a while, I realized it was too exhausting to change the image every time—I had to search for the path and paste it into the script. That’s when I decided to create a web interface for the program using Flask.
![Screenshot (17)](https://github.com/user-attachments/assets/25a7d23f-d103-47be-87c0-6864705c9863)

To be honest, this is my first time using a web framework, and I’m really excited about this project! Sure, it’s a small project—it only does maybe 4 things—but I truly enjoyed working on it, and I’m proud of the result.
![Screenshot (18)](https://github.com/user-attachments/assets/8113da81-a920-42a4-a01c-340d7d4ede0b)

This is how the output looks.

The logic behind the ASCII conversion is based on nested for loops. If you check app.py, you'll see that I first loop through the image height and then through the width. I calculate the brightness of each pixel and map it to a character based on its value. There’s more technical detail involved, but I’ve kept it simple in this README.

