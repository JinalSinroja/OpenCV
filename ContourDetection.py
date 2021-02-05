import cv2 as cv
import numpy as np

img = cv.imread('Images/dog1.jpg')
cv.imshow('Dog',img)

blank = np.zeros(img.shape, dtype='uint8') 
cv.imshow('Blank',blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny',canny)

# thresholding means to binerise an image if any pixel is below 125 it sets that to 0 means black and for the above 125 it sets it to 255(white)
ret , thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Tresh',thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours\' found!')
# RETR_LIST = returns all the contours it finds on an image
# RETR_EXTERNAL = returns all the external contours
# RETR_TREE = all the contours that are hierarchical it returns that
# cv.CHAIN_APPROX_SIMPLE(how we want to approximate our contours)=compresses all the contour that are returned
# cv.CHAIN_APPROX_NONE = does nothing it returns all of the contours
# for example if we have one line NONE will return all the contours(coordinates) of that line and SIMPLE will compress all that into two end points


cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)
# compare thus result to the canny image it will look same

cv.waitKey(0)