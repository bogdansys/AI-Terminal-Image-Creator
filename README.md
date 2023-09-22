# AI-Powered Image to ASCII Converter

A Python script that leverages OpenAI's DALL·E to generate images from text prompts and subsequently converts those images into ASCII art suitable for displaying in terminal or text documents.

## Prerequisites

- Python 3.x

## Installation

1. **Clone the repository**:

git clone https://github.com/bogdansys/AI-Terminal-Image-Creator


2. **Navigate to the repository's directory**:

cd AI-Terminal-Image-Creator


3. **Install the required packages**:

pip install -r requirements.txt

On some machines, installing requirements fails. If this is the case, install them manually with pip: 
pip install pillow
pip install openai
pip install requests


## Usage

To generate an image from a text prompt using DALL·E and then convert it into ASCII art, execute the script:

python main.py


Upon execution, the script will prompt you for:

- OpenAI API key (if not already saved).
- A text prompt for DALL·E to generate an image.
   
The ASCII representation width is set to 100 characters by default. If you want a different width, modify the code accordingly.

## Example

Simply execute:

python main.py


And follow the on-screen prompts.

## Contributing

Contributions are welcome! Please submit pull requests for any enhancements or bug fixes.

## License

This project is open-source and available under the MIT License.

