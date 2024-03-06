from PIL import Image
import os

def resize_and_compress_image(input_image_path, output_image_path):
    # Open the image file
    with Image.open(input_image_path) as img:
        # Resize the image to 200x200
        img = img.resize((200, 200))
        
        # Compress and save the image
        img.save(output_image_path, optimize=True, quality=50)

def main():
    # Get the list of image files in the current directory
    image_files = [f for f in os.listdir() if os.path.isfile(f) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        # Construct the output filename
        output_filename = os.path.splitext(image_file)[0] + "-min" + os.path.splitext(image_file)[1]
        output_image_path = os.path.join(os.path.dirname(image_file), output_filename)

        # Resize and compress the image
        resize_and_compress_image(image_file, output_image_path)

if __name__ == "__main__":
    main()
