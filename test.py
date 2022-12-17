import cv2 as cv

# Reading image data
# img = cv.imread('Photo/1103339.jpg')

# cv.imshow('Test', img)
capture = cv.VideoCapture('Photo/Shopping.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Test', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

