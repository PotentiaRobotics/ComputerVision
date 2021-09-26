import cv2 as cv
import numpy as np

img = cv.imread('Photos/tj.jpg')

cv.imshow('TJHSST', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]]) # create a translation matrix which takes in a list with two lists inside of it
    dimensions = (img.shape[1], img.shape[0])  # tuple of img.shape[1]
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:    # assuming were going to rotate around the center if no rotation point is given
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)   # 1.0 = scale
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)   # input negative value for degrees if wanting clockwise
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, 45)
cv.imshow('Rotated Rotated', rotated_rotated)  # black lines is default when there's no image there
                                            # rotated black triangeles along with the image (can save this trouble by just adding the total angle change you want)

# Resizing 
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)   #for resizing to smaller just use default
cv.imshow('Resized', resized)

# Flipping 
flip = cv.flip(img, 0)
# takes in 3 possible flip codes:
# 0 implies flipping the image vertically (over x-axis)
# 1 specifies flipping the image horizontally (over the y-axis)
# -1 implies flipping the image both vertically and horizontally
cv.imshow('Flip', flip)

# Cropping 
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)