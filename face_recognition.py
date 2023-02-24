from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import VideoCapture
from time import strftime, time
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np


class face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognisation System")

        title_lbl= Label(self.root, text = "FACE RECOGNITION", font= ("Times New Roman",35, "bold"), bg="black",fg="white")
        title_lbl.place(x=0,y=0,width= 1330, height = 50)

        img_left = Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\face_recog1.jpg")
        img_left = img_left.resize((640,500),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(self.root,image=self.photoimg_left) 
        f_lbl.place(x=0,y=50,width=640,height=500)

        img_right = Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\face_recog2.jpg")
        img_right = img_right.resize((640,500),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(self.root,image=self.photoimg_right) 
        f_lbl.place(x=640,y=50,width=640,height=500)

        end_lbl= Label(self.root, text = "", font= ("Times New Roman",35, "bold"), bg="dark blue",fg="white")
        end_lbl.place(x=0,y=550,width= 1330, height = 100)

        #button1
        b1_1 = Button(self.root,text="SCAN FACE", cursor="hand2",command= self.face_recog,font=("times new roman",20, "bold"),bg ="white",fg ="black")
        b1_1.place(x=160,y=570,width=300,height=50)

        #====================Attendance=====================
    def mark_attendance(self,i,r,n,d):
        with open("C:\\Users\\kadal\\Desktop\\Project\\Face_Recognisation_System\\akash.csv","r+",newline="\n") as f:
            myDataList= f.readlines()
            name_list =[]
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list)):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

        #==================Face Recognition=================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color, text, clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features= classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict((gray_image[y:y+h,x:x+w]))
                confidence = int(100*(1-predict/300))

                conn = mysql.connector.connect(host= "127.0.0.1",port="3307",username = "root",password= "Nirvignaa@2002", database = "face_recognize")
                my_cursor = conn.cursor()

                my_cursor.execute("select StudentName from student_final where Student_id = "+str(id))
                n = my_cursor.fetchone()
                #n = str(n)
                #n = "".join(n)
                
                my_cursor.execute("select Roll from student_final where Student_id = "+str(id))
                r = my_cursor.fetchone() 
                #r = str(r)
                #r = "".join(r) 
              
                my_cursor.execute("select Dep from student_final where Student_id = "+str(id))
                d = my_cursor.fetchone()
                #d = str(d)
                #d = "".join(d)
            

                my_cursor.execute("select Student_id from student_final where Student_id =" + str(id))
                i = my_cursor.fetchone()
                #i = str(i)
                #i = "".join(i)
                

                if confidence>77:
                    cv2.putText(img,f"ID: {i}",(x,y-80),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),3)
                    cv2.putText(img,f"Name: {n}",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),3)
                    cv2.putText(img,f"Roll: {r}",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),3)
                    cv2.putText(img,f"Department: {d}",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),3)
                    self.mark_attendance(i,n,r,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,25,255),2)

                coord = [x,y,w,h]

            return coord

        import cv2

        def recognize(img, clf, faceCascade):
            img, coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("C:\\Users\\kadal\\Desktop\\Project\\Face_Recognisation_System\\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("C:\\Users\\kadal\\Desktop\\Project\\Face_Recognisation_System\\classifier.xml")

        video_cap =cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognization", img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = face_Recognition(root)
    root.mainloop() 