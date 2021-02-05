import cv2 as cv
import os
import numpy as np

people = []
for i in os.listdir(r'C:/Users/jinal/Documents/Python training/Image Processing/OpenCV/Faces/train'):
    people.append(i)

# print(people) # Or else you can do this manually
DIR = r'C:/Users/jinal/Documents/Python training/Image Processing/OpenCV/Faces/train'
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# creating training set 
# this traing set will contain two lists features and labels 

# this function will loop over every folder in train and all the picture inside it.
# grab the image and it to traing set 
# traing set consist of two lists (features : which consist of array of the image faces)(labels : which consist of labels of corresponding faces)

features = []
labels = []
def creat_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
            for x,y,w,h in face_rect:
                face_region = gray[y:y+h, x:x+w]
                features.append(face_region)
                labels.append(label)

creat_train()

# for the training purpose ,convert the two lists into numpy array
features = np.array(features, dtype='object')
labels = np.array(labels)
# now use that features and labels to train our recognizer
# instantiating the face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer 
face_recognizer.train(features,labels)
print('training done!!!!!!!!')

# saving the trained model
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)


