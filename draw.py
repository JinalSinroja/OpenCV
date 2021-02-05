import cv2
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv2.imshow('blank', blank)

# putting color 
# blank[::] = 0,255,0
blank[200:300, 300:400] = 0,0,255
cv2.imshow('Green', blank)

# rectangle
cv2.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv2.FILLED)
cv2.imshow("rectanlge", blank)

# circle
cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv2.imshow("cicle", blank)

# line
cv2.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
cv2.imshow("Line",blank)

# text writting
cv2.putText(blank,'Hello! Here We Go!!!',(0,300),cv2.FONT_HERSHEY_PLAIN,2.0,(255,0,0),1)
cv2.imshow("Text",blank)

cv2.waitKey(0)