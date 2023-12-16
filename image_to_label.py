import os

"""
    Detect images without an label file
    or labels without images
"""

image_dir = '/home/alexj/PycharmProjects/VideoTraining/images'
annotation_dir = '/home/alexj/PycharmProjects/VideoTraining/labels'

# List of image and annotation filenames (without extensions)
image_files = {os.path.splitext(f)[0] for f in os.listdir(image_dir) if f.endswith('.jpg')}
annotation_files = {os.path.splitext(f)[0] for f in os.listdir(annotation_dir) if f.endswith('.txt')}

# Images without labels
images_without_labels = image_files - annotation_files

# Labels without images
labels_without_images = annotation_files - image_files

print("Images without labels:", images_without_labels)
print("Labels without images:", labels_without_images)
