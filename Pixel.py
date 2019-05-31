import numpy as np
import cv2

img = cv2.imread('Recogniser.png',1)

#px = img[231,357]
#px = img[559,1439]
#print (px)
#blue = img[100,100,0]
#img[600,600] = [20,201,11]
#print (img[600,600])
#print (px)
#print (blue)
#print(px)
cv2.imshow('pixel',img)
#cv2.waitKey(0)

'''print ('original values')

red = img[231,357,2]
print (px)
print ('red values',red)

print ('before changing the values to the red one')

img.item(231,357,2)
print (img.item(231,357,2))

print ('after changing the values to the red one')

img.itemset((231,357,2),50)
print (img.item(231,357,2))'''

#print (img.shape)
#print (img.size)
#print (img.dtype)
'''
ball = img[280:340, 330:390]
img[273:333, 100:160] =ball

cv2.imshow(img)'''
b,g,r = cv2.split(img)
print (b)
print ("'''''''''''''''''''''''''''''''''''''''''")
print (g)
print ("'''''''''''''''''''''''''''''''''''''''''")
print (r)


img = cv2.merge((b,g,r))
print (img)

img[:,:,2] = 0

print (img)

            
