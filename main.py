import os
import time
import json
import random
import sys
from PIL import Image

def create_output_folders(output_folder_path):
    # Create output folders if they don't exist.
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

def get_valid_input(prompt, input_type=int):
    # Prompt user for valid input.
    while True:
        try:
            user_input = input_type(input(prompt))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return user_input

def find_largest_divisor(n, min_divisor=10):
    # Find the largest divisor of n that is at least min_divisor.
    for divisor in range(min_divisor, 0, -1):
        if n % divisor == 0:
            return divisor
    return min_divisor  # Default to min_divisor if no larger divisor is found

def load_colour_codes(json_path):
    try:
        # Load colour codes from JSON file.
        with open(json_path, 'r') as file:
            colour_codes = json.load(file)
            # Validate the format of JSON content
            if not all(isinstance(v, list) and len(v) == 3 and all(isinstance(c, int) and 0 <= c <= 255 for c in v) for v in colour_codes.values()):
                raise ValueError("Invalid format in JSON file.")
            return colour_codes
    except FileNotFoundError:
        print(f"Error: File '{json_path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file. Please check the file format.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def generate_image(input_string, width, height, colour_codes):
    # Compute the largest suitable pixel size.
    pixel_size = find_largest_divisor(width, 10)
    squares_per_row = width // pixel_size
    num_rows = height // pixel_size

    image = Image.new('RGB', (width, height), 'white')

    index = 0
    x, y = 0, 0

    for row in range(num_rows):
        for square_index in range(squares_per_row):
            if index >= len(input_string):
                index = 0
            char = input_string[index]
            rgb_values = colour_codes.get(char)
            if rgb_values is not None:
                colour = tuple(rgb_values)
                square = (x, y, x + pixel_size, y + pixel_size)
                colour_image = Image.new('RGB', (pixel_size, pixel_size), colour)
                image.paste(colour_image, square)
                x += pixel_size
                index_shift = random.randint(1, 2)
                index = (index + index_shift) % len(input_string)
            else:
                print(f"No RGB values found for character '{char}'. Skipping.")
            index += 1
        y += pixel_size
        x = 0

    return image

def main():
    start_time = time.time()
    src = os.path.dirname(os.path.realpath(__file__))
    output_folder_path = os.path.join(src, "output")
    create_output_folders(output_folder_path)

    json_path = os.path.join(src, 'json', 'sorted_chars.json')
    colour_codes = load_colour_codes(json_path)

    width = get_valid_input("Enter the desired width of the output image:\n")
    height = get_valid_input("Enter the desired height of the output image:\n")

    input_string = input("Enter the input string:\n")
    while not input_string:
        print("Invalid input. Please enter a non-empty string.")
        input_string = input("Enter the input string:\n")

    image = generate_image(input_string, width, height, colour_codes)

    output_file_path = os.path.join(output_folder_path, 'output.png')
    image.save(output_file_path)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Image saved to: {output_file_path}")
    print(f'Total processing time: {total_time:.2f} seconds')

if __name__ == "__main__":
    main()