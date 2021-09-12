import cv2 as cv
import numpy as np


blank = np.zeros((500, 500, 3), dtype='uint8')   # uint8 is data type of image    # (height, width, # of color channels)
cv.imshow('Blank', blank)

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

#1. Paint the image a certain color
blank[:] = 0, 255, 0  # ":" indicates all pixels (painting all pixels green)
cv.imshow('Green', blank)

blank[200:300, 300:400] = 0,0,255
cv.imshow('Red Portion', blank)

#2. Draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = -1)    # use cv.FILLED method or -1 as thickness to fill rectangle
cv.imshow('Rectangle', blank)

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness = -1)  # scaled entire rectangle into 1/2 of original image
cv.imshow('Rectangle', blank)

#3. Draw a circle
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness = -1)
cv.imshow('Circle', blank)

#4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness = 3)
cv.imshow('Line', blank)

#5. Write text
cv.putText(blank, 'Hello, my name is Ryan!', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness = 2)
cv.imshow('Text', blank)

cv.waitKey(0)