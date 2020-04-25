import sys
import dlib
#from skimage import io
import cv2 as cv

# Take the image file name from the command line
file_name = sys.argv[1]

# Create a HOG face detector using the built-in dlib class
face_detector = dlib.get_frontal_face_detector()

#win = dlib.image_window()

# Load the image into an array
img = cv.imread(file_name)
image = img
#resize image to scale of 640 width or smaller
if img.shape[1] > 640 and img.shape[1] >= img.shape[0]:
    perc=1080/img.shape[1]
    image = cv.resize(img,(int(img.shape[1]*perc),int(img.shape[0]*perc)),interpolation = cv.INTER_AREA)

# Run the HOG face detector on the image data.
# The result will be the bounding boxes of the faces in our image.
detected_faces = face_detector(image, 1)
if len(detected_faces)== 0:
    print("No faces in this photo")
    sys.exit()
print("I found {} faces in the file {}".format(len(detected_faces), file_name))

# Open a window on the desktop showing the image
#win.set_image(image)

#img = cv.imread(file_name)
# Loop through each face we found in the image
for i, face_rect in enumerate(detected_faces):
    # Detected faces are returned as an object with the coordinates 
    # # of the top, left, right and bottom edges
    print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))
    start = (face_rect.left(),face_rect.top())
    end = (face_rect.right(),face_rect.bottom())
    bColor= (0,190,0)
    #print("Start{} End{} Color{}".format(start, end, bColor))
    image = cv.rectangle(image,start,end,bColor,1)
#cv.imshow("Faces", image)
file_name.replace(".jpg", "")
cv.imwrite(file_name + 'face-detect.jpg',image)
#cv.waitKey(8000)
#cv.destroyAllWindows()
# Draw a box around each face we found
#win.add_overlay(face_rect)
	        
# Wait until the user hits <enter> to close the window	        
#dlib.hit_enter_to_continue()