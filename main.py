import os
import time
import string
import random
from PIL import Image

def create_output_folders(output_folder_path):
    # Create output folders if they don't exist.
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

def generate_colour_codes():
    # Generate RGB colour codes for characters.
    dictionary_of_colours = {}
    all_printable_chars = [char for char in string.printable if char in string.ascii_letters or char in string.digits or char in string.punctuation or char in string.whitespace]

    red_chan = 0
    green_chan = 0
    blue_chan = 0

    for i, char in enumerate(all_printable_chars):
        rgb_code = (red_chan, green_chan, blue_chan)
        dictionary_of_colours[char] = rgb_code

        red_chan =   random.randint(0, 255)
        blue_chan =  random.randint(0, 255)
        green_chan = random.randint(0, 255)

        red_chan %= 256
        green_chan %= 256
        blue_chan %= 256

    return dictionary_of_colours

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
    output_folder_path = rf"{src}/output"
    create_output_folders(output_folder_path)
    colour_codes = generate_colour_codes()

    width = get_valid_input("Enter the desired width of the output image:\n")
    height = get_valid_input("Enter the desired height of the output image:\n")

    input_string = input("Enter the input string:\n")
    while not input_string:
        print("Invalid input. Please enter a non-empty string.")
        input_string = input("Enter the input string:\n")

    image = generate_image(input_string, width, height, colour_codes)

    output_file_path = rf'{output_folder_path}/output.png'
    image.save(output_file_path)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Image saved to: {output_file_path}")
    print(f'Total processing time: {total_time:.2f} seconds')

if __name__ == "__main__":
    main()