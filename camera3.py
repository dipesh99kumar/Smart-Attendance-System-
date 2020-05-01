import cv2
import os

#Loading the xml file hactic step
face_cascade = cv2.CascadeClassifier('C:\\Users\\DIPESH KUMAR\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')


def Create_User():
    global face_id
    count=0
    video_capture=cv2.VideoCapture(0)
    while(True):
        ret,frame=video_capture.read()
        print(frame)
        #convert frame to grayscale
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.3,5)
        #drawing a box around the face
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            count+=1
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('frame',frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        elif (count>30):
            break
    
    video_capture.release()
    cv2.destroyAllWindows()
    face_id+=1
    return 
    

face_id=1
c=input("Wnat to Create a new USER \n")
if (c=='y'):
    Create_User()
c=input("Wnat to Create a new USER \n")
if (c=='y'):
    Create_User()
    

    