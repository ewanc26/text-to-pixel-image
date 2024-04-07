import json
import os
import time
import string
import random

src = os.path.dirname(os.path.realpath(__file__))
json_file = rf"{src}/json/sorted_chars.json"

if not os.path.exists(os.path.dirname(json_file)):
    os.makedirs(os.path.dirname(json_file))

# Initialize dictionary to store characters and their RGB codes
dictionary_of_colours = {}

# Start time
start_time = time.time()

# Generate a list of printable characters
all_printable_chars = [char for char in string.printable if char in string.ascii_letters or char in string.digits or char in string.punctuation or char in string.whitespace]

# Calculate total number of characters
total_characters = len(all_printable_chars)

# Initialize RGB channels
red_chan = 0
green_chan = 0
blue_chan = 0

# Process characters
for i, char in enumerate(all_printable_chars):
    # Construct RGB code as a tuple
    rgb_code = (red_chan, green_chan, blue_chan)

    # Add the character and its RGB code to the dictionary
    dictionary_of_colours[char] = rgb_code

    red_chan =   random.randint(0, 255)
    blue_chan =  random.randint(0, 255)
    green_chan = random.randint(0, 255)

    # Reset RGB channels if they reach 256
    red_chan %= 256
    green_chan %= 256
    blue_chan %= 256

# Write the dictionary of characters and RGB codes to a JSON file
with open(json_file, 'w') as f:
    json.dump(dictionary_of_colours, f, indent=4)

# End time
end_time = time.time()
total_time = end_time - start_time

print(f'Data has been written to {json_file}')
print(f'Total processing time: {total_time:.2f} seconds')
