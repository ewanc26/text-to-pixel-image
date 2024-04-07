# text-to-pixel-image

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

*This Python script utilizes the `PIL (Python Imaging Library) module` to generate an image composed of squares, with each square representing a character from a user-provided input string. The colours of the squares are determined by randomly generated RGB colour codes.*

## Prerequisites

- Python 3.x
- Pillow package (can be installed via pip: `pip install Pillow` or `pip3 install Pillow` on UNIX based systems such as macOS)

## Usage

1. Ensure that `sorted_chars.json` is in the same directory as the script. You can use `colour generator.py` to create a new set of colours.
2. Run the script in the terminal or command prompt: `python main.py`
3. Input the desired width and height (in pixels) of the output image when prompted.
4. Enter the string you want to convert into an image when prompted.
5. The resulting image will be saved as `output.png` in the same directory as the script.

## Script Explanation

- The script generates random RGB colour codes for characters in the input string.
- It then creates an image based on the input string and colour codes, with each character represented by a coloured square.
- The dimensions of the output image are specified by the user.
- The processing time for image generation is displayed upon completion.
