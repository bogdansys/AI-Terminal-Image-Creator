# Image to ASCII Converter

A simple Python script that converts images into ASCII art, suitable for displaying in terminal or text documents.

## Prerequisites

Ensure you have Python 3.x installed. 

## Installation

1. Clone this repository: git clone https://github.com/bogdansys/AI-Terminal-Image-Creator

2. Navigate to the repository's directory: cd AI-Terminal-Image-Creator

3. Install the required packages:pip install -r requirements.txt


## Usage

To convert an image (JPEG or JPG) into ASCII art, use the following command:

python main.py [PATH_TO_YOUR_IMAGE] --width [DESIRED_WIDTH]


- Replace `[PATH_TO_YOUR_IMAGE]` with the path to the image you wish to convert.
- The `--width` argument defines the width of the ASCII representation. Adjust it to fit your terminal or desired size. If not specified, it defaults to 100 characters in width.

## Example

python main.py sample.jpeg --width 150 

## Contributing

Contributions are welcome! Please submit pull requests for any enhancements or bug fixes.

## License

This project is open-source and available under the MIT License.

