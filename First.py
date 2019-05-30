import numpy as np
import cv2
import matplotlib


img = cv2.imread('Love.jpg',0)
img1 = cv2.imread('gray.png')

#gray = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
#gray1 = cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR)

cv2.imshow('image' , img)
#cv2.imshow('image1' , gray)
#cv2.imwrite('gray.png',gray)
cv2.waitKey(0)
cv2.destroyWindow('image')

