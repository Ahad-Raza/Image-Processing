import cv2

path = input("Enter the Path and name of an image===")

print("You Enter this=",path)

img1 = cv2.imread(path, 0)  # convert image into grayscale

img1 = cv2.resize(img1, (560, 700))
#img1 = cv2.flip(img1, 0)  # it accept 3 parameters 0,-1,1

cv2.imshow("converted image==", img1)

k = cv2.waitKey(0) & 0xFF

if k == ord("q"):

    cv2.destroyAllWindows()

elif k == ord("s"):

    cv2.imwrite("C:\\Users\\ahadraza\\Desktop\\weather.png", img1)

    cv2.destroyAllWindows()


























