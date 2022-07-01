import cv2
#camera = "ip address of your webcame"
cap = cv2.VideoCapture(0)
#cap.open(camera)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)
print(cap)
while cap.isOpened:
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(700,450))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame = cv2.flip(frame,0)
        cv2.imshow("frame",frame)
        cv2.imshow("gray",gray)
        output.write(frame)
        k = cv2.waitKey(100)
    if k ==ord("q"):
        break
cap.release()
output.release()
cv2.destroyAllWindows()
