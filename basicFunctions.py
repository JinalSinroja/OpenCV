import cv2

img = cv2.imread('Images/boston.jpg')
cv2.imshow('Boston', img)

# grayscale
Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',Gray)

# blur
blur=cv2.GaussianBlur(img,(7,7),cv2.BORDER_DEFAULT)
cv2.imshow('Blur',blur)

#Edge cascading
canny=cv2.Canny(blur,125,175)
cv2.imshow('Canny Edges',canny)

#Dilation of image
dilated = cv2.dilate(canny,(7,7),iterations=3)
cv2.imshow('Dilated',dilated)

#Eroding
eroded=cv2.erode(dilated,(7,7),iterations=3)
cv2.imshow('Eroded',eroded)

#Cropping
cropped = img[50:200,200:400]
cv2.imshow('Cropped',cropped)
cv2.waitKey(0)