import sys
from image_to_ascii import image_to_ascii, display_ascii

def main():
    if len(sys.argv) == 3:
        image_path = sys.argv[1]
        image_width = int(sys.argv[2])
        
        ascii_lines = image_to_ascii(image_path, image_width)
        display_ascii(ascii_lines)
    else:        
        print(
            "Wrong number of arguments passed!\n"
            "Usage:\n"
            "  python3 src/main.py <path-to-image> <width>\n"
            "\n"
            "Example:\n"
            "  python3 src/main.py ./image.png 100"
        )

if __name__ == "__main__":
    main()