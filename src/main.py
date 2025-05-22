import sys
from image_to_ascii import *

def main():
    if len(sys.argv) > 2:
        image_path = sys.argv[1]
        image_width = int(sys.argv[2])
        img = load_image(image_path)
        img_resized = resize_image(img, image_width)
        img_gray = convert_to_grayscale(img_resized)
        img_ascii = map_pixels_to_ascii(img_gray)
        lines = format_ascii_output(img_ascii, image_width)
        save_or_display_ascii(lines)
    else:        
        print(
            "Not enough arguments were passed!\n"
            "Usage:\n"
            "  python3 src/main.py <path-to-image> <width>\n"
            "\n"
            "Example:\n"
            "  python3 src/main.py ./image.png 100"
        )

if __name__ == "__main__":
    main()