from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
import wikipedia

# declare obj
root=Tk(className="------This editor is created by Mr Priyesh Ranjan--------")
# for text Editor
textpad=scrolledtext.ScrolledText(root,width=100,height=80)
# for open file
def open_command():
    file=filedialog.askopenfile(parent=root,mode='rb',title="select a file",
                                filetypes=(("Files","*.py"),("All Files","*.*")))
    if file !=None:
        contents=file.read()
        textpad.insert('1.0',contents)
        file.close()

# for save file
def save_command():
    file=filedialog.asksaveasfile(mode='w', filetypes=(("Files","*.py"),("All Files","*.*")))
    if file !=None:
        data=textpad.get('1.0',END + '-1c')
        file.write(data)
        file.close()
def entry_kk():
    ans=entry.get()
    textpad.delete(1.0,END)
    try:
      detl=wikipedia.summary(ans)
      textpad.insert(INSERT,detl)
    except:
      textpad.insert(INSERT,"Please insert correct input or check input connection")

# for exit file
def exit_command():
    if messagebox.askokcancel("Exit","Do you want to exit ?\n"
                                     "if 'Yes' press ok else 'Cancel'"):
        print("We are exiting Window")
        root.quit()  # we can use "root.destroy()" also.....
# for about
def about_command():
    label=messagebox.showinfo("About","This is "
                                      "text Editor Created by Mr Priyesh Ranjan.\n"
                                      "He is a final year student of bhagalpur college of enginering \n"
                                      "with an stream of computer Science")
menu1=Menu(root)
root.config(menu=menu1)
submenu=Menu(menu1)
menu1.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New",)
submenu.add_command(label="Open",command=open_command)
submenu.add_command(label="Save",command=save_command)
submenu.add_command(label="Exit",command=exit_command)
menu1.add_cascade(label="Edit")
menu1.add_cascade(label="View")
menu1.add_cascade(label="Navigate")
menu1.add_cascade(label="Code")
menu1.add_cascade(label="Refractor")
submenu1=Menu(menu1)
menu1.add_cascade(label="Help",menu=submenu1)
submenu1.add_command(label="About.....",command=about_command)
submenu1.add_command(label="search",command=entry_kk)
textpad.pack()
root.mainloop()