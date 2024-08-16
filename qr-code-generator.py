import requests

# handle input text/url
print("write the text here : ")
text = input()

# api
response = requests.get('https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + text)

if response.status_code == 200:
    # Define the path and save the image
    image_path = "qr-code.jpg"
    with open(image_path, 'wb') as file:
        file.write(response.content)
    print(f"Image saved successfully at {image_path}")
else:
    print(f"Failed to retrieve the image. Status code: {response.status_code}")