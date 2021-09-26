import cv2 as cv

img = cv.imread('Photos/cat.jpg')  # takes in a path to an image and returns that image as a matrix of pixels

img = cv.imread('Photos/cat_large.jpg')  # image is far greater than dimensions of monitor

cv.imshow('Cat', img)  # displays image as a new window

# Reading videos

capture = cv.VideoCapture('videos/dog.mp4')   # provide integer argument if using webcam (0 is webcam, 1 is first camera connected to computer)

while True:
    isTrue, frame = capture.read()  # capture.read reads in video frame by frame and returns the frame and a boolean that says whether the frame was succesfully read in or not
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):   # if d is pressed break out of loop and stop displaying video
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)    # keyboard binding function (waits for a specific delay in milliseconds for a key to be pressed)