import pafy
import cv2
url = "https://www.youtube.com/watch?v=SLD9xzJ4oeU"
data = pafy.new(url)
data = data.getbest(preftype="mp4")
cap = cv2.VideoCapture()
cap.open(data.url)
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
output = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480), 0)
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # here flip is used to lip the video at recording time
        # frame = cv2.flip(frame,0)
        # output.write(gray)

        # cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # press to exit
            break
    else:
        break
# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()
# if any os error regarding youtube-dl occur thn
# conda install -c forge youtube-dl
# pip3 install youtube-dl

