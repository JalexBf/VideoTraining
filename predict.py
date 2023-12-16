import os
import subprocess
import re

darknet_path = '/home/alexj/PycharmProjects/darknet-master'
frames_path = '/home/alexj/PycharmProjects/VideoTraining/images'
yolo_config = os.path.join(darknet_path, 'cfg/yolov3-tiny.cfg')
yolo_weights = os.path.join(darknet_path, 'yolov3-tiny_final.weights')

# Change working directory to Darknet directory
os.chdir(darknet_path)

# List all frames in the frames directory
frames = [f for f in os.listdir(frames_path) if f.endswith('.jpg')]

# Run detection on each frame
for frame in frames:
    frame_path = os.path.join(frames_path, frame)
    command = f"./darknet detect {yolo_config} {yolo_weights} {frame_path}"
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Process and print the output
    output = process.stdout.decode()
    matches = re.findall(r'([a-zA-Z0-9]+): (\d+)%', output)  # Capture class label and confidence score
    if matches:
        detections = [f"{label} ({score}%)" for label, score in matches]
        print(f"{frame}: {', '.join(detections)}")
    else:
        print(f"{frame}: No detection")