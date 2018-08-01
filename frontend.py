from tkinter import *
import sqlite3

def connect():
	self.title = ''
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS book (id INTERGER PRIMARY KEY, title_text, author_text, year_text, prince_text)")
	conn.commit()
	conn.close()
	
	
def insert():
	conn=sqlite3.connect( "book.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title_text, author_text, year_text, prince_text))
	conn.commit()
	conn.close()

	
def view():
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM book")
	rows=cur.fetchall()
	conn.close()
	return rows
	
def search():
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? or prince=?"(title_text, author_text, year_text, prince_text))
	rows=cur.fetchall()
	conn.close()
	return rows
	
def delete():
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("DELETE * FROM book WHERE id = ?,(id)")
	conn.close()
	return rows
	
def update():
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("UPDATE book set title_text=?, author_text=?, year_text=?, prince_text=? WHERE id=?", (title_text, author_text, year_text, prince_text, id) )
	conn.commit()
	conn.close()
	return rows


window=Tk()

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="Prince")
l4.grid(row=1, column=2)


title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

prince_text=StringVar()
e4=Entry(window, textvariable=prince_text)
e4.grid(row=1, column=3)


list1=Listbox(window, height=10, width=40)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window, text="View All", width=12, command=view)
b1.grid(row=2,column=3)

b2=Button(window, text="Search Entry", width=12, command=search)
b2.grid(row=3,column=3)

b3=Button(window, text="Add Entry", width=12, command=insert)
b3.grid(row=4,column=3)

b4=Button(window, text="Update Selected", width=12, command=update)
b4.grid(row=5,column=3)

b5=Button(window, text="Delete Selected", width=12, command=delete)
b5.grid(row=6,column=3)

b6=Button(window, text="View All", width=12, command=view)
b6.grid(row=7,column=3)

window.geometry("400x300")
window.mainloop()
