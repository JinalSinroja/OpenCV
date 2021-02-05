# masking is used to focus on the particular region of an image
import cv2 as cv
import numpy as np

img = cv.imread('Images/boston.jpg')
cv.imshow('boston',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

# masking image by the circle kind of area
mask=cv.circle(blank.copy(), (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask',mask)

masked = cv.bitwise_and(img,img,mask=mask) # this will give us the circle(size of mask) portion of the image 
cv.imshow('Masked image',masked)

# # masking image by the rectangle area
mask2=cv.rectangle(blank.copy(), (30,30), (370,370),  255, -1)
cv.imshow('Mask_rect',mask)

masked2 = cv.bitwise_and(img,img,mask=mask2)
cv.imshow('Masked image 2',masked2)

# Masking image by Weird Shape
weird_shape = cv.bitwise_and(mask, mask2)
cv.imshow('Weird Shape',weird_shape)

masked3 = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shape Masked Image',masked3)

cv.waitKey(0)