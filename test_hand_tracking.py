import cv2
import numpy as np
import mediapipe as mp
import time
import HandTrackingModule as htm

  
cap = cv2.VideoCapture(0)
pTime =0
cTime =0
detector = htm.handDetector()

while True:
  success, img = cap.read()
  img = detector.FindHands(img, draw=False)
  lmList = detector.findPosition(img, draw=False)
  if(len(lmList) !=0):
    print(lmList[8])
  cTime = time.time()
  fps = 1/(cTime-pTime)
  pTime = cTime
  
  cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3,(255,255,0), 2)
  cv2.imshow("Image", img)
  if cv2.waitKey(1) & 0xFF==ord('x'):
    break

