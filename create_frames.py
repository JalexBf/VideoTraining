import cv2
import os

# Define the path to your video and the folder where you want to save the frames
video_path = 'video.mp4'  # Replace with your video path
save_folder = 'frames'

# Set frame size
new_width = 1280
new_height = 720

# Check if the frame folder exists, and if not create it
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Load video
video = cv2.VideoCapture(video_path)

# Check if the video is loaded correctly
if not video.isOpened():
    print("Error: Could not open video.")
    exit()

# Get the FPS of the video
fps = video.get(cv2.CAP_PROP_FPS)

# Calculate the interval for frame extraction (1 frame per 2 seconds)
interval = int(fps) * 2

# Frame count
count = 0

# Loop through each frame in the video
while True:
    # Read current frame
    success, frame = video.read()

    # If frame was not successfully read, break
    if not success:
        print("Finished reading the video.")
        break

    # Resize the frame
    frame = cv2.resize(frame, (new_width, new_height))

    # Display the frame
    cv2.imshow('Frame', frame)

    # Save the frame (one frame per second)
    if count % interval == 0:
        # Define the path for each frame
        frame_path = os.path.join(save_folder, f"frame{count}.jpg")
        # Save the frame at the specified path
        cv2.imwrite(frame_path, frame)

    # Increment frame count
    count += 1

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
