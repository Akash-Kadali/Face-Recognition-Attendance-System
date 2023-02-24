from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import face_Recognition
from tkinter import messagebox
import cv2
import numpy as np
from attendance import Attendance
from developer import Developer

class Face_Recognization_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognisation System")
#first image
        img= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\background.jpg")
        img = img.resize((130,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=130,height=130)

#second image
        img2= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\background.jpg")
        img2 = img2.resize((130,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=130,y=0,width=130,height=130)

#third image
        img3= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\background.jpg")
        img3 = img3.resize((130,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=260,y=0,width=130,height=130)

#fourth image
        img4= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\background.jpg")
        img4 = img4.resize((130,130),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        f_lbl = Label(self.root,image=self.photoimg4)
        f_lbl.place(x=390,y=0,width=130,height=130)

#fifth image
        img5= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\background.jpg")
        img5 = img5.resize((130,130),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        f_lbl = Label(self.root,image=self.photoimg5)
        f_lbl.place(x=520,y=0,width=130,height=130)

#sixth image
        img6= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\background.jpg")
        img6 = img6.resize((130,130),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        f_lbl = Label(self.root,image=self.photoimg6)
        f_lbl.place(x=650,y=0,width=130,height=130)

#seventh image
        img7= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\background.jpg")
        img7 = img7.resize((130,130),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        f_lbl = Label(self.root,image=self.photoimg7)
        f_lbl.place(x=780,y=0,width=130,height=130)

#eighth image
        img8= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\background.jpg")
        img8 = img8.resize((130,130),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        f_lbl = Label(self.root,image=self.photoimg8)
        f_lbl.place(x=910,y=0,width=130,height=130)

#ninth image
        img9= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\background.jpg")
        img9 = img9.resize((130,130),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        f_lbl = Label(self.root,image=self.photoimg9)
        f_lbl.place(x=1040,y=0,width=130,height=130)

#tenth image
        img10= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\background.jpg")
        img10 = img10.resize((130,130),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        f_lbl = Label(self.root,image=self.photoimg10)
        f_lbl.place(x=1170,y=0,width=130,height=130)

#Background image
        img11= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\big.jpg")
        img11 = img11.resize((1530,710),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        bg_img = Label(self.root,image=self.photoimg11)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl= Label(bg_img, text = "FACIAL RECOGNIZATION ATTENDANCE", font= ("Times New Roman",35, "bold"), bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width= 1330, height = 50)

#Student Button
        img12= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\std_info.jpg")
        img12 = img12.resize((170,170),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1 = Button(bg_img,image=self.photoimg12,command=self.student_details,cursor="hand2")
        b1.place(x = 150, y = 100,width= 170,height=170)

        b1_1 = Button(bg_img,text= "Student Details",command=self.student_details,cursor="hand2",font= ("Times New Roman",15, "bold"), bg="dark blue",fg="white")
        b1_1.place(x = 150, y = 240,width= 170,height=40)
        
#Detect Face Button
        img13= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\face_detect.jpg")
        img13 = img13.resize((170,170),Image.ANTIALIAS)
        self.photoimg13=ImageTk.PhotoImage(img13)

        b1 = Button(bg_img,image=self.photoimg13,cursor="hand2",command = self.face_data)
        b1.place(x = 400, y = 100,width= 170,height=170)

        b1_1 = Button(bg_img,text= "Face Detector",cursor="hand2",command = self.face_data,font= ("Times New Roman",15, "bold"), bg="dark blue",fg="white")
        b1_1.place(x = 400, y = 240,width= 170,height=40)

#Attendance Button
        img14= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\attend.jpg")
        img14 = img14.resize((170,170),Image.ANTIALIAS)
        self.photoimg14=ImageTk.PhotoImage(img14)

        b1 = Button(bg_img,image=self.photoimg14,cursor="hand2",command=self.attendance_data)
        b1.place(x = 650, y = 100,width= 170,height=170)

        b1_1 = Button(bg_img,text= "Attendance",cursor="hand2",command= self.attendance_data,font= ("Times New Roman",15, "bold"), bg="dark blue",fg="white")
        b1_1.place(x = 650, y = 240,width= 170,height=40)

#Helpdesk Button
        img15= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\help.jpg")
        img15 = img15.resize((170,170),Image.ANTIALIAS)
        self.photoimg15=ImageTk.PhotoImage(img15)

        b1 = Button(bg_img,image=self.photoimg15,cursor="hand2")
        b1.place(x = 900, y = 100,width= 170,height=170)

        b1_1 = Button(bg_img,text= "Helpdesk",cursor="hand2",font= ("Times New Roman",15, "bold"), bg="dark blue",fg="white")
        b1_1.place(x = 900, y = 240,width= 170,height=40)

#Training Data Button
        img16= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\train.jpg")
        img16 = img16.resize((170,170),Image.ANTIALIAS)
        self.photoimg16=ImageTk.PhotoImage(img16)

        b1 = Button(bg_img,image=self.photoimg16,cursor="hand2",command=self.train_classifier)
        b1.place(x = 150, y = 300,width= 170,height=170)

        b1_1 = Button(bg_img,text= "Train Data",cursor="hand2",command=self.train_classifier,font= ("Times New Roman",15, "bold"), bg="dark blue",fg="white")
        b1_1.place(x = 150, y = 450,width= 170,height=40)

#Student Photos Button
        img17= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\student_photos.jpg")
        img17 = img17.resize((170,170),Image.ANTIALIAS)
        self.photoimg17=ImageTk.PhotoImage(img17)

        b1 = Button(bg_img,image=self.photoimg17,cursor="hand2",command = self.open_img)
        b1.place(x = 400, y = 300,width= 170,height=170)

        b1_1 = Button(bg_img,text= "Student Photos",cursor="hand2",command = self.open_img,font= ("Times New Roman",15, "bold"), bg="dark blue",fg="white")
        b1_1.place(x = 400, y = 450,width= 170,height=40) 

#Developer Button
        img18= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\develop.jpg")
        img18 = img18.resize((170,170),Image.ANTIALIAS)
        self.photoimg18=ImageTk.PhotoImage(img18)

        b1 = Button(bg_img,image=self.photoimg18,cursor="hand2",command= self.developer)
        b1.place(x = 650, y = 300,width= 170,height=170)

        b1_1 = Button(bg_img,text= "Developer",cursor="hand2",command= self.developer,font= ("Times New Roman",15, "bold"), bg="dark blue",fg="white")
        b1_1.place(x = 650, y = 450,width= 170,height=40)

#Exit Button
        img19= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\exit.jpg")
        img19 = img19.resize((170,170),Image.ANTIALIAS)
        self.photoimg19=ImageTk.PhotoImage(img19)

        b1 = Button(bg_img,image=self.photoimg19,cursor="hand2")
        b1.place(x = 900, y = 300,width= 170,height=170)

        b1_1 = Button(bg_img,text= "Exit",cursor="hand2",font= ("Times New Roman",15, "bold"), bg="dark blue",fg="white")
        b1_1.place(x = 900, y = 450,width= 170,height=40)

    def open_img(self):
        os.startfile("C:\\Users\\kadal\\Desktop\\Project\\Face_Recognisation_System\\data")

    #def iExit(self):
     #   self.iExit = tkinter.askyesno("Face Recognization", "Are you sure you want to exit this Project?",parent = self.root)
      #  if self.iExit>0:
       #     self.root.destroy()
        #else:
         #   return

        

#=================Function Buttons==================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
 
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def train_classifier(self):
        data_dir = ("C:\\Users\\kadal\\Desktop\\Project\\Face_Recognisation_System\\data")
        path =[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces =[]
        ids = []

        for image in path:
            img=Image.open(image).convert('L')
            imageNp = np.array(img,'uint8')
            id =int(os.path.split(image)[1].split('.')[1]) 

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids =np.array(ids)

        #=================Train the Classifier and Save==============
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("C:\\Users\\kadal\\Desktop\\Project\\Face_Recognisation_System\\classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed")

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognization_System(root)
    root.mainloop()