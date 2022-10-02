

from tkinter import *
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os


root=Tk()

####--------------------functions-------------------
def new():
    global file
    file=None
    root.title("Untitled -Notepad")
    text_area.delete(1.0,END)

def Open():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Document","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        text_area.delete(1.0, END)
        f= open(file,"r")
        text_area.insert(1.0,f.read())
        f.close()
def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(text_area.get(1.0, END))
        f.close()

def Exit():
    exit()
def cut():
    text_area.event_generate("<<Cut>>")
def copy():
    text_area.event_generate("<<Copy>>")
def paste():
    text_area.event_generate("<<Paste>>")
def about():
    msg.showinfo(title="About software",message="This software is developed by Pawan Sapkota. All right reserved to Pawan Sapkota")
def delete():
    text_area.delete(1.0, END)


root.title("Notepad")
root.wm_iconbitmap("1icon.png")

root.geometry("500x500")
root.minsize(200,200)

menubar=Menu(root)



# for text entry
text_area=Text(root,font="timesnewroman 15")
text_area.pack(fill=BOTH,expand=True)
file=NONE


# menubar content

file_menu=Menu(menubar)
edit_menu=Menu(menubar)
help_menu=Menu(menubar)

# displaying the main content in menubar
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit",menu=edit_menu)
menubar.add_cascade(label="Help",menu=help_menu)

##displaying the submenu from mainmenu(file)

file_menu.add_command(label="New",command=new)
file_menu.add_command(label="Open",command=Open)
file_menu.add_command(label="Save",command=save)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=Exit)

##displaying the submenu from mainmenu(Edit)

edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_command(label="Paste",command=paste)
edit_menu.add_command(label="Delete",command=delete)

#displaying the submenu of help
help_menu.add_command(label="About",command=about)


# displaying the  scroll bar
scrolly=Scrollbar(text_area)
scrolly.pack(fill=Y,side=RIGHT)
scrolly.config(command=text_area.yview)
text_area.config(yscrollcommand=scrolly.set)


root.config(menu=menubar)
root.mainloop()