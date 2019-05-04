import cv2
import numpy as np
img=cv2.imread("jp.jpg")
cv2.imshow("orignal",img)
cv2.waitKey(0)
b,g,r=cv2.split(img)
zeros=np.zeros(img.shape[:2],dtype="uint8")
cv2.imshow("Red",cv2.merge([zeros,zeros,r]))
cv2.waitKey(0)
cv2.imshow("Green",cv2.merge([zeros,g,zeros]))
cv2.waitKey(0)
cv2.imshow("Blue",cv2.merge([b,zeros,zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()
