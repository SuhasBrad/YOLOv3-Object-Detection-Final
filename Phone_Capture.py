import cv2 as cv


url = "https://192.168.43.1:8080/video"
capture = cv.VideoCapture(url)


def rescaleFrame(frames, scale=0.75):
    width = int(frames.shape[1] * scale)
    height = int(frames.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frames, dimensions, interpolation=cv.INTER_AREA)


while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.5)
    cv.imshow('Camera', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
