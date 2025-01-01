from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import *
import os

def NewFile():
    global file
    root.title("Untitled -- Notepad")
    file = None

    textarea.delete(1.0, END)

def OpenFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file) + "-- Notepad")
        textarea.delete(1.0, END)
        f= open(file,'r')
        textarea.insert(1.0, f.read())
        f.close()

def SaveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:
            f = open(file,'w')
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "--Notepad")
            print("SAVED")

    else:
        f = open(file,'w')
        f.write(textarea.get(1.0, END))
        f.close()


def QuitApp():
    root.destroy()
def cut():
    textarea.event_generate(("<<Cut>>"))
def copy():
    textarea.event_generate(("<<Copy>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad", "Notepad by Duttabir")

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled-- Notepad")
    root.wm_iconbitmap('Notepad/notepad-icon.ico')
    root.geometry("480x360")

    textarea = Text(root, font="lucida 10")
    textarea.pack(expand = True, fill = BOTH)

    file = None

    MenuBar = Menu(root)

    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=NewFile)
    FileMenu.add_command(label="Open", command=OpenFile)
    FileMenu.add_command(label="Save", command=SaveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=QuitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=MenuBar)

    Scroll  = Scrollbar(textarea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)
    
    root.mainloop()