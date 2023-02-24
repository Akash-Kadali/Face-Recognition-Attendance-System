from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")

        #==============Variable==================
        self.var_name = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_roll = StringVar()
        self.var_std_id = StringVar() 
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_gender = StringVar()
        self.var_div = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()


#tenth image
        img10= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\back2.jpg")
        img10 = img10.resize((130,130),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        f_lbl = Label(self.root,image=self.photoimg10)
        f_lbl.place(x=1170,y=0,width=130,height=130)

#Background image
        img11= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\back3.jpg")
        img11 = img11.resize((1530,710),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        bg_img = Label(self.root,image=self.photoimg11)
        bg_img.place(x=0,y=0,width=1530,height=710)
        
        title_lbl= Label(bg_img, text = "STUDENT DETAILS", font= ("Times New Roman",35, "bold"), bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width= 1330, height = 60)

        main_frame = Frame(bg_img, bd = 2)
        main_frame.place(x=15, y=75, width= 1250, height = 600)

        #left label frame
        Left_frame = LabelFrame(main_frame,bd = 2, bg="white",relief=RIDGE,text = "Student Details", font = ("times new roman", 12,"bold"))
        Left_frame.place(x=10, y=10, width = 610, height = 550)

        img_left= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\students_pic.jpg")
        img_left = img_left.resize((600,120),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=35,y=110,width=600,height=120)

        #current course
        current_course_frame = LabelFrame(main_frame,bd = 2, bg="white",relief=RIDGE,text = "Current Course Information", font = ("times new roman", 12,"bold"))
        current_course_frame.place(x=15, y=155, width = 600, height = 125)

        #Department
        dep_label = Label(current_course_frame,text = "Department",font = ("times new roman", 12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo= ttk.Combobox(current_course_frame,textvariable=self.var_dep,font = ("times new roman", 12,"bold"), state= "readonly")
        dep_combo["values"]=("Select Department:","Computer Science","Information Technology","Civil","Mechanical","Chemical","Biotechnology")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1,padx=2,pady=10)
        
        #Course
        dep_label = Label(current_course_frame, text = "Course",font = ("times new roman", 12,"bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10,sticky=W)

        dep_combo= ttk.Combobox(current_course_frame,textvariable=self.var_course,font = ("times new roman", 12,"bold"), state= "readonly")
        dep_combo["values"]=("Select Course:","Machine Learning","Autometa","Computer Networks","Software Engineering","Data Structures","Mathematics")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label = Label(current_course_frame, text = "Year",font = ("times new roman", 12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        dep_combo= ttk.Combobox(current_course_frame,textvariable=self.var_year,font = ("times new roman", 12,"bold"), state= "readonly")
        dep_combo["values"]=("Select Year:","B.Tech-1","B.Tech-2","B.Tech-3","B.Tech-4","M.Tech-1","M.Tech-2")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label = Label(current_course_frame, text = "Semester",font = ("times new roman", 12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        dep_combo= ttk.Combobox(current_course_frame,textvariable=self.var_semester,font = ("times new roman", 12,"bold"), state= "readonly")
        dep_combo["values"]=("Select Semester:","Semester-1","Semester-2")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=3,padx=2,pady=10,sticky=W)

        #Student Class Information
        class_Student_frame = LabelFrame(main_frame,bd = 2, bg="white",relief=RIDGE,text = "Class Student Information", font = ("times new roman", 12,"bold"))
        class_Student_frame.place(x=15, y=280, width = 600, height = 275)

        #Student ID
        studentID_label = Label(class_Student_frame, text = "Student ID:", font =("times new roman", 13,"bold"), bg = "white")
        studentID_label.grid(row=0,column=0,padx=8,sticky = W)

        studentID_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id, width = 16, font =("times new roman", 13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=8,pady = 4,sticky = W)

        #Student Name
        studentID_label = Label(class_Student_frame, text = "Student Name:", font =("times new roman", 13,"bold"), bg = "white")
        studentID_label.grid(row=0,column=2,padx=8,sticky = W)

        studentID_entry = ttk.Entry(class_Student_frame,textvariable=self.var_name,width = 16, font =("times new roman", 13,"bold"))
        studentID_entry.grid(row=0,column=3,padx=8,sticky = W)

        #Class Division
        studentID_label = Label(class_Student_frame, text = "Class Division:", font =("times new roman", 13,"bold"), bg = "white")
        studentID_label.grid(row=3,column=0,padx=8,sticky = W)

        #studentID_entry = ttk.Entry(class_Student_frame,textvariable=self.var_div,width = 16, font =("times new roman", 13,"bold"))
        #studentID_entry.grid(row=3,column=1,padx=8,pady = 4,sticky = W)

        div_combo= ttk.Combobox(class_Student_frame,textvariable=self.var_div,font = ("times new roman", 12,"bold"), state= "readonly",width=16)
        div_combo["values"]=("Class Division:","A","B")
        div_combo.current(0)
        div_combo.grid(row=3, column=1,padx=8,pady=4, sticky=W)

        #Roll Number
        rollnumber_label = Label(class_Student_frame, text = "Roll Number:", font =("times new roman", 13,"bold"), bg = "white")
        rollnumber_label.grid(row=3,column=2,padx=8,pady = 4,sticky = W)

        rollnumber_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width = 16, font =("times new roman", 13,"bold"))
        rollnumber_entry.grid(row=3,column=3,padx=8,pady = 4,sticky = W)

        #Email
        eMail_label = Label(class_Student_frame, text = "Email:", font =("times new roman", 13,"bold"), bg = "white")
        eMail_label.grid(row=5,column=0,padx=8,pady = 4,sticky = W)

        rollnumber_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width = 16, font =("times new roman", 13,"bold"))
        rollnumber_entry.grid(row=5,column=1,padx=8,pady = 4,sticky = W)

        #Gender
        gender_label = Label(class_Student_frame, text = "Gender:", font =("times new roman", 13,"bold"), bg = "white")
        gender_label.grid(row=5,column=2,padx=8,pady = 4,sticky = W)

        gender_combo= ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font = ("times new roman", 12,"bold"), state= "readonly",width = 16)
        gender_combo["values"]=("Gender:","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=5, column=3,padx=8,pady=4,sticky=W)

        #Phone Number
        phoneNumber_label = Label(class_Student_frame, text = "Phone Number:", font =("times new roman", 13,"bold"), bg = "white")
        phoneNumber_label.grid(row=7,column=0,padx=8,pady = 4,sticky = W)

        phoneNumber_entry = ttk.Entry(class_Student_frame,textvariable=self.var_phone,width = 16, font =("times new roman", 13,"bold"))
        phoneNumber_entry.grid(row=7,column=1,padx=8,pady = 4,sticky = W)

        #Address Line 
        address1_label = Label(class_Student_frame, text = "Address:", font =("times new roman", 13,"bold"), bg = "white")
        address1_label.grid(row=7,column=2,padx=8,pady = 4,sticky = W)

        address1_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width = 16, font =("times new roman", 13,"bold"))
        address1_entry.grid(row=7,column=3,padx=8,pady = 4,sticky = W)

        #Teacher Name
        teacherName_label = Label(class_Student_frame, text = "Teacher Name:", font =("times new roman", 13,"bold"), bg = "white")
        teacherName_label.grid(row=9,column=0,padx=8,pady = 4,sticky = W)

        teacherName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width = 16, font =("times new roman", 13,"bold"))
        teacherName_entry.grid(row=9,column=1,padx=8,pady = 4,sticky = W)

        #DOB
        DOB_label = Label(class_Student_frame, text = "Date of Birth:", font =("times new roman", 13,"bold"), bg = "white")
        DOB_label.grid(row=9,column=2,padx=8,pady = 4,sticky = W)

        DOB_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width = 16, font =("times new roman", 13,"bold"))
        DOB_entry.grid(row=9,column=3,padx=8,pady = 4,sticky = W)

        #radioButtons
        self.var_radio1=StringVar()
        radiobtn1= ttk.Radiobutton(class_Student_frame,variable = self.var_radio1,text = "No Photo Sample", value = "No")
        radiobtn1.grid(row=11,column=0)

        radiobtn2= ttk.Radiobutton(class_Student_frame,variable = self.var_radio1,text = "Add Photo Sample", value = "Yes")
        radiobtn2.grid(row=11,column=1)

        #bbuttonFrame
        btn_frame = Frame(class_Student_frame, bd = 2, relief= RIDGE, bg = "white")
        btn_frame.place(x = 2, y = 200, width= 590, height = 36)

        #save button
        save_btn = Button(btn_frame,text ="Save",command= self.add_data,width = 9,font =("times new roman", 12,"bold"),bg ="dark blue",fg ="white")
        save_btn.grid(row = 0, column = 0)

        #update button
        update_btn = Button(btn_frame,text ="Update",command= self.update_data,width = 9,font =("times new roman", 12,"bold"),bg ="dark blue",fg ="white")
        update_btn.grid(row = 0, column = 1)

        #delete button
        delete_btn = Button(btn_frame,text ="Delete",command = self.delete_data,width = 9,font =("times new roman", 12,"bold"),bg ="dark blue",fg ="white")
        delete_btn.grid(row = 0, column = 2)

        #reset button
        reset_btn = Button(btn_frame,text ="Reset",command = self.reset_data,width = 9,font =("times new roman", 12,"bold"),bg ="dark blue",fg ="white")
        reset_btn.grid(row = 0, column = 3)

        #takephoto button
        takephoto_btn = Button(btn_frame,text ="Take Pic",command =  self.generate_dataset,width = 12,font =("times new roman", 12,"bold"),bg ="dark blue",fg ="white")
        takephoto_btn.grid(row = 0, column = 4)

        #update button
        updatephoto_btn = Button(btn_frame,text ="Update Pic",width = 12,font =("times new roman", 12,"bold"),bg ="dark blue",fg ="white")
        updatephoto_btn.grid(row = 0, column = 5)

        
#right label frame
        Right_frame = LabelFrame(main_frame,bd = 2, bg="white",relief=RIDGE,text = "Student Details in Tabular Format", font = ("times new roman", 12,"bold"))
        Right_frame.place(x=630, y=10, width = 610, height = 550)

        img_right= Image.open(r"C:\Users\kadal\Desktop\Project\Face_Recognisation_System\college_Images\students_pic2.jpg")
        img_right = img_right.resize((600,120),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=655,y=110,width=600,height=120)

        #Search Frame
        search_frame = LabelFrame(main_frame,bd = 2, bg="white",relief=RIDGE,text = "Search System", font = ("times new roman", 12,"bold"))
        search_frame.place(x=635, y=155, width = 600, height = 400)

        search_label = Label(search_frame, text = "Search By",font = ("times new roman", 12,"bold"),bg="green", fg = "white")
        search_label.grid(row=0,column=0,padx=10,pady =5,sticky=W)

        search_combo= ttk.Combobox(search_frame,font = ("times new roman", 12,"bold"), state= "readonly")
        search_combo["values"]=("Select:","Roll Number","Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0, column=1,padx=2,pady=10,sticky=W)

        #Search Entry
        search_entry = ttk.Entry(search_frame, width = 12, font =("times new roman", 13,"bold"))
        search_entry.grid(row=0,column=2,padx=8,sticky = W)

        #Search Button
        search_btn = Button(search_frame,text ="Search",width = 9,font =("times new roman",12,"bold"),bg ="dark blue",fg ="white")
        search_btn.grid(row = 0, column = 3,padx=4)

        #Show All Button
        showall_btn = Button(search_frame,text ="Show All",width = 9,font =("times new roman", 12,"bold"),bg ="dark blue",fg ="white")
        showall_btn.grid(row = 0, column = 4,padx=4)

        #Table Frame
        table_frame = Frame(main_frame,bd = 2, bg="white",relief=RIDGE,)
        table_frame.place(x=640, y=220, width = 590, height = 330)

        scroll_x = ttk.Scrollbar(table_frame,orient= HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient= VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("name","year","sem","roll","id","dep","course","div","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side= BOTTOM,fill= X)
        scroll_y.pack(side= RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("name",text ="StudentName")
        self.student_table.heading("year",text ="Year")
        self.student_table.heading("sem",text ="Semester")
        self.student_table.heading("roll",text ="Roll")
        self.student_table.heading("id",text ="StudentID")
        self.student_table.heading("dep",text ="Department")
        self.student_table.heading("course",text ="Course")
        self.student_table.heading("div",text ="Gender")
        self.student_table.heading("gender",text ="Division")
        self.student_table.heading("dob",text ="DateofBirth")
        self.student_table.heading("email",text ="Email")
        self.student_table.heading("phone",text ="Phone")
        self.student_table.heading("address",text ="Address")
        self.student_table.heading("teacher",text ="Teacher")
        self.student_table.heading("photo",text ="PhotoSampleStatus")

        self.student_table["show"]="headings"

        self.student_table.column("name",width = 100)
        self.student_table.column("year",width = 100)
        self.student_table.column("sem",width = 100)
        self.student_table.column("roll",width = 100)
        self.student_table.column("id",width = 100)
        self.student_table.column("dep",width = 100)
        self.student_table.column("course",width = 100)
        self.student_table.column("gender",width = 100)
        self.student_table.column("div",width = 100)
        self.student_table.column("dob",width = 100)
        self.student_table.column("email",width = 100)
        self.student_table.column("phone",width = 100)
        self.student_table.column("address",width = 100)
        self.student_table.column("teacher",width = 100)
        self.student_table.column("photo",width = 150)

        self.student_table.column("dep", width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    #=========================function declaration=======================
    def add_data(self):
        try:
            if self.var_dep.get()=="Select Department" or self.var_name.get() == "" or self.var_std_id.get()=="":
                messagebox.showerror("Error", "All Fields are required", parent = self.root)
            else:
                conn = mysql.connector.connect(host= "127.0.0.1",port="3307",username = "root",password= "Nirvignaa@2002", database = "face_recognize")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student_final values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_name.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added successfully", parent = self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root)   
    #====================fetch==============
    def fetch_data(self):
        conn = mysql.connector.connect(host= "127.0.0.1",port="3307",username = "root",password= "Nirvignaa@2002", database = "face_recognize")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student_final")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(* self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close() 
    #==================get cursor============
    def get_cursor(self,event = ''):
        cursor_focus =self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_name.set(data[0]),
        self.var_year.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_roll.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_dep.set(data[5]),
        self.var_course.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_div.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get() == "" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)
        else:
            try:
                Upadate = messagebox.askyesno("Update","Do you want to update",parent= self.root)
                if Upadate>=0:
                    conn = mysql.connector.connect(host= "127.0.0.1",port="3307",username = "root",password= "Nirvignaa@2002", database = "face_recognize")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student_final set StudentName =%s,Year=%s,Semester=%s,Roll=%s,Dep=%s,course=%s,Gender=%s,Division=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                
                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_std_id.get()
                                                                                                                                                                                    ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details successfully updated", parent =self.root)                                                                                                                                                                 
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root)
    #delete function 
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to Delete this Student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host= "127.0.0.1",port="3307",username = "root",password= "Nirvignaa@2002", database = "face_recognize")
                    my_cursor = conn.cursor()
                    sql = "delete from student_final where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent= self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root) 
    #reset function
    def reset_data(self):
        self.var_name.set("")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_roll.set("")
        self.var_std_id.set("")
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course") 
        self.var_gender.set("Select Gender")
        self.var_div.set("Select Division") 
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    #===============Generate Data Set or take a Photo Sample=============
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get() == "" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host= "127.0.0.1",port="3307",username = "root",password= "Nirvignaa@2002", database = "face_recognize")
                my_cursor = conn.cursor()
                my_cursor.execute("select *  from student_final")
                my_result =my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id+=1
                my_cursor.execute("update student_final set StudentName =%s,Year=%s,Semester=%s,Roll=%s,Dep=%s,course=%s,Gender=%s,Division=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                
                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_std_id.get() == id+1
                                                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #===================Load predefined Data from Frontal Face===================
                face_classifier=cv2.CascadeClassifier("C:\\Users\\kadal\\Desktop\\Project\\Face_Recognisation_System\\haarcascade_frontalface_default.xml")
    

                def face_cropped(img):
                    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling Factor = 1.3
                    #Minimum Neighbour = 5

                    for(x,y,w,h) in faces:
                        face_cropped= img[y:y+h,x:x+w]
                        return face_cropped
                        

                cap = cv2.VideoCapture(0)


                img_id = 0
                while True:
                    ret, my_frame= cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id = img_id + 1
                        face = cv2.resize(face_cropped(my_frame),(650,650))                                                                                                                                                                
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "C:\\Users\\kadal\\Desktop\\Project\\Face_Recognisation_System\\data\student"+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(40,40),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()             
                messagebox.showinfo("Result","Generating Datasets Completed!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root) 

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()