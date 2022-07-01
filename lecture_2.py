'''
import cv2

cap = cv2.VideoCapture("C:\\Users\\ahadraza\\Downloads\\y2mate.com - Top Trending Pakistani Memes  Funniest Pakistani Memes  Pakistani Memes Compilation_1080p.mp4")

print("your video cap is:",cap)

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(700,450))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("gray scale image",gray)
    k = cv2.waitKey(25)
    if k==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
'''

#webcamera

import cv2
cap = cv2.VideoCapture(0)  #CAP_DSHOW
print(cap)
while cap.isOpened:
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(700,450))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
        cv2.imshow("gray",gray)
        k = cv2.waitKey(100)
    if k ==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
