import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

folderPath = "Header"
myList = os.listdir(folderPath)
# print(myList)

overLayList= []
colourList = (255,0,255)
brushThickness = 25
eraserThickness = 75
xp,yp =0,0

for file in myList:
  img = cv2.imread(f"{folderPath}/{file}")
  overLayList.append(img)

# print(len(overLayList))
header = overLayList[0]

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = htm.handDetector(detectionCon=0.85)
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
  # 1. Importing the Image
  success, img = cap.read()
  img = cv2.flip(img,1)

  # 2. Finding hand landmarks
  img = detector.FindHands(img)
  lmList = detector.findPosition(img, draw=False)

  if(len(lmList)!=0):
    # print(lmList)

    x1,y1 = lmList[8][1:]
    x2,y2 = lmList[12][1:]
    
    # 3. Checking which Finger is up
    fingers = detector.fingersUp()
    # print(fingers)

    # 4. Selection Mode : if two fingers up
    if fingers[1] and fingers[2]:
      # print("Selection Mode")
      if(y1<124):
        if 250<x1<450:
          header = overLayList[0]
          colourList = (255, 0 ,255)
        elif 500<x1<750:
          header = overLayList[1]
          colourList = (255, 0 ,0)
        elif 800<x1<900:
          header = overLayList[2]
          colourList = (0, 255 ,0)
        elif 1050<x1<1200:
          header = overLayList[3]
          colourList = (0, 0 ,0)
      cv2.rectangle(img, (x1,y1-25), (x2,y2+25), colourList, cv2.FILLED)


    # 5. Draw Mode : if one finger is up
    if fingers[1]==True and fingers[2]==False:
      xp,yp =0,0
      cv2.circle(img, (x1,y1), 20, colourList, -1)
      # print("Drawing Mode")
      if xp==0 and yp==0:
        xp,yp = x1,y1

      if colourList == (0,0,0):  
        cv2.line(img, (xp,yp), (x1,y1), colourList, eraserThickness)
        cv2.line(imgCanvas, (xp,yp), (x1,y1), colourList, eraserThickness)

      else:
        cv2.line(img, (xp,yp), (x1,y1), colourList, brushThickness)
        cv2.line(imgCanvas, (xp,yp), (x1,y1), colourList, brushThickness)
      xp,yp = x1,y1

  imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
  _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
  imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
  img = cv2.bitwise_and(img, imgInv)
  img = cv2.bitwise_or(img, imgCanvas)


  img[0:124, 0:1280] = header
  cv2.imshow("image",img)
  # cv2.imshow("Canvas",imgCanvas)

  if cv2.waitKey(1) & 0xFF==ord('x'):
    break