import cv2 as cv
import numpy as np 

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# a color image consists of multiple channels: red, gree, and blue
# openCV allows us to split an image into its respective color channels

b, g, r = cv.split(img)    # grayscale because it shows the pixel intensity with the lighter portion showing higher concentration of a color

blue = cv.merge([b,blank,blank])   # sets green and red components to black
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)   # grayscale images have a shape of 1
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

cv.waitKey(0)