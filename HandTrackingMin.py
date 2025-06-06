import cv2
import numpy as np
import mediapipe as mp
import time

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw= mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
pTime =0

while True:
  success, img = cap.read()
  imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
  results = hands.process(imgRGB)
  # print(results.multi_hand_landmarks)

  if results.multi_hand_landmarks:
    for handLms in results.multi_hand_landmarks:
      for id, lm in enumerate(handLms.landmark):
        # print(id,lm)
        h,w,c = img.shape
        cx,cy = int(lm.x*w), int (lm.y*h)
        # print(id,cx,cy)
        if id==8:
          cv2.circle(img,(cx,cy),20, (255,255,0), -1, cv2.FILLED)

      mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

  cTime = time.time()
  fps = 1/(cTime-pTime)
  pTime = cTime
  
  cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3,(255,255,0), 2)

  cv2.imshow("Image", img)
  if cv2.waitKey(1) & 0xFF==ord('x'):
    break
