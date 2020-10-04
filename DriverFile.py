# import the necessary packages
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
import argparse
import imutils
import dlib
import cv2
import os
from datetime import datetime




# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True, help="path to facial landmark predictor")
#   ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-d","--directoryPath", required=True, help="path to directory with pictures")
ap.add_argument("-f","--directoryFinal", required=True, help="path to directory where processed images will be stored")
args = vars(ap.parse_args())


# initialize dlib's face detector (HOG-based) and then create the facial landmark predictor and the face aligner
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])
faceAligner = FaceAligner(predictor, desiredFaceWidth=256)


directory = args["directoryPath"]
final_directory = args["directoryFinal"]

# create new directory inside main directory in which the processed images will be saved
# To make sure there are no duplicate names, I will use date and time as name
#now = datetime.now()
#path = now.strftime("%d%m%Y%H%M%S")
# double check that there is no directory already with the same name
#os.makedirs(os.path.join(final_directory, path))

counter = 0

# extract the names of the pictures one by one to be parsed
for picture in os.listdir(directory):
    image = cv2.imread(os.path.join(directory, picture))
    #cv2.waitKey(0)
    image = imutils.resize(image, width=800)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Input", image)
    # detect faces in the grayscale image
    rects = detector(gray, 2)

    # loop over the face detections
    for rect in rects:
        # extract the ROI of the *original* face, then align the face using facial landmarks
        (x, y, w, h) = rect_to_bb(rect)
        #faceOrig = imutils.resize(image[y:y + h, x:x + w], width=256)
        faceAligned = faceAligner.align(image, gray, rect)
        # display the output images
        #cv2.imshow("Original", faceOrig)
        cv2.imshow("Output", faceAligned)
        cv2.waitKey(10)
    counter = counter + 1
    print(counter)
    #final_destination = os.path.join(final_directory, path) )
    #print(final_destination)
    cv2.imwrite(str(final_directory) + "\ProcessedPic{}.jpg".format(str(counter)), faceAligned)