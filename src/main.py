from image_to_ascii import *

ASCII_WIDTH = 50

def main():    
    img = load_image("bulbasaur_example.png")
    img_resized = resize_image(img, ASCII_WIDTH)
    img_gray = convert_to_grayscale(img_resized)
    img_ascii = map_pixels_to_ascii(img_gray)
    lines = format_ascii_output(img_ascii, ASCII_WIDTH)
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()