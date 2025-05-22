from image_to_ascii import *

ASCII_WIDTH = 64

def main():    
    image_path = input("Hello, please enter the path to your image: ")
    img = load_image(image_path)
    img_resized = resize_image(img, ASCII_WIDTH)
    img_gray = convert_to_grayscale(img_resized)
    img_ascii = map_pixels_to_ascii(img_gray)
    lines = format_ascii_output(img_ascii, ASCII_WIDTH)
    save_or_display_ascii(lines)

if __name__ == "__main__":
    main()