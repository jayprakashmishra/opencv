import cv2
import numpy as np
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
for j in range(1,10):
    out=cv2.VideoWriter("out12.jpg",fourcc,50.0,(640,480))
while(cap.isOpened()):
    ret, frame=cap.read()
    if ret==True:
        for i in range(1,100):
            out.write(frame)
            cv2.imshow("frame",frame)
        if cv2.waitKey(1)&0xFF==ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
