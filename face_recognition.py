import cv2 as cv
import numpy as np

people = ['jerry', 'madonna']
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# recognizer instance
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:/Users/jinal/Documents/Python training/Image Processing/OpenCV/Faces/train/madonna/15.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# face detection
face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for x,y,w,h in face_rect:
    face_region = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(face_region)
    print(f'label = {people[label]} with confidence of {confidence}') 

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,255,255), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,0,255), thickness=2)

cv.imshow('Detected face', img)

cv.waitKey(0)