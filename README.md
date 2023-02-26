# text-to-pixel-image

*This Python script uses the `PIL (Python Imaging Library) module` to create an image consisting of squares, where each square represents a character from a user-provided input string. The colours of the squares are determined by a pre-defined colour code dictionary (`sorted_chars.json`), which maps each character to a hexadecimal colour code.*

## Prerequisites

- Python 3.x
- Pillow package (can be installed via pip: pip install Pillow)

## Usage

1. Place the sorted_chars.json file in the same directory as the script. Use `colour generator.py` to regenerate a new set of colours.
2. Run the script in the terminal or command prompt: python script_name.py
3. Enter the desired width and height (in pixels) of the output image when prompted.
4. Enter the input string to be converted to the image when prompted.
5. The resulting image will be saved as output.png in the same directory as the script.
