from image_to_ascii import *

def main():
    img = load_image("bulbasaur_tb.png")
    print(resize_image(img))

if __name__ == "__main__":
    main()