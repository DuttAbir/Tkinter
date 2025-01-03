from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def enter_data():

    terms = terms_status_var.get()

    if terms =="Accepted":
        firstName = first_name_entry.get()
        last_name = last_name_entry.get()
        if firstName and last_name:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combox.get()
            numcourses = numcourse_spinbox.get()
            numsemesters = numsemester_spinbox.get()
            regStatus = reg_status_var.get()

            print(f"First Name: {firstName} Last Name: {last_name}")
            print(f"Title: {title} Age: {age} Nationality: {nationality}")
            print(f"# Courses: {numcourses} # Semesters: {numsemesters}")
            print(f"Registration Status : {regStatus}")
            print("-----------------------------------------------")
        else:
            messagebox.showwarning(title="ERROR",message="First name and Last name required")
    else:
        messagebox.showwarning(title="ERROR", message="You have not accepted the terms")



root  = Tk()

root.title("Data Entry Form")

frame = Frame(root)
frame.pack()

#user info

user_info_frame = LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0,padx=20,pady=10)

first_name_label = Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry = Entry(user_info_frame)
last_name_entry = Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

title_label = Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame,values=["","Mr.","Ms.","Dr."])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_label = Label(user_info_frame, text="Age")
age_spinbox = Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3,column=0)

nationality_label = Label(user_info_frame, text="Nationality")
nationality_combox = ttk.Combobox(user_info_frame, values=["Asia","Europe","Africa","North America","South America","Oceinia"])
nationality_label.grid(row=2,column=1)
nationality_combox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#course info

courses_frame = LabelFrame(frame)
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=10)

register_label = Label(courses_frame,text="Registration Status")
reg_status_var = StringVar(value="Not Registered")
register_check = Checkbutton(courses_frame, text="Currently Registered",variable=reg_status_var, onvalue="Registered",offvalue="Not Registered")
register_label.grid(row=0,column=0)
register_check.grid(row=1,column=0)

numcourse_label = Label(courses_frame,text="# Completed Courses")
numcourse_spinbox = Spinbox(courses_frame,from_=0,to='infinity')
numcourse_label.grid(row=0,column=1)
numcourse_spinbox.grid(row=1,column=1)

numsemester_label = Label(courses_frame,text="# Semester")
numsemester_spinbox = Spinbox(courses_frame,from_=0,to="infinity")
numsemester_label.grid(row=0,column=2)
numsemester_spinbox.grid(row=1,column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#Accept terms 

terms_frame = LabelFrame(frame,text="Terms & Conditions")
terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)

terms_status_var = StringVar(value="Not Accepted")
terms_check = Checkbutton(terms_frame,text="I accept the terms & conditions",variable=terms_status_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0,column=0)

#Button 

button = Button(frame, text="Enter Data",command=enter_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=10)

root.mainloop()