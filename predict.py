import cv2
import pymysql

face_cascade = cv2.CascadeClassifier('C:\\Users\\DIPESH KUMAR\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
#face_cascade.load('haarcascade_frontalface_default.xml')
#eye_cascade.load('harrcascade_eye.xml')
ID=5
print(face_cascade.empty())


def detect(gray, frame):
   faces = face_cascade.detectMultiScale(gray, 1.3, 5)
   for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        ID,conf=rec.predict(gray[y:y+h,x:x+w])
        print(ID)
        cv2.putText(frame,"NAME : "+str(ID)+"  "+names[ID],(25,470), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 3)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
   return frame       

video_capture=cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read("G://project skill LAB//recognizer//trainer.yml")
#font=cv2.cv.InitFont(cv2.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
fontface=cv2.FONT_HERSHEY_SIMPLEX
names=["","Dipesh","Subha","Saswat","Gaurav"]
while True:
    ret,frame=video_capture.read()
    print(ret)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas=detect(gray,frame)
    print(frame)
    #cv2.putText(frame,"ABCD",(25,470), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 3)
    cv2.imshow('Video',canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
video_capture.release()
cv2.destroyAllWindows()

