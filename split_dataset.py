import os
import shutil
import random

# Step 1: Define your paths
current_dataset_path = '/home/alexj/PycharmProjects/VideoTraining/resized_images'
new_dataset_path = '/home/alexj/PycharmProjects/VideoTraining/dataset'
train_path = os.path.join(new_dataset_path, 'train')
val_path = os.path.join(new_dataset_path, 'val')

# Step 2: Create new directories
for path in [train_path, val_path]:
    os.makedirs(os.path.join(path, 'images'), exist_ok=True)
    os.makedirs(os.path.join(path, 'labels'), exist_ok=True)

# Step 3: Get a list of image files (change extensions as needed)
all_files = os.listdir(current_dataset_path)
all_images = [f for f in all_files if f.endswith('.jpg') or f.endswith('.png')]

# Step 4: Split the dataset
random.shuffle(all_images)
split = int(0.8 * len(all_images))  # 80% for training
train_images = all_images[:split]
val_images = all_images[split:]

# Step 5: Function to move the files
def move_files(file_list, source_folder, destination_folder):
    for file in file_list:
        # Move image
        image_src = os.path.join(source_folder, file)
        image_dst = os.path.join(destination_folder, 'images', file)
        shutil.move(image_src, image_dst)

        # Move corresponding annotation
        annotation_file = file.rsplit('.', 1)[0] + '.txt'  # Change extension for annotations if different
        annotation_src = os.path.join(source_folder, annotation_file)
        if os.path.exists(annotation_src):
            annotation_dst = os.path.join(destination_folder, 'labels', annotation_file)
            shutil.move(annotation_src, annotation_dst)

# Step 6: Move training images and annotations
move_files(train_images, current_dataset_path, train_path)

# Step 7: Move validation images and annotations
move_files(val_images, current_dataset_path, val_path)

print("Dataset organization complete.")

