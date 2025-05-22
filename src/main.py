from image_to_ascii import *

def main():    
    image_path = input("Hello, please enter the path to your image: ")
    image_width = int(input("And desired output width: "))
    img = load_image(image_path)
    img_resized = resize_image(img, image_width)
    img_gray = convert_to_grayscale(img_resized)
    img_ascii = map_pixels_to_ascii(img_gray)
    lines = format_ascii_output(img_ascii, image_width)
    save_or_display_ascii(lines)

if __name__ == "__main__":
    main()