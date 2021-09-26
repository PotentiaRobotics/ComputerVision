import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Thresholding is a binarization of an image (an image where pixels are either white or black, (0, 255))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # thresh is the image returned and threshold is the value you inputted which would be 150
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) # thresh is the image returned and threshold is the value you inputted which would be 150
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding (computer finds the optimal thresholding value)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)  # Gaussian puts weight on certain pixels so that's why it looks clearer
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)