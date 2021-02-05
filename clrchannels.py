# splitting and merging the color channels
import cv2 as cv
import numpy as np

img=cv.imread('Images/boston.jpg')
cv.imshow('boston',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

#spllit the image
b,g,r = cv.split(img)

cv.imshow("Blue",b)
cv.imshow("Red",r)
cv.imshow("Green",g)
# this results depicted as grayscale,that show the pixel distribution intencity
# regions where it's darker repesents that there is no pixels in that region 
# regions where it's lighter represents that there is more concentration of those pixel values

print(img.shape) # 3 means three color channels
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([r,g,b]) # bgr to rgb format 
cv.imshow('Merged',merged)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("Blue_blank",blue)
cv.imshow("red_blank",red)
cv.imshow("Green_blank",green)
cv.waitKey(0)