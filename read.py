import cv2

# reading images
img = cv2.imread('Images/dog2.jfif')

cv2.imshow('Cat', img)

# reading videos

capture = cv2.VideoCapture('Videos/Dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv2.imshow('dogVideo', frame)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()