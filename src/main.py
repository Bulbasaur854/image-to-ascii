from image_to_ascii import *

def main():
    img = load_image("bulbasaur_example.png")
    print(f"Original Image: {img}")
    img_resized = resize_image(img)
    print(f"Resized Image: {img_resized}")
    img_gray = convert_to_grayscale(img_resized)
    print(f"Gray Scaled Image: {img_gray}")

if __name__ == "__main__":
    main()