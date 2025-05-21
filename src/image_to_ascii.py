from PIL import Image

def load_image(filepath):
    return Image.open(filepath)