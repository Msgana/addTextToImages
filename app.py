#Install pillow image libraty ->  https://pypi.org/project/pillow/
from PIL import Image, ImageDraw,ImageFont
import os

def add_text_to_image(image_path, text, output_path):
    # Open the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Specify the path to your custom font
    font_path = "./files/Roboto/Roboto-Regular.ttf"
    
    # Choose a font and size
    font_size = 26
    font = ImageFont.truetype(font_path, font_size)
    
    # Calculate text size and position
    text_width, text_height = draw.textsize(text, font=font)
    text_position = (20, image.size[1] - text_height - 20)  # Adjusted for bottom left position
    
    # Add text to the image
    draw.text(text_position, text, fill=(255, 255, 255), font=font)
    
    # Save the modified image
    image.save(output_path)
    print(f"Text added to {output_path}")

def main():
    input_directory = "./files/input"
    output_directory = "./files/output"

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Loop through images in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            filename_without_extension = os.path.splitext(filename)[0]
            add_text_to_image(input_path, filename_without_extension, output_path)

if __name__ == "__main__":
    main()
