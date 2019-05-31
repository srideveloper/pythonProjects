'''import numpy
import cv2


cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')

out = cv2.VideoWriter('output.avi',fourcc, 20.0,(640,480)) # no of frames per second and frame size

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,1)
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break

cap.release()
out.release()
#cv2.destroyAllWindows()'''
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')

out = cv2.VideoWriter('Recod.avi',fourcc,30.0,(640,480))

while(True):

    ret, frame = cap.read()
    
    out.write(frame)
    cv2.imshow('RecordWindow', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

cap.release()
out.release()
cv2.destroyAllWindows()
