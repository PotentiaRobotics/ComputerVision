import cv2 as cv

# haar cascades are very sensitive to noise in an image 

img = cv.imread('Photos/group 1.jpg')
cv.imshow('Group of 5 People', img)

# haar cascades essentially look at an object in an image and using the edges, it determines whether it's a face or not 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# rectangular coordinates for the faces that are present in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 1)   # by minimizing these values, your making openCV more sensitive to noise

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)

# in order to do this on a video, just do it on each individual frame