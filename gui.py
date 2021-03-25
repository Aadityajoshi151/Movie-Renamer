from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def selectfiles():
    print("Select Files Clicked!")
def selectfolders():
    print("Select Folders Clicked")
def reset():
    print("Reset Button Clicked")
def rename():
    print("Rename Button Clicked")
def selectformat(event):
    global finalformat
    finalformat = selectedformat.get()
    if finalformat.find("Quality")>-1:
        messagebox.showinfo("Title","You Have Selected Format Which Involves Quality. If Quality Is Not Present In The Title, It Will Be Omitted")

root = Tk()
selectedformat = StringVar()
dualaudiocheck = IntVar()
subfoldercheck = IntVar()

formats = [
    "Movie Name",
"Movie Name (Year)",
"Movie Name [Year]",
"Movie Name (Quality)",
"Movie Name [Quality]",
"Movie Name (Filesize)",
"Movie Name [Filesize]",
"Movie Name (Year) [Quality]",
"Movie Name [Year] (Quality)",
"Movie Name (Quality) [Filesize]",
"Movie Name [Quality] (Filesize)",
"Movie Name (Year) [Qualtity] {Filesize}"
]
selectedformat.set(formats[0])
root.title("Movie Renamer")
root.geometry("350x250")
Label(root,text="Welcome To Movie Renamer",pady=10).pack()
Button(root,text="Select File(s)",command=selectfiles).pack()
Button(root,text="Select Folder(s)",command=selectfolders).pack()
formatdd = OptionMenu(root,selectedformat,*formats,command=selectformat)
formatdd.config(width=40,pady=5)
formatdd.pack(pady=5)
dualaudiocheckbox = Checkbutton(text = "Add Dual Audio Suffix (If Exists)", variable = dualaudiocheck,
                 onvalue = 1, offvalue = 0,)
subfoldercheckbox = Checkbutton(text = "Rename Files Inside Folder As Well", variable = subfoldercheck,
                 onvalue = 1, offvalue = 0,)
dualaudiocheckbox.pack()
subfoldercheckbox.pack()
Button(root,text="Rename",command=rename,width=7,height=3).pack(side=RIGHT,padx=10,pady=10)
Button(root,text="Reset",command=reset,width=6,height=3).pack(side=LEFT,padx=10,pady=10)
root.mainloop()