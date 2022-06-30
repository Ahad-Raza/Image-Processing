import cv2

img  = cv2.imread("C:\\Users\\ahadraza\\Desktop\\Capture.png",0)
img = cv2.resize(img,(700,700))
cv2.imshow("Window 1",img)

img1  = cv2.imread("C:\\Users\\ahadraza\\Desktop\\Capture.png",1)
img1= cv2.resize(img1,(700,700))
cv2.imshow("Window 2",img1)

img2  = cv2.imread("C:\\Users\\ahadraza\\Desktop\\Capture.png",-1)
img2 = cv2.resize(img2,(700,700))
cv2.imshow("Window 3",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()