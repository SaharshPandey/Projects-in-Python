from tkinter import *
def kms_to_miles():
    miles=float(entryvalue.get())*1.6
    text.insert(END,miles)
window=Tk()
#Tk.aspect( window,minNumer=30, minDenom=80, maxNumer=80, maxDenom=20)

button=Button(window,text="Find",command=kms_to_miles)
button.grid(column=0,row=0)

entryvalue=StringVar()
entry=Entry(window,textvariable=entryvalue,width=8)
entry.grid(row=0,column=1)

text=Text(window,height=1,width=8)
text.grid(row=1,column=0)
window.mainloop()
