#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:34:57 2018

@author: iknownothing
"""

import sqlite3,sys


def create():
    db=sqlite3.connect("book.db")
    cur=db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY,title TEXT,year INTEGER,author TEXT,isbn INTEGER)")
    db.commit()
    db.close()
    print('Successfull')
    

def insert(title,year,author,isbn):
    create() 
    db=sqlite3.connect("book.db")
    cur=db.cursor()
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,year,author,isbn))    
    db.commit()
    db.close()
    viewAll()

def update(id,title,year,author,isbn):
    create() 
    db=sqlite3.connect("book.db")
    cur=db.cursor()
    cur.execute("UPDATE books SET title=?,year=?,author=?,isbn=? WHERE id=?",(title,year,author,isbn,id))
    db.commit()
    db.close()
    

def viewAll():
    create() 
    db=sqlite3.connect("book.db")
    cur=db.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()
    db.close()
    print(rows)
    return rows

def delete(id):
    create() 
    db=sqlite3.connect("book.db")
    cur=db.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id,))
    db.commit()
    db.close()
    

def searchEntry(title="",year="",author="",isbn=""):
    create() 
    db=sqlite3.connect("book.db")
    cur=db.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR year=? OR author=? OR isbn=?",(title,year,author,isbn))
    rows=cur.fetchall()
    db.close()    
    return rows

def exit():
        sys.exit(1)
       