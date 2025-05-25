import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

folderPath = "Header"
myList = os.listdir(folderPath)
# print(myList)

overLayList= []

for file in myList:
  img = cv2.imread(f"{folderPath}/{file}")
  overLayList.append(img)

# print(len(overLayList))
header = overLayList[0]

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = htm.handDetector(detectionCon=0.85)


while True:
  # 1. Importing the Image
  success, img = cap.read()
  img = cv2.flip(img,1)

  # 2. Finding hand landmarks
  img = detector.FindHands(img)
  lmList = detector.findPosition(img, draw=False)

  if(len(lmList)!=0):
    print(lmList)

  # 3. Checking which Finger is up

  # 4. Selection Mode : if two fingers up
  # 5. Draw Mode : if one finger is up

  img[0:124, 0:1280] = header
  cv2.imshow("image",img)

  if cv2.waitKey(1) & 0xFF==ord('x'):
    break

