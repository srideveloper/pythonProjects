import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg


img = cv2.imread('colors.jpg',1)
#plt.imshow(img)#, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])
#plt.axis('off')
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()
cv2.waitKey(0)
