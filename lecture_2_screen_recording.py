import cv2

import pyautogui as p

import numpy as np

rs = p.size()

fn = input("enter your file name and path:")

fps = 60.0

fourcc = cv2.VideoWriter_fourcc(*"XVID") # format thk karnai hou ghai

output = cv2.VideoWriter(fn,fourcc,fps,rs)

cv2.namedWindow("CODE WITH AHAD",cv2.WINDOW_NORMAL)

cv2.resizeWindow("CODE WITH AHAD",(600,400))

while True:

    img = p.screenshot()

    f = np.array(img)

    f = cv2.cvtColor(f,cv2.COLOR_BGR2RGB)

    output.write(f)

    cv2.imshow("LIVE RECORDING",f)

    k = cv2.waitKey(1)
    if k==ord("a"):
        break
output.release()
cv2.destroyAllWindows()


