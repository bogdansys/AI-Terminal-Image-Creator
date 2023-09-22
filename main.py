from PIL import Image

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
    import argparse
    parser = argparse.ArgumentParser(description="Convert an image to its ASCII representation.")
    parser.add_argument("image_path", help="Path to the image file.")
    parser.add_argument("--width", type=int, default=100, help="Width of the output ASCII representation.")
    args = parser.parse_args()

    ascii_result = image_to_ascii(args.image_path, args.width)
    print(ascii_result)
