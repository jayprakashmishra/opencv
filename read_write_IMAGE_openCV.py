import cv2
img=cv2.imread("hi.jpg")
cv2.imshow("output",img)
cv2.imwrite("photoclocction.jpg",img)
cv2.imwrite("collectedpothos.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
