'''
this code is not working, i coudn't understand the meaning of this lesson as 
it will be explained later as mentioned in the documentations.
'''

import numpy as np
import cv2

im = cv2.imread('test.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(image, contours, 3, (0,255,0), 3)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




