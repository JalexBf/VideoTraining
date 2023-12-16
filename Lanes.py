import cv2
import numpy as np
from helpers.Decor import Helper


class Lanes:
    def __int__(self):
        # Initialize parameters for lane detection
        self.low_threshold = 50
        self.high_threshold = 150
        self.rho = 1
        self.theta = np.pi / 180
        self.threshold = 15
        self.min_line_length = 40
        self.max_line_gap = 20

    @Helper.screen_capture_routine
    def detect_lanes(self, frame):
        # Convert the image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Canny edge detection
        edges = cv2.Canny(blur, 50, 150)

        # You can display the result to see the effect
        cv2.imshow("Edges", edges)

        return frame