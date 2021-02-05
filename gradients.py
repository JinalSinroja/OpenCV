# Edge Detection
# Methods to detect the edges: laplacian, sobel, canny
import cv2 as cv
import numpy as np

img = cv.imread('Images/boston.jpg')
cv.imshow('boston',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Laplacian Edges
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian Edges',lap)

#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # X-axis specific
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) # Y-axis specific
combined_sobel=cv.bitwise_or(sobelx,sobely) # combination
cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('Combine sobel',combined_sobel)

# Canny method
canny=cv.Canny(gray, 150, 175)
cv.imshow('Canny',canny)

cv.waitKey(0)