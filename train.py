from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import destroyAllWindows
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognisation System")

        title_lbl= Label(self.root, text = "TRAIN DATA SET", font= ("Times New Roman",35, "bold"), bg="dark blue",fg="white")
        title_lbl.place(x=0,y=0,width= 1330, height = 50)

        img_top = Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\students_pic.jpg")
        img_top = img_top.resize((1330,250),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root,image=self.photoimg_top) 
        f_lbl.place(x=0,y=50,width=1330,height=250)
        
        #button
        b1_1 = Button(self.root,text="STUDENT DETAILS",command=self.train_classifier, cursor="hand2", font=("times new roman",20, "bold"),bg ="dark green",fg ="white")
        b1_1.place(x=0,y=300,width=1330,height=50)

        img_bottom = Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\students_pic.jpg")
        img_bottom = img_bottom.resize((1330,300),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root,image=self.photoimg_top) 
        f_lbl.place(x=0,y=400,width=1330,height=250)

    def train_classifier(self):
        data_dir = ("C:\\Users\\kadal\\Desktop\\Project\\Face_Recognisation_System\\data")
        path =[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

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
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop() 