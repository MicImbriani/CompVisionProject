# Daily Picture Stabilisation

Computer Vision based software created for automising the stabilisation of my own face pictures, with the aim of creating a final slideshow of them.

![PicAday](https://user-images.githubusercontent.com/67190150/115866828-2a4de480-a432-11eb-84a1-afb8c9b46939.png)

Inspired by the idea of this video (One Picture Every Day):
https://www.youtube.com/watch?v=65nfbW-27ps


To apply the program on your own set of pictures, follow these steps:
1) Delete all the current pictures in "Input" and "Output" folder.
2) Insert the input pictures in the "Input" folder
3) In the terminal, navigate to the folder 
4) type "python DriverFile.py -p "shape_predictor_68_face_landmarks.dat" -d "Input"  -f "Output"
5) The processed images should appear in the "Output" folder



# Dependencies needed:
1) dlib
2) cv2
3) os
4) datetime
5) argparse
6) numpy
7) imutils (folder provided with download)



# The Computer Vision model has been developed by PhD Adrian Rosebrock with Caffe DL framework.
