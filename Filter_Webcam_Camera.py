# Charlotte Meola, 1/31/2019

# Program to capture webcam video, display stream, capture an image, filter image, and display filtered image.
# Edge detection used to determine contours of human fac.
# OpenCV used to verify human face and place borer around verified human face.

# Some resources for face recognition and edge detection:
# https://pdfs.semanticscholar.org/5ee5/5db7322cf5445a110e8e0ed11ddfef0f4d9d.pdf
# https://realpython.com/face-recognition-with-python/

# Canny Edge Detection algorithm and stages explained here:
# https://docs.opencv.org/3.1.0/da/d22/tutorial_py_canny.html
# ------------------------------------------------------------------------------------------------------

import cv2

# Import for Canny Edge Detection - IF plotted filtered image data is desired.
import numpy as np
from matplotlib import pyplot as plt

# Show message box displaying directions to user:
import tkinter
from tkinter import messagebox
# Hide main window:
root = tkinter.Tk()
root.withdraw()
# Info message box display:
messagebox.showinfo("Information", "Press the Spacebar to capture image.  Press Escape to stop.")

# Find computer camera and camera stream:
cam = cv2.VideoCapture(0)

# Create user GUI window:
# Name this namedWindow the same title of frame, below:
cv2.namedWindow("Unfiltered Webcam Stream")
cv2.namedWindow("Filtered Webcam Stream")

# Initialize counter for how many images will be processed:
img_counter = 0

while True:
    ret, frame = cam.read()
    # Name this frame the same title of namedWindow, above
    cv2.imshow("Unfiltered Webcam Stream", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # If ESC is pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        img_name = "Webcam_Image_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        print("Image from webcam is shown")

        # Apply Canny Edge Detection to webcam images -
        img = cv2.imread(img_name, 0)
        edges = cv2.Canny(img, 100, 200)
        cv2.imshow("Filtered Webcam Stream", edges)

        # Increase count to name next image saved
        img_counter += 1


# Release and close camera (webcam) once the escape button is pushed and break is activated.
cam.release()
cam.close()

# Close windows displaying camera feed.
cv2.destroyAllWindows()