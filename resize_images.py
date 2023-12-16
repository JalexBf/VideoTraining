from PIL import Image
import os


def resize_images(input_dir, output_dir, target_width, target_height):
    # Create the output directory 
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            # Open image using PIL
            with Image.open(input_path) as img:
                # Resize image while preserving the aspect ratio
                img = img.resize((target_width, target_height), Image.LANCZOS)

                img.save(output_path)


input_dir = '/home/alexj/PycharmProjects/VideoTraining/images'
output_dir = '/home/alexj/PycharmProjects/VideoTraining/resized_images'

# Target dimensions (608x608)
target_width = 608
target_height = 608

# Resize images
resize_images(input_dir, output_dir, target_width, target_height)

print(f"All images resized to {target_width}x{target_height} and saved in {output_dir}")
