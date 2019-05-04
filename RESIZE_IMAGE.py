import cv2
import numpy as np
img=cv2.imread("jp2.jpg")
cv2.imshow("Orignal Image",img)
cv2.waitKey(0)
scaled1=cv2.resize(img,None,fx=0.75,fy=0.75)
cv2.imshow("Resied Image",scaled1)
cv2.waitKey()
scaled2=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow(" cubic interplotation",scaled2)
cv2.waitKey()
scaled3=cv2.resize(img,(900,400),interpolation=cv2.INTER_AREA)
cv2.imshow("scaled Size",scaled3)
cv2.waitKey()
