import numpy as np
import cv2

cap = cv2.VideoCapture('output.avi')

def srikanth(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame

while(True):

    ret, frame = cap.read()
    frame = srikanth(frame)    

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
cap.release()
cv2.destroyAllWindows()
