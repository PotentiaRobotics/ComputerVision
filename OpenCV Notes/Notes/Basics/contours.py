import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# contours (curves that join the points along the boundary) and edges are different (but basically same and can technically treat them as the same)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #loooks at an image and tries to binarize it
# if density of a pixel is below 125 its going to be set to 0 or black and if its above 125 it is set to white or 255 
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)   
# contours are a python list of all coordinates of the contours that were found in the image
# hierarchies refers to the hierarchacal representation of the contours 

# cv.RETR_LIST (returns all contours) is a mode in which the find contours methods returns and finds the contours
# RETR_EXTERNAL (retirms all external or outside)
# RETR_TREE (returns all hierarchacal contours)

# contour approximation methods: how we want to approximate the contour 
# CHAIN_APPROX_NONE does nothing and just returns all the contours
# CHAIN_APPROX_SIMPLE compresses all the contours that were returned into simple ones that make most sense

print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)  #contours that were drawn in image
cv.imshow('Contours Drawing', blank)

cv.waitKey(0)
