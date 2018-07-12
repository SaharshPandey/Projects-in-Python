#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 00:52:12 2018

@author: iknownothing
"""

from tkinter import *
import backend
root=Tk()
root.wm_title("BookStore")

def get_row_selected(event):
    try:
        global selected_tuple
        index=listbox.curselection()[0]
        selected_tuple=listbox.get(index)
        titleEntry.delete(0,END)
        titleEntry.insert(END,selected_tuple[1])
    except IndexError:
        pass
    
    
    authorEntry.delete(0,END)
    authorEntry.insert(END,selected_tuple[3])
    
    yearEntry.delete(0,END)
    yearEntry.insert(END,selected_tuple[2])
    
    isbnEntry.delete(0,END)
    isbnEntry.insert(END,selected_tuple[4])

def viewCommand():
    listbox.delete(0,END)
    for row in backend.viewAll():
        listbox.insert(END,row)
    
def searchCommand():
    listbox.delete(0,END)
    for i in backend.searchEntry(titleEntry.get(),yearEntry.get()
    ,authorEntry.get(),isbnEntry.get()):
        listbox.insert(END,i)                                                                 

def insertCommand():
    backend.insert(titleEntry.get(),yearEntry.get()
    ,authorEntry.get(),isbnEntry.get())
    
    listbox.delete(0,END)
    
    listbox.insert(END,(titleEntry.get(),yearEntry.get()
    ,authorEntry.get(),isbnEntry.get()))
  
def updateCommand():
    backend.update(selected_tuple[0],titleEntry.get(),yearEntry.get()
    ,authorEntry.get(),isbnEntry.get())
    viewCommand()

def deleteCommand():
    backend.delete(selected_tuple[0])
    viewCommand()
    


title=Label(root,text="Title")
title.grid(row=0,column=0)

author=Label(root,text="Author")
author.grid(row=0,column=2)

year=Label(root,text="Year")
year.grid(row=1,column=0)

isbn=Label(root,text="ISBN")
isbn.grid(row=1,column=2)

titleString=StringVar()
titleEntry=Entry(root,textvariable=titleString)
titleEntry.grid(row=0,column=1)

authorString=StringVar()
authorEntry=Entry(root,textvariable=authorString)
authorEntry.grid(row=0,column=3)

yearString=StringVar()
yearEntry=Entry(root,textvariable=yearString)
yearEntry.grid(row=1,column=1)

isbnString=StringVar()
isbnEntry=Entry(root,textvariable=isbnString)
isbnEntry.grid(row=1,column=3)

listbox=Listbox(root,height=6,width=35)
listbox.grid(row=2,column=0,rowspan=6,columnspan=2)

scrollbar=Scrollbar(root)
scrollbar.grid(row=2,column=2,rowspan=6)

listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>',get_row_selected)

b1=Button(root,text="View all",width=12,command=viewCommand)
b1.grid(row=2,column=3)

b2=Button(root,text="Search Entry",width=12,command=searchCommand)
b2.grid(row=3,column=3)

b3=Button(root,text="Add Entry",width=12,command=insertCommand)
b3.grid(row=4,column=3)

b4=Button(root,text="Update",width=12,command=updateCommand)
b4.grid(row=5,column=3)

b5=Button(root,text="Delete",width=12,command=deleteCommand)
b5.grid(row=6,column=3)

b6=Button(root,text="Close",width=12,command=root.destroy)
b6.grid(row=7,column=3)
root.mainloop()
