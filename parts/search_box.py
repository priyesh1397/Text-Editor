from tkinter import  *
import wikipedia
root=Tk()
def entry_kk():
    ans=entry.get()
    text.delete(1.0,END)
    try:
      detl=wikipedia.summary(ans)
      text.insert(INSERT,detl)
    except:
      text.insert(INSERT,"Please insert correct input or check input connection")
topframe=Frame(root)
topframe.pack(side=TOP)

entry=Entry(topframe)
entry.pack()
bttn=Button(topframe,text="Search",command=entry_kk)
bttn.pack()

bttmframe=Frame(root)
scroll=Scrollbar(bttmframe)
scroll.pack(side=RIGHT,fill=Y)
text=Text(bttmframe,width=50,height=30,yscrollcommand=scroll.set,wrap=WORD)
scroll.config(command=text.yview())
text.pack()
bttmframe.pack()

root.mainloop()





































































































































































