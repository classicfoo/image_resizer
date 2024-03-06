# Image Resizer and Compressor

This Python script resizes and compresses images to a target file size of less than 10KB. It takes input images and resizes them to 150x150 pixels while compressing them until the resulting file size is under 10KB. The compressed images are saved in the same directory as the original images with "-min" appended to the filenames.

## Requirements:
Python 3.x
Pillow library (pip install Pillow)

## Usage:
Save the provided Python script in the directory containing the images you want to resize and compress.
Open a terminal or command prompt and navigate to the directory containing the Python script.

Run the script by double clicking on image_resizer.pyw

The script will resize and compress all images in the directory, saving the resulting images with "-min" appended to their filenames.

## Features:
Image Resizing: Images are resized to 150x150 pixels to reduce dimensions.
File Compression: Images are compressed to achieve a target file size of less than 10KB.
Automatic Processing: Simply run the script in the directory containing the images, and it will process all eligible images.

## Notes:
Input images can be in PNG, JPG, or JPEG format.
Output images are saved with "-min" appended to the original filenames.

## Example:
Suppose you have an image named example.jpg in your directory. Running the script will resize and compress the image, saving the result as example-min.jpg.

Feel free to use, modify, and contribute to this project!
