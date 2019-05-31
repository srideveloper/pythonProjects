import numpy
import cv2

###########For excute Run Through Shell#######
#### For that no need to write path to excute programe
#img = cv2.imread('colors.jpg',0)

###########For excute command prompt###########
img = cv2.imread('D:\Python\Img\colors.jpg',0)
img1 = cv2.imread('D:\Python\Img\colors.jpg',1)
#cv2.namedWindow('IMGAE',cv2.WINDOW_AUTOSIZE)
cv2.imshow('GrayImageWindow',img)
#cv2.imshow('ColorImageWindow',img1)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('D:\Python\Img\gray.png',img)
    cv2.destroyAllWindows()
#cv2.imwrite('D:\Python\Img\gray.png',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

