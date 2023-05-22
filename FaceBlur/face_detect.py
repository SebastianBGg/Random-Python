import cv2
import sys
import os

path = os.listdir(os.path.abspath(os.getcwd()))
imagePath = os.listdir(path[0])
cascPath = path[3]
one = os.path.abspath(path[0])


for x in imagePath:
    pic = os.path.join(one, x)
    print(pic)
    faceCascade = cv2.CascadeClassifier(cascPath)
    

    image = cv2.imread(pic)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    for (x, y, w, h) in faces:
        ROI = image[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(ROI, (51,51), 0) 
        image[y:y+h, x:x+w] = blur
    cv2.imshow("Faces found", image)
    cv2.waitKey(0)
