from PIL import Image
import openai
import os
import requests
from io import BytesIO

API_KEY_PATH = "api_key.txt"

def save_api_key():
    api_key = input("Enter your OpenAI API key: ")
    with open(API_KEY_PATH, 'w') as f:
        f.write(api_key)

def get_api_key():
    if not os.path.exists(API_KEY_PATH):
        save_api_key()
    with open(API_KEY_PATH, 'r') as f:
        return f.read().strip()

def create_image_with_ai(api_key, prompt):
    openai.api_key = api_key
    
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="256x256" 
    )
    image_url = response['data'][0]['url']

    # Download the image from the URL
    response = requests.get(image_url)
    img_data = BytesIO(response.content)

    return Image.open(img_data)

def image_to_ascii(image_path, output_width):
    # Define a list of ASCII characters that will represent different brightness levels
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    # Open the image and convert it to grayscale
    image = Image.open(image_path).convert('L')

    # Get the aspect ratio
    width, height = image.size
    aspect_ratio = height / float(width)
    output_height = int(output_width * aspect_ratio)

    # Resize the image to fit the desired width
    image = image.resize((output_width, output_height))

    # Create the ASCII representation
    pixels = list(image.getdata())
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value * len(ASCII_CHARS) // 256]
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, output_width):
        ascii_img += ascii_str[i:i+output_width] + "\n"

    return ascii_img


if __name__ == "__main__":
    api_key = get_api_key()
    prompt = input("Enter a prompt for image creation: ")
    image = create_image_with_ai(api_key, prompt)
    image_path = "temp_image.jpg"
    image.save(image_path)
    ascii_result = image_to_ascii(image_path, 100)
    print(ascii_result)
    
    # Optionally delete the temporary image
    os.remove(image_path)
