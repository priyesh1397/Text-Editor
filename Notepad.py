       #                                  " Text Editor "
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import colorchooser
import wikipedia
import webbrowser
import time
import calendar
                                        # CREATING CLASS
class editor:
    current_opened_file="no file"

                                       # OPENING FILE FUNCTION
    def open_file(self,event=""):
        f=filedialog.askopenfile(mode='rb',initialdir='/',title="Open file",filetypes=(("file type",".txt"),("All files","*.*")))
        if f!=None:
            self.txt.delete(1.0,END)
            for lines in f:
                self.txt.insert(END,lines)
            self.current_opened_file=f.name
            f.close()
                                      # SAVE-FILE FUNCTION
    def save_file(self,event=""):
        if self.current_opened_file=="no file":
            self.saveas_file()
        else:
            f=open(self.current_opened_file,mode='w+')
            f.write(self.txt.get(1.0,END))
            f.close()

                                      # SAVE-AS FILE FUNCTION
    def saveas_file(self,event=""):
        f = filedialog.asksaveasfile(mode='w', default=".txt", filetypes=(("file type", ".txt"), ("All files", "*.*")))
        if f is None:
            return
        textt=self.txt.get(1.0,END)
        f.write(textt)
        f.close()
                                      # EXIT FILE
    def custom_exit(self,event=""):
        self.ans=tkinter.messagebox.askokcancel("Hi...This is Priyesh Ranjan","You want to quit the editor ? "
                                                " Save the file else you will lose the data...")
        if self.ans:
            print("Exit")
            self.master.destroy()
                                      # NEW FILE FUNCTION
    def new_file(self,event=""):
         self.txt.delete(1.0,END)
         self.current_opened_file="no file"
                                      #  COPY FILE FUNCTION
    def copy_file(self,event=""):
        self.txt.clipboard_clear()
        self.txt.clipboard_append(self.txt.selection_get())
                                      # PASTE FILE FUNCTION
    def paste_file(self,event=""):
        self.txt.insert(INSERT,self.txt.clipboard_get())

                                      # CUT FILE FUNCTION
    def cut_file(self,event=""):
        self.copy_file()
        self.txt.delete("sel.first","sel.last")
                                      # BACK GROUND COLOUR CHANGE
    def color_change(self,event=""):
        self.color=colorchooser.askcolor(title="Choose Color")
        self.txt.configure(background=self.color[1])

                                       # DATE/TIME
    def find_date(self):
        self.dte=time.asctime(time.localtime(time.time()))
        self.label=tkinter.messagebox.showinfo("The today date is :",self.dte)

                                        # DAY
    def find_day(self):
            self.day =calendar.month(2019,1)
            self.label = tkinter.messagebox.showinfo("The Today is :", self.day)
                                      # SEARCH THE TEXT
    def search_text(self,event=""):
        self.inputt=Entry(self.master)
        self.inputt.pack()
        self.str=self.inputt.get()
        self.txt.delete(1.0,END)
        try:
            self.detail=wikipedia.summary(self.str)
            self.txt.insert(INSERT,self.detail)
        except:
            self.txt.insert(INSERT,"Enter the correct meaningful word....")

                                        # BROWSER
    def browse(self,event=""):
         webbrowser.open_new(r"http://www.google.com")

                                        # ABOUT
    def about_command(self,event=""):
        self.label = tkinter.messagebox.showinfo("About", "This is "
                                         "text Editor Created by Mr Priyesh Ranjan.\n"
                                        "He is a final year student of bhagalpur college of enginering \n"
                                         "with an stream of computer Science")



                                    #  MAIN FUNCTION
    def __init__(self,master):
        self.master=master
        master.title("Priyesh Ranjan Singh")

                   #  Text Editor
        self.txt=Text(self.master,undo=True,wrap=WORD)
                   # SCROLL-TEXT
        self.txt=scrolledtext.ScrolledText(master,wrap=WORD)

        self.txt.pack(fill=BOTH,expand=1)

                                       # CREATING OBJECT OF MENU
        self.main_menu=Menu()
        self.master.config(menu=self.main_menu)

                         # CREATING FILE MENU

        self.file=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="File",menu=self.file)
                                       # NEW MENU
        self.file.add_command(label="New            Ctrl+N",command=self.new_file)
                                       # OPEN MENU
        self.file.add_command(label="Open          Ctrl+O",command=self.open_file)
                                       # SEPARATOR
        self.file.add_separator()
                                       # SAVE MENU
        self.file.add_command(label="Save            Ctrl+S",command=self.save_file)
                                       # SAVE-AS MENU
        self.file.add_command(label="Save As",command=self.saveas_file)
                                       # SEPARATOR
        self.file.add_separator()
                                       # EXIT MENU
        self.file.add_command(label="Exit",command=self.custom_exit)

                        # CREATING EDIT MENU

        self.edit= Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Edit",menu=self.edit)
                                       # COPY MENU
        self.edit.add_command(label="Copy            Ctrl+C",command=self.copy_file)
                                       # CUT MENU
        self.edit.add_command(label="Cut               Ctrl+X",command=self.cut_file)
                                       # SEPARATOR
        self.edit.add_separator()
                                       # PASTE MENU
        self.edit.add_command(label="Paste            Ctrl+V",command=self.paste_file)
                                       # SEPARATOR
        self.edit.add_separator()
                                       # UNDO MENU
        self.edit.add_command(label="Undo            Ctrl-Z",command=self.txt.edit_undo)
                                       # REDO MENU
        self.edit.add_command(label="Redo",command=self.txt.edit_redo)

                     #  CREATING FORMAT MENU
        self.format = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Format",menu=self.format)

                                       # CHANGE COLOR
        self.format.add_command(label="Edit background...",command=self.color_change)
                                       # SEPARATOR
        self.format.add_separator()
                                       #  CHANGE FONT
        self.format.add_command(label="Font...")

                     #  CREATING VIEW MENU

        self.view = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="View",menu=self.view)
                                       #  CREATING  DATE/TIME
        self.view.add_command(label="Date/Time",command=self.find_date)
                                       #  CREATING DAY
        self.view.add_command(label="Day",command=self.find_day)
                                       # SEPARATOR
        self.view.add_separator()
                                       #SEARCH WIKIPEDIA
        self.view.add_command(label="Search",command=self.search_text)

                     # CREATING HELP MENU

        self.help = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Help",menu=self.help)
                                       #  HELP
        self.help.add_command(label="View Help",command=self.browse)
                                       #SEPARATOR
        self.help.add_separator()
                                       #  ABOUT
        self.help.add_command(label="About Notepad",command=self.about_command)


                                     # BINDING KEYS

        self.master.bind('<Control-o>',self.open_file)
        self.master.bind('<Control-n>', self.new_file)
        self.master.bind('<Control-s>', self.save_file)
        self.master.bind('<Control-s>', self.saveas_file)
        self.master.bind('<Control-c>', self.copy_file)
        self.master.bind('<Control-x>',self.cut_file)
        self.master.bind('<Control-v>',self.paste_file)
        self.master.bind('<Control-z>',self.txt.edit_undo)




root = Tk()
text=editor(root)
root.mainloop()