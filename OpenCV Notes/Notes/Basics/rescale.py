import cv2 as cv

img = cv.imread('Photos/cat.jpg') 
cv.imshow('Cat', img) 

def rescaleFrame(frame, scale = 0.75):
    # images, videos, and live video
    width = int(frame.shape[1] * scale)    # frame.shape[1] is basically width
    height = int(frame.shape[0] * scale) # frame.shape[0] is basically height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # live video
    capture.set(3,width)    # makes 3 reference width
    capture.set(4,height)   # makes 4 reference height



resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

# reading videos

capture = cv.VideoCapture('videos/dog.mp4')   # provide integer argument if using webcam (0 is webcam, 1 is first camera connected to computer)

while True:
    isTrue, frame = capture.read()  # capture.read reads in video frame by frame and returns the frame and a boolean that says whether the frame was succesfully read in or not
    
    frame_resized = rescaleFrame(frame, 0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):   # if d is pressed break out of loop and stop displaying video
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)