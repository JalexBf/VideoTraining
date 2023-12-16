import os

"""
    Create an empty label for images with no objects.
"""

image_dir = '/home/alexj/PycharmProjects/VideoTraining/no_objects'
annotation_dir = '/home/alexj/PycharmProjects/VideoTraining/labels'

# Create annotation directory if it doesn't exist
if not os.path.exists(annotation_dir):
    os.makedirs(annotation_dir)

# Process each image in the directory
for filename in os.listdir(image_dir):
    if filename.endswith('.jpg'):
        # Create an empty annotation file for each image
        annotation_path = os.path.join(annotation_dir, filename.replace('.jpg', '.txt'))
        open(annotation_path, 'w').close()

print("Empty annotation files created.")
