"""
RPi - Open CV Camera Test Color.py
Originally Created on Tue Feb 5 17:58:10 2019
Author: OpenCV Example / Ryan Schmalenberg
"""

import numpy as np
import cv2

#VideoCapture(0) is for internal camera, VidoCapture(1) is for external
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everthing done, release the capture
cap.release()
cv2.destroyAllWindows()
