import cv2
from cv2 import VideoCapture
import numpy as np
cap=VideoCapture(0)
while True:
    ret,frame =cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) and 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
