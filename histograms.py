# to visualize the pixel distribution intensity by using histograms

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Images/boston.jpg')
cv.imshow('boston',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

mask=cv.circle(blank.copy(), (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked image',masked)

#Grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
# gray_hist = cv.calcHist([gray], [0],masked, [256], [0,256])  Using masked image
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# Colour Histogram for the three color channels
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], masked, [256], [0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)