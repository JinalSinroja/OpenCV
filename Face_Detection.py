# Face detection is done using classifier
# classifier is an algorithm that decides wherether a face is present or not
# classifier need to be trained images thousands of with and without the faces.
# Opencv have pretrained classifier called haarcascade, localbinary pattern.
import cv2 as cv

img = cv.imread('Images/group.jpg')
cv.imshow('group', img)

# firstly we covert an image into grayscale because face detection does not involve any colors
# haarcascade looks at object in an image and using edges find the faces in an image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayScale', gray)

# Now Reading into haarcascade file
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Detection of Face
face_rect = haar_cascade.detectMultiScale(gray, 1.1, minNeighbors=3) # detects a face and returns list of the rectangle coordinates of each faces
print(f'No. of faces detected : {len(face_rect)}')
# print(face_rect)

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,0,255), thickness=2)

# so for the group of people haarcascade is more sensitiveto noise which will end up with more no. of faces than the actual no. of faces
# less minNeighbour value leads to more face and vise versa
cv.imshow('Detected_Faces', img)
cv.waitKey(0)