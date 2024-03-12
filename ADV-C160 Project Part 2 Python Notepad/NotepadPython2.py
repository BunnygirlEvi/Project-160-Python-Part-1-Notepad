from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import os

root=Tk()
root.title("Notepad")
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background="#ffea82")
open_img = ImageTk.PhotoImage(Image.open ("open.png"))
save_img = ImageTk.PhotoImage(Image.open ("save.png"))
run_img = ImageTk.PhotoImage(Image.open ("run.png"))

label1 = Label(root, text= "File name")
label1.place(relx= 0.3, rely= 0.05, anchor=CENTER)
file_entry = Entry(root)
file_entry.place(relx= 0.55, rely= 0.05, anchor=CENTER)
my_text= Text(root,height=35,width=90)
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)
root.mainloop()

