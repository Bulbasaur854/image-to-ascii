from PIL import Image
import math

ASCII_RAMP = [
    "$", "@", "B", "%", "8", "&", "W", "M", "#", "*", "o", "a", "h", "k", "b", "d",
    "p", "q", "w", "m", "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c",
    "v", "u", "n", "x", "r", "j", "f", "t", "/", "\\", "|", "(", ")", "1", "{", "}",
    "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", ",",
    "\"", "^", "`", "'", ".", " "
]
ASCII_RAMP.reverse()
# ASCII_RAMP = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]

def load_image(filepath):
    return Image.open(filepath)

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(ratio * new_width)       
    return image.resize((new_width, new_height))  

def convert_to_grayscale(image):
    return image.convert("RGBA").convert("L")

def map_pixels_to_ascii(image):
    pixels = image.getdata()    
    return "".join([ASCII_RAMP[pixel * (len(ASCII_RAMP) - 1) // 255] for pixel in pixels])

def format_ascii_output(ascii_chars, width=100):
    return list("".join(ascii_chars[i:i+width]) for i in range(0, len(ascii_chars), width))