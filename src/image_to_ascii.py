from PIL import Image
import math

def load_image(filepath):
    return Image.open(filepath)

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(ratio * new_width)   

    return image.resize((new_width, new_height))  

def convert_to_grayscale(image):
    return image.convert("LA")