import cv2 as cv
url = "https://192.168.43.1:8080/video"
# Capturing the video stream
capture = cv.VideoCapture(url)


# Rescaling the video stream
def rescaleFrame(frames, scale=0.75):
    width = int(frames.shape[1] * scale)  # width of the video
    height = int(frames.shape[0] * scale)  # height of the video
    dimensions = (width, height)  # dimensions of the video
    return cv.resize(frames, dimensions, interpolation=cv.INTER_AREA)
    # output of the resized video frames

# Capturing the frames and scaling them
while True:
    isTrue, frame = capture.read()  # read the frame
    frame_resized = rescaleFrame(frame,scale=0.25)  # function to rescale the frame

    cv.imshow('Test', frame)
    cv.imshow('Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
