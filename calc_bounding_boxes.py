import os

annotations_dir = '/home/alexj/PycharmProjects/VideoTraining/labels'

bounding_boxes = []

# Iterate over the annotation files and read the bounding box info
for filename in os.listdir(annotations_dir):
    if filename.endswith(".txt") and not filename.startswith("classes"):  # Avoid the classes.txt file
        with open(os.path.join(annotations_dir, filename), "r") as file:
            for line in file.readlines():
                _, x_center, y_center, width, height = map(float, line.split())
                bounding_boxes.append((width, height))  # Append width and height as a tuple to the list

# Save to a file:
with open('bounding_boxes.txt', 'w') as f:
    for bbox in bounding_boxes:
        f.write(f"{bbox[0]} {bbox[1]}\n")

