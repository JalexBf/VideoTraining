import os

"""
    Strip .xml extension from label files
"""

annotation_dir = '/home/alexj/PycharmProjects/VideoTraining/labels'

# Rename files
for filename in os.listdir(annotation_dir):
    if filename.endswith('.xml.txt'):
        new_name = filename.replace('.xml.txt', '.txt')
        os.rename(os.path.join(annotation_dir, filename),
                  os.path.join(annotation_dir, new_name))

print("Files renamed.")
