from cgitb import text
from hashlib import new
from tkinter import*
from tkinter import ttk
import PIL 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")
        
        #==================variables=====================
        self.var_attend_id = StringVar() 
        self.var_attend_roll = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_attendance = StringVar()

#tenth image
        img10= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\back2.jpg")
        img10 = img10.resize((130,130),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        f_lbl = Label(self.root,image=self.photoimg10)
        f_lbl.place(x=1170,y=0,width=130,height=730)

#Background image
        img11= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\back3.jpg")
        img11 = img11.resize((1530,710),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        bg_img = Label(self.root,image=self.photoimg11)
        bg_img.place(x=0,y=0,width=1530,height=710)
        
        title_lbl= Label(bg_img, text = "STUDENT ATTENDANCE", font= ("comicsansns 11 bold",30, "bold"), bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width= 1330, height = 60)

        main_frame = Frame(bg_img, bd = 2)
        main_frame.place(x=15, y=75, width= 1250, height = 600)

        #left label frame
        Left_frame = LabelFrame(main_frame,bd = 2, bg="white",relief=RIDGE,text = "Student Attendance Details", font = ("comicsansns 11 bold", 12,"bold"))
        Left_frame.place(x=10, y=10, width = 610, height = 950)

        img_left= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\students_pic.jpg")
        img_left = img_left.resize((600,120),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=35,y=110,width=600,height=120)

        #Student Class Information
        class_Student_frame = LabelFrame(main_frame,bd = 2, bg="white",relief=RIDGE,text = "Class Student Information", font = ("comicsansns 11 bold", 12,"bold"))
        class_Student_frame.place(x=15, y=280, width = 600, height = 275)

        #Attendance ID
        studentID_label = Label(class_Student_frame, text = "Attendance ID:", font =("comicsansns 11 bold", 13,"bold"), bg = "white")
        studentID_label.grid(row=0,column=0,padx=8,sticky = W)

        studentID_entry = ttk.Entry(class_Student_frame,width = 26,textvariable= self.var_attend_id,font =("comicsansns 11 bold", 13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=8,pady = 4,sticky = W)

        #Student Name
        studentName_label = Label(class_Student_frame, text = "Student Name:", font =("comicsansns 11 bold", 13,"bold"), bg = "white")
        studentName_label.grid(row=1,column=0,padx=8,sticky = W)

        studentName_entry = ttk.Entry(class_Student_frame,width = 26,textvariable= self.var_attend_name,font =("comicsansns 11 bold", 13,"bold"))
        studentName_entry.grid(row=1,column=1,padx=8,sticky = W)

        #Roll Number
        rollnumber_label = Label(class_Student_frame, text = "Roll Number:", font =("comicsansns 11 bold", 13,"bold"), bg = "white")
        rollnumber_label.grid(row=2,column=0,padx=8,pady = 4,sticky = W)

        rollnumber_entry = ttk.Entry(class_Student_frame,width = 26,textvariable= self.var_attend_roll,font =("comicsansns 11 bold", 13,"bold"))
        rollnumber_entry.grid(row=2,column=1,padx=8,pady = 4,sticky = W)

        #Department
        department_label = Label(class_Student_frame, text = "Department:", font =("comicsansns 11 bold", 13,"bold"), bg = "white")
        department_label.grid(row=2,column=0,padx=8,pady = 4,sticky = W)

        department_entry = ttk.Entry(class_Student_frame,width = 26,textvariable= self.var_attend_dep,font =("comicsansns 11 bold", 13,"bold"))
        department_entry.grid(row=2,column=1,padx=8,pady = 4,sticky = W)

        #Time 
        time_label = Label(class_Student_frame, text = "Time:", font =("comicsansns 11 bold", 13,"bold"), bg = "white")
        time_label.grid(row=3,column=0,padx=8,pady = 4,sticky = W)

        time_entry = ttk.Entry(class_Student_frame,width = 26,textvariable= self.var_attend_time,font =("comicsansns 11 bold", 13,"bold"))
        time_entry.grid(row=3,column=1,padx=8,pady = 4,sticky = W)

        #Attendance
        attendance_label = Label(class_Student_frame, text = "Attendance Status:", font =("comicsansns 11 bold", 13,"bold"), bg = "white")
        attendance_label.grid(row=4,column=0,padx=8,pady = 4,sticky = W)

        attendance_combo= ttk.Combobox(class_Student_frame,textvariable= self.var_attend_attendance,font = ("comicsansns 11 bold", 13,"bold"), state= "readonly",width = 24)
        attendance_combo["values"]=("Mark Status:","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=4, column=1,padx=8,pady=4,sticky=W)

        #Date
        Date_label = Label(class_Student_frame, text = "Date:", font =("comicsansns 11 bold", 13,"bold"), bg = "white")
        Date_label.grid(row=5,column=0,padx=8,pady = 4,sticky = W)

        Date_entry = ttk.Entry(class_Student_frame,width = 26,textvariable= self.var_attend_date,font =("comicsansns 11 bold", 13,"bold"))
        Date_entry.grid(row=5,column=1,padx=8,pady = 4,sticky = W)

        #bbuttonFrame
        btn_frame = Frame(class_Student_frame, bd = 1, relief= RIDGE, bg = "white")
        btn_frame.place(x = 40, y = 200, width= 535, height = 38)

        #Import CSV button
        save_btn = Button(btn_frame,text ="Import CSV",width = 10,command= self.importCsv,font =("comicsansns 11 bold", 12,"bold"),bg ="dark blue",fg ="white")
        save_btn.grid(row = 0, column = 0,padx=12,pady = 2,sticky = W)

        #Export CSV button
        update_btn = Button(btn_frame,text ="Export CSV",width = 10,command=self.exportCsv,font =("comicsansns 11 bold", 12,"bold"),bg ="dark blue",fg ="white")
        update_btn.grid(row = 0, column = 1,padx=12,pady = 2,sticky = W)

        #Update button
        delete_btn = Button(btn_frame,text ="Update",width = 10,font =("comicsansns 11 bold", 12,"bold"),bg ="dark blue",fg ="white")
        delete_btn.grid(row = 0, column = 2,padx=12,pady = 2,sticky = W)

        #Reset button
        reset_btn = Button(btn_frame,text ="Reset",width = 10,command=self.reset_data,font =("comicsansns 11 bold", 12,"bold"),bg ="dark blue",fg ="white")
        reset_btn.grid(row = 0, column = 3,padx=12,pady = 2,sticky = W)


#right label frame
        Right_frame = LabelFrame(main_frame,bd = 2, bg="white",relief=RIDGE,text = "Student Details", font = ("comicsansns 11 bold", 12,"bold"))
        Right_frame.place(x=630, y=10, width = 610, height = 550)

        img_right= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\students_pic2.jpg")
        img_right = img_right.resize((600,120),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=655,y=110,width=600,height=120)

        #Table Frame
        table_frame = Frame(main_frame,bd = 2, bg="white",relief=RIDGE,)
        table_frame.place(x=640, y=160, width = 590, height = 380)

        scroll_x = ttk.Scrollbar(table_frame,orient= HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient= VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("ID","StudentName","Department","Roll","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side= BOTTOM,fill= X)
        scroll_y.pack(side= RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID",text ="Student ID")
        self.AttendanceReportTable.heading("StudentName",text ="Student Name")
        self.AttendanceReportTable.heading("Roll",text ="Roll Number")
        self.AttendanceReportTable.heading("Department",text ="Department")
        self.AttendanceReportTable.heading("Time",text ="Time")
        self.AttendanceReportTable.heading("Date",text ="Date")
        self.AttendanceReportTable.heading("Attendance",text ="Attendance")
        

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("ID",width = 100)
        self.AttendanceReportTable.column("StudentName",width = 100)
        self.AttendanceReportTable.column("Roll",width = 100)
        self.AttendanceReportTable.column("Department",width = 100)
        self.AttendanceReportTable.column("Time",width = 100)
        self.AttendanceReportTable.column("Date",width = 100)
        self.AttendanceReportTable.column("Attendance",width = 100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir= os.getcwd(), title = "Open CSV", filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data is found to Export", parent = self.root)
                return False
            fln = filedialog.askopenfilename(initialdir= os.getcwd(), title = "Open CSV", filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data is exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root)
    #==================get cursor==============
    def get_cursor(self,event = ''):
        cursor_row =self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        data = content["values"]

        self.var_attend_id.set(data[0])
        self.var_attend_name.set(data[1])
        self.var_attend_roll.set(data[2])
        self.var_attend_dep.set(data[3])
        self.var_attend_time.set(data[4])
        self.var_attend_date.set(data[5])
        self.var_attend_attendance.set(data[6])
    #===================Reset Data================
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_name.set("")
        self.var_attend_roll.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("Mark Status:")
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()