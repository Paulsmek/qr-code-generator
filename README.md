This Python script generates a QR code from user-provided text or URL using the requests library to interact with an online API. The generated QR code is saved as an image file on the local machine.

How It Works:

User Input: The script prompts the user to input text or a URL that they want to encode into a QR code.

API Request: The script sends a GET request to the qrserver.com API with the provided text or URL as data.

QR Code Generation: The API generates a QR code based on the input and returns it as an image file.

Saving the Image: If the API request is successful, the script saves the QR code image as qr-code.jpg in the current directory.

Error Handling: If the API request fails, the script will print an error message with the HTTP status code.

Usage:

"python3 qr_code_generator.py"

When prompted, input the text or URL

