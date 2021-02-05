# To convert the image into binary image
import cv2 as cv
import numpy as np

img = cv.imread('Images/dog1.jpg')
cv.imshow('Dog',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

## Simple Thresholding
threshold,thresh = cv.threshold(gray, 150 ,255, cv.THRESH_BINARY) # for above 150 it's 255 and for below it's 0
cv.imshow('Simple Thresholded',thresh)
# Inverse Thresholding (as the name implies), it can be done by using cv.TRESH_BINARY_INV


## Adaptive Thresholding (Let the computer find the optimal threshold value)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
# MEAN_C means finding mean value of the neighbourhood pixels and subtracted by c where mean value is gotten from the kernal matrix (11 is the kernal size)
cv.imshow('Adaptive Thresholded',adaptive_thresh)
# GUASSIAN_C is also used in that case, weights are added and then it finds mean(and then as similar to the MEAN_C)
cv.waitKey(0)