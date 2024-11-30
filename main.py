from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("IMAGE VIEWER")
root.geometry("360x480")
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='Python_image_viewer/image.png'))

img1 = Image.open("Python_image_viewer/Images/panda.png")
img1_resize = img1.resize((360, 360))
my_img1 = ImageTk.PhotoImage(img1_resize)

img2 = Image.open("Python_image_viewer/Images/panda2.png")
img2_resize = img2.resize((360, 360))
my_img2 = ImageTk.PhotoImage(img2_resize)

img3 = Image.open("Python_image_viewer/Images/panda3.png")
img3_resize = img3.resize((360, 360))
my_img3 = ImageTk.PhotoImage(img3_resize)


img4 = Image.open("Python_image_viewer/Images/pandasssss.png")
img4_resize = img4.resize((360, 360))
my_img4 = ImageTk.PhotoImage(img4_resize)

img5 = Image.open("Python_image_viewer/Images/po.png")
img5_resize = img5.resize((360, 360))
my_img5 = ImageTk.PhotoImage(img5_resize)

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

pic = Label(root, image=my_img1)
pic.grid(row=0, column=0, columnspan=3)

status = Label(text=(f"Image 1 of {len(image_list)}"), bd=1, relief=SUNKEN, anchor=E)


def next(image_num):
  global pic
  global button_next
  global button_back

  pic. grid_forget()
  pic = Label(image=image_list[image_num-1])
  pic.grid(row=0, column=0, columnspan=3)
  button_next = Button(root, text=">>",command=lambda:next(image_num+1))
  button_back = Button(root, text="<<",command=lambda:back(image_num-1))

  if (image_num==5):
    button_next = Button(root, text=">>", state= DISABLED)
  
  button_back.grid( row=1, column=0)
  button_next.grid( row=1, column=2)

  status = Label(text=(f"Image {image_num} of {len(image_list)}"), bd=1, relief=SUNKEN, anchor=E)
  status.grid(row=2, column=0, columnspan=3, sticky=W+E)
  
def back(image_num):
  global pic
  global button_next
  global button_back

  pic. grid_forget()
  pic = Label(image=image_list[image_num-1])
  pic.grid(row=0, column=0, columnspan=3)
  button_next = Button(root, text=">>",command=lambda:next(image_num+1))
  button_back = Button(root, text="<<",command=lambda:back(image_num-1))

  if (image_num==1):
    button_back = Button(root, text="<<", state= DISABLED)

  button_back.grid( row=1, column=0)
  button_next.grid( row=1, column=2)

  status = Label(text=(f"Image {image_num} of {len(image_list)}"), bd=1, relief=SUNKEN, anchor=E)
  status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", command=back, state= DISABLED)
button_exit = Button(root, text="EXIT",command= root.quit)
button_next = Button(root, text=">>", command= lambda:next(2))

button_back.grid( row=1, column=0)
button_exit.grid( row=1, column=1)
button_next.grid( row=1, column=2, pady=20)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
