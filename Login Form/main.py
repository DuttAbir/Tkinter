from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login Form")
root.geometry("340x440")
root.config(bg="#333333")

frame = Frame(bg="#333333")

def login():
    user = "ABIR"
    password = "12345"

    if user_entry.get()==user and pass_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You have logged in succesfully")
    else:
        messagebox.showerror(title="INVALID", message="Invalid credentials")


log_lebel = Label(frame, text="Login",bg="#333333",fg="#FF2349",font=["Arial",30])
user_label = Label(frame, text="Username",bg="#333333",fg="#FFFFFF",font=["Arial",16])
user_entry = Entry(frame, font=["Arial",16])
pass_entry = Entry(frame, show="*", font=["Arial",16])
pass_label = Label(frame, text="Password",bg="#333333",fg="#FFFFFF", font=["Arial",16])
log_buton = Button(frame, text="LOGIN",bg="#FF2349",fg="#FFFFFF", font=["Arial",16],command=login)

log_lebel.grid(row=0, column=0, columnspan=2,sticky="news", pady=40)
user_label.grid(row=1, column=0)
user_entry.grid(row=1,column=1,pady=20)
pass_label.grid(row=2,column=0)
pass_entry.grid(row=2, column=1,pady=20)

log_buton.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()


root.mainloop()
