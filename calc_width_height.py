from PIL import Image
import numpy as np

image_path = '/home/alexj/PycharmProjects/VideoTraining/resized_images/frame180.jpg'

with Image.open(image_path) as img:
    width, height = img.size

print(f"Width: {width}, Height: {height}")

