# -*- coding: utf-8 -*-
"""
Open CV Camera Test Timelapse Async

Created on Sat Feb  16 16:58 2019

This script captures timelapse imagery from a camera based on examples from:
https://www.idtools.com.au/time-lapse-photography-python-opencv/

The Async version attempts to add keyboard listening and display concurently

@author: rschm
"""

import numpy as np
import cv2
import asyncio

loop = asyncio.get_event_loop()

nframes = 6
interval = 5

#VideoCapture(0) is for internal camera, VideoCapture(1) is for external
cap = cv2.VideoCapture(0)

async def periodic_capture():

	for i in range(nframes):

		# Capture frame-by-frame
	    ret, image = cap.read()

	    # Save file
	    cv2.imwrite('./img_'+str(i).zfill(5)+'.png',image)

	    #await 5 seconds
	    await asyncio.sleep(interval)

	    #Display the resulting frame
	    cv2.imshow('frame',image)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	    	break

# Run periodic_capture function
if __name__ == '__main__':
	loop.run_until_complete(periodic_capture())

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
