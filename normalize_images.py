from PIL import Image
import torchvision.transforms as transforms

# Path to your image
image_path = '/home/alexj/PycharmProjects/VideoTraining/resized_images/frame0.jpg'
output_path = 'normalized_image.jpg'

# Load the image
image = Image.open(image_path).convert('RGB')

# Define the normalization transform
normalize_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Normalize the image
normalized_tensor = normalize_transform(image)

# Convert the tensor to an image
normalized_image = transforms.ToPILImage()(normalized_tensor)

# Save the image
normalized_image.save(output_path)
