# Tkinter GUI Text Editor Announcement | Python Tkinter GUI Tutorial In Hindi #28

#My Approach To Make Own Text Editor(NotePad)

from tkinter import * 
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
from tkinter import simpledialog

#Importing components
from Files.help import HelpDialog
from Files.about import About
from Files.rate import RatingDialog

root = Tk()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
root.geometry(f"{ws}x{hs}")
root.title("Notepad - By Rajan Poudel")
ico = Image.open('Icons/notepad.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

#App Logic

#User Defined Functions

def open_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"),("Python files", "*.py"), ("All files", "*.*")])
    root.title(file_path)
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text.delete("1.0", tk.END)
            text.insert("1.0", content)
    
def save():
    try:
      content = text.get("1.0", tk.END)
      with open(file_path, "w") as file:
          file.write(content)
    except Exception as e:
      tmsg.showerror("Error","Sorry ! Couldn't Save The File")

def saveas():
  file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"),("Python files", "*.py"), ("All files", "*.*")])
  if file_path:
        with open(file_path, "w") as file:
            content = text.get("1.0", tk.END)
            file.write(content)

def exit():
        tmsg_value=tmsg.askquestion("Exit","Wanna Exit The Application ?")
        if tmsg_value == "yes":
            root.destroy()

def review():
       review = simpledialog.askstring("Review Me", "Please provide your feedback , review or complains . I will get to you soon")
       if review=='':
          pass
       elif review is not None:
            f = open("Rating&Review/review.txt","a")
            f.write(f"Review : {review} \n")
            f.close()
            tmsg.showinfo("Thank You", "Thank you for the review and feedback!")
def cut():
    text.event_generate(("<<Cut>>"))
def copy():
    text.event_generate(("<<Copy>>"))
def paste():
    text.event_generate(("<<Paste>>"))

def new_file():   
    root.title("Untitled - Notepad")
    text.delete(1.0,END)

#Menubar
menubar= Menu(root)

m1 = Menu(menubar,tearoff=0)
m1.add_command(label="New",command=new_file)
m1.add_command(label="Open",command=open_file)
m1.add_separator()
m1.add_command(label="Save",command=save)
m1.add_command(label="Save As",command=saveas)
m1.add_command(label="Save All",command=save)
m1.add_separator()
m1.add_command(label="Exit",command=exit)
menubar.add_cascade(label="File",menu=m1)

m2 = Menu(menubar,tearoff=0)
m2.add_command(label="Cut",command=cut)
m2.add_command(label="Copy",command=copy)
m2.add_command(label="Paste",command=paste)
menubar.add_cascade(label="Edit",menu=m2)

menubar.add_command(label="About",command=lambda: About(root))

menubar.add_command(label="Help",command=lambda: HelpDialog(root))

menubar.add_command(label="Rate Me",command=lambda: RatingDialog(root))

menubar.add_command(label="Review",command=review)


root.config(menu=menubar)

#ScrollBar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

#Text Area
text = Text(root,yscrollcommand=scrollbar.set,font=("Noto Sans","19"))
text.pack(fill=BOTH,expand=True)
scrollbar.config(command=text.yview)

if __name__ == "__main__":
  root.mainloop()
