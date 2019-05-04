import cv2
import numpy as np
img=cv2.imread("jp.jpg")
cv2.imshow("Original Image",img)
cv2.waitKey(0)
height,width=cv2.split(img)
#height,width=np.zeros(img.shape[:2],dtype="uint8")
rotate=cv2.getRotationMatrix20((width/2,height/2))
rotateimg=cv2.warpAffline(img,rotate,(width,height))
cv2.imshow("Rotate Image",rotateimg)
cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.DestroyAllWindows()
