from PIL import Image
import json
import os
from random import randint
from string import printable

src = os.path.dirname(os.path.realpath(__file__))
json_file = rf"{src}/json/sorted_chars.json"
output_folder = rf"{src}/output"

if not os.path.exists(os.path.dirname(json_file)):
    os.mkdir(os.path.dirname(json_file))

elif not os.path.exists(output_folder):
    os.mkdir(output_folder)

else:
    pass

with open(json_file) as f:
    colour_codes = json.load(f)

while True:
    try:
        width = int(input("Enter the desired width of the output image:\n"))
        height = int(input("Enter the desired height of the output image:\n"))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for width and height.")

squares_per_row = width // 10
num_rows = height // 10

image = Image.new('RGB', (width, height), 'white')

while True:
    input_string = input("Enter the input string:\n")
    if input_string:
        break
    else:
        print("Invalid input. Please enter a non-empty string.")

for char in input_string:
    if char in printable:
        pass
    else:
        print(f"Invalid character found! ('{char}')\nPlease don't use '{char}'.")

index = 0
x, y = 0, 0
for row in range(num_rows):
    for square_index in range(squares_per_row):
        if index >= len(input_string):
            index = 0
        char = input_string[index]
        colour_code = colour_codes.get(char, '000000')  # Default to '000000' if char not found
        colour = tuple(int(colour_code[i:i + 2], 16) for i in (0, 2, 4))
        square = (x, y, x + 10, y + 10)
        colour_image = Image.new('RGB', (10, 10), colour)
        image.paste(colour_image, square)
        x += 10
        index_shift = randint(0, 3)
        index = (index + index_shift) % len(input_string)
    y += 10
    x = 0

image.save(rf'{output_folder}/output.png')
