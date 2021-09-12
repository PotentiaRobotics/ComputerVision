import cv2 as cv

img = cv.imread('Photos/park.jpg')

cv.imshow('park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray) 

img = cv.imread('Photos/meme.jpg')

cv.imshow('Meme', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   # convert bgr image to grayscale image 
cv.imshow('Meme', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)   # kernel size has to be an odd number (increase size to increase blur)
cv.imshow('Blur', blur)

# Edge cascade
canny = cv.Canny(blur, 125, 175) # can reduce the amount of edges by using blur instead of img
cv.imshow('Canny Edges', canny)  

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations = 3) # increase to make edges thicker basically
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations = 3)  # reverse dilation and try to close to same edge cascade as original
cv.imshow('Eroded', eroded)

# Resize                             # cv.INTER_CUBIC is slowest of them all, but image that you get is much higher quality 
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)   # does not put into account aspect ratio 
cv.imshow('Resized', resized)   # interpolation = cv.INTER_AREA is useful when shrinking the image to dimensions that are smaller than original

# Cropping  (images are arrays, and we can employ array splicing which is basically selecting a portion of the image on the basis of their pixel values)
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)