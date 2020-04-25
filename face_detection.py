import sys
import dlib
import cv2 as cv

## Libraries to download in requirements.txt
'''
dlib
opencv-python
'''
## Prepare HOG face detector
face_detector = dlib.get_frontal_face_detector()

## First get video streams up and running
vid = cv.VideoCapture(0)

## get the frame and the faces from the frame
while True:
    ret, frame = vid.read()
    faces = face_detector(frame, 1)
    
    ## 1 If there are faces show the boundary boxes over the face
    if len(faces) > 0:
        # Display total number of captured faces
        total = "Total {}".format(len(faces))
        font = cv.FONT_HERSHEY_PLAIN
        color = (255,192,203)
        frame = cv.putText(frame,total,(50,50),font,1,color,2)
        for face in faces:
            start = (face.left(),face.top())
            end = (face.right(),face.bottom())
            frame = cv.rectangle(frame, start,end,color,2)
    #cv.windowResize
    cv.imshow("Face Detection",frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

#Gently exit
vid.release()
cv.destroyAllWindows()