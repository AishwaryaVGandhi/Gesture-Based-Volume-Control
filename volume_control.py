import cv2
import numpy as np
import time
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam = 640
hCam = 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector(detectionCon=0.85)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        #img, co-ordinates, radius, color, filled
        cv2.circle(img, (x1, y1), 10, (90, 23, 51), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (90, 23, 51), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (90, 23, 51), 3)
        cv2.circle(img, (cx, cy), 10, (90, 23, 51), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)

        # Hand Range: 50 - 300
        # Volume Range: -65 - 0

        #np.interp(the value to be converted, our range, conversion range)
        volBar = np.interp(length, [50, 300], [400, 150]) # Length of Volume Bar
        print(int(length), vol)

        volPer = np.interp(length, [50, 300], [0, 1])  # Normalize to 0-1
        volume.SetMasterVolumeLevelScalar(volPer, None)  # Set linear volume
        vol = volume.GetMasterVolumeLevelScalar() * 100  # Get actual volume percentage

    cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 255), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 255, 255), cv2.FILLED)
    cv2.putText(img, f"{int(vol)} %", (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    #img, text, co-ordinates, font, scale, color, thickness
    cv2.putText(img, f"FPS: {int(fps)}", (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, ((0, 255, 0)), 2)

    cv2.imshow("image", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
