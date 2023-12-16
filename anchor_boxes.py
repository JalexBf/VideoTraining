import numpy as np
from sklearn.cluster import KMeans

bounding_boxes = np.loadtxt('bounding_boxes.txt')

# K-Means Clustering
num_anchors = 9     # Number of anchors
kmeans = KMeans(n_clusters=num_anchors, random_state=0)
kmeans.fit(bounding_boxes)

# Extract the anchor boxes
anchors = kmeans.cluster_centers_

# Adjust anchors for YOLO
input_size = np.array([608, 608])
scaled_anchors = anchors * input_size

# Sort the anchors by area from smallest to largest
sorted_indices = np.argsort(scaled_anchors.prod(axis=1))
scaled_anchors = scaled_anchors[sorted_indices]

# Convert to integers (width, height)
scaled_anchors = scaled_anchors.astype(np.int)

print("Anchors =", scaled_anchors)
