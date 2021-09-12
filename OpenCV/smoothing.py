import cv2 as cv

img = cv.imread('Photos/cats.jpg')  # apply a blurring method to smooth out the image or reduce some of the noise
cv.imshow('Cats', img)

# kernel (or window) = a "window" you draw over an image
# the size of the window is called "kernel size" (# of rows and # of columns)
# blur is applied to the middle pixel as a result of the pixels around it (surrounding pixels)

# Averaging (the window will compute the pixel intesity of the middle pixel of the true center as the average of the surrounding pixel intensities)
average = cv.blur(img, (3,3))   #increase kernel size to increase blur
cv.imshow('Average Blur', average)

# Gaussian Blur (each surrounding pixel is given a weight, and the average of the products of those weights give you the value for the true center)
# less blur, but more natural than averaging
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur (same as averaging, except it finds the median of the surrounding pixels instead of the average)
# more effective in reducing noise in an image compared to Averaging and Gaussian Blur  
median = cv.medianBlur(img, 3)  # openCV automatically assumes that this kernel size will be a 3 by 3 just by the integer 
cv.imshow('Median Blur', median)  # not meant for high kernel sizes like 7

# Bilateral Blurring (applies blurring but retains the edges in the image)
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)