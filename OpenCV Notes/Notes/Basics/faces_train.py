import os
import cv2 as cv
import numpy as np

# create a list of all the people in the image
# people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']  # can manually type it

people = []  # OR you could loop over every folder in the folder below
for i in os.listdir(r'C:\Users\user\projects\git\opencv-course\Resources\Faces\train'):
    people.append(i)

# print(p)

# create a variable that is equal to the base folder (the folder that contains the five folders of the people)
DIR = r'C:\Users\user\projects\git\opencv-course\Resources\Faces\train'    # change to wherever the faces folder is located

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []  # the image
labels = []  # the label that goes with the feature (image)

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
                

create_train()
print('Training done -----------')

features = np.array(features, dtype = object)
labels = np.array(labels)

# print(f'Length of the features list = {len(features)}')
# print(f'Length of the labels list = {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)