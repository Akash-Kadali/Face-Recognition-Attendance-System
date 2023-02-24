from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import destroyAllWindows
import mysql.connector
import cv2
import os
import numpy as np


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognisation System")

        title_lbl= Label(self.root, text = "ABOUT DEVELOPER @akash_kadali", font= ("Times New Roman",35, "bold"), bg="black",fg="white")
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

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop() 