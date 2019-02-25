#############################
# Author: Joshua Cullings   #
# Date: 2/24/2019           #
#                           #
#############################

# taking the running average of images grayscaling and subtracting it from the current image
'''
App Instructions
----------------------------------------------

----------------------------------------------
ESC - close program
1   - toggle HSV
'''

#importing the necessary packages
import numpy as np
import cv2 as cv
import time

print(__doc__)

src = cv.VideoCapture(0)
previous, frame = src.read()

while(True):
    tf, frame = src.read()
    cv.imshow("Live Feed", frame)
    
    #hsv functionality
    if hsvKey == 1:
        cv.imshow("HSV", hsv)
    else:
        cv.destroyWindow("HSV")

    keyboard = cv.waitKey(33)
    if keyboard == 27:
        break

    #setting hsv conversion to 1
    elif keyboard == 49:
        hsvKey = hsvKey+1
        hsvKey = hsvKey%2

    previous = frame
        
src.release()
cv.destroyAllWindows()

#Extra code for flip functionality
"""        if flipKey == 1:
            image1 = cv.flip(image1, 0)
            cv.imshow('image1', image1)
            
    elif flipKey == 1:
        image1 = cv.flip(image1, 0)
        cv.imshow('image1', image1)
"""
#####################################
# RESOURCES USED:                   #
# - opencv/sources/samples/python   #
# - https://stackoverflow.com/      #
#   questions/13538748/crop-black-  #
#   edges-with-opencv               #
# - https://www.opencv-srf.com/2011 #
#   /11/mouse-events.html           #
#                                   #
#####################################
