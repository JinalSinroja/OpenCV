import cv2

img = cv2.imread('Images/CAT1.jpg')

def rescaleFrames(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
    return cv2.resize(frame, dimensions,interpolation=cv2.INTER_AREA)


resized_frame = rescaleFrames(img,scale = 0.2)
cv2.imshow('Cat1', img)
cv2.imshow('Cat', resized_frame)

cv2.waitKey(0)

# reading and rescaling videos
capture = cv2.VideoCapture('Videos/Dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv2.imshow('dogVideo', frame)

    resized_video = rescaleFrames(frame,scale=0.2)
    cv2.imshow('resizedvideo', resized_video)
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()