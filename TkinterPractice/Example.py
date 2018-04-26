import tkinter
window=tkinter.Tk()
window.geometry("500x200")

def execute():
    entry2.delete(0,tkinter.END)
    entry3.delete(0,tkinter.END)
    entry4.delete(0,tkinter.END)
    #entry3.delete()
    #entry4.delete()
    entry2.insert(0,str(float(variable1.get())*1000.0)[0:9]+' grams')
    entry3.insert(0,str(float(variable1.get())*2.20462)[0:9]+' pounds')
    entry4.insert(0,str(float(variable1.get())*35.274)[0:9]+' ounces')
     
label1=tkinter.Label(window,text='Enter Value?')
label1.grid(row=0,column=2,ipadx=10,ipady=10)

variable1=tkinter.StringVar()
entry1=tkinter.Entry(window,textvariable=variable1)
entry1.grid(row=1,column=2)

label2=tkinter.Label(window,text='kg')
label2.grid(row=1,column=3,sticky=tkinter.W)

button1=tkinter.Button(window,text="Solve",command=execute)
button1.grid(row=2,column=2,padx=10,pady=10)

variable2=tkinter.StringVar()
entry2=tkinter.Entry(window,textvariable=variable2)
entry2.grid(row=3,column=1,padx=10,pady=10)

variable3=tkinter.StringVar()
entry3=tkinter.Entry(window,textvariable=variable3)
entry3.grid(row=3,column=2,padx=10,pady=10)

variable4=tkinter.StringVar()
entry4=tkinter.Entry(window,textvariable=variable4)
entry4.grid(row=3,column=3,padx=10,pady=10)

window.mainloop()
