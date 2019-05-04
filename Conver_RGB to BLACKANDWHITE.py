import cv2
img=cv2.imread("jp.jpg")
cv2.imshow("output",img)
cv2.waitKey(0)
ret, bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("bainary",bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
