import cv2 as cv
import numpy as np

img = cv.imread('Images/boston.jpg')

cv.imshow('boston',img)

#translation
def translate(img, x , y):
    transMat= np.float32([[1,0,x],[0,1,y]])
    dimensions= (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

#-x--> left
#-y--> up
#x--> right
#y--> down

translated = translate(img, -100, -100)
cv.imshow('Translated',translated)


#Rotation    
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:  # to rotate around the center if rotation point is none
        rotPoint = (width//2, height//2)    
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)      # -x means it will rotate clockwise ,if +x then it will rotate anticlockwise
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, 45) # if we try to rotate the rotated image,then the black space of that rotated image will also be rotated along with it
cv.imshow('Rotated rotated',rotated_rotated)

#Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Flipping
flip = cv.flip(img, -1)
# flip code
# 0 Flipping img vertically on X axis
# 1 Flipping img horizontally on Y axis
# -1 Flipping img both vertically and horizontally
cv.imshow('Flip',flip)

cv.waitKey(0)