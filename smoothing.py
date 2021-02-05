import cv2 as cv

img=cv.imread('Images/cat5.jpg')
cv.imshow('Cat',img)

#Averaging
average = cv.blur(img, (7,7))
# (7,7) represents the kernel size which means assume it as 7x7matrix
# and the center value of that matrix will be avarage of all pixels around it
cv.imshow('Average Blur',average)

#Gaussian Blur
# this type of blur gives the natural blur image
# it works same as averager but instead of using surrounging pixel intensity it uses the product of weights that are given to each pixels
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur',gauss)

#Median Blur
# same as averager but it uses median instead of average
# it is not used for large kernel size
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur',median)

#Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)