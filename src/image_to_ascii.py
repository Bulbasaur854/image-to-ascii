from PIL import Image
import math

ASCII_RAMP = list("@%#*+=-:. ")
ASCII_RAMP.reverse()


def load_image(filepath):
    return Image.open(filepath)

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width    
    # because char height is usually twice as long as its width,
    # multiply new height by 0.5 in order to "squish characters",
    # this way ascii art displays better when printing
    new_height = int(ratio * new_width * 0.5)
    return image.resize((new_width, new_height))  

def convert_to_grayscale(image):
    return image.convert("RGBA").convert("L")

def map_pixels_to_ascii(image):
    pixels = image.getdata()    
    return "".join([ASCII_RAMP[pixel * (len(ASCII_RAMP) - 1) // 255] for pixel in pixels])

def format_ascii_output(ascii_chars, width):
    return list("".join(ascii_chars[i:i+width]) for i in range(0, len(ascii_chars), width))

def display_ascii(ascii_lines):
    for line in ascii_lines:
        print(line)