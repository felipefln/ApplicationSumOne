from tkinter import *

window=Tk()

l1 = Label(window, tex="Title")
l1.grid(row=0, column=0)

l2 = Label(window, tex="Author")
l2.grid(row=0, column=2)

l3 = Label(window, tex="Year")
l3.grid(row=1, column=0)

l4 = Label(window, tex="ISBN")
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

isbn_text=StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)


list1=ListBox(windows, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=1,rowspan=6)

list1.configure(yscrollcomand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window, text="View All", width=12)
b1.grid(row=2,column=3)

b1=Button(window, text="Search Entry", width=12)
b1.grid(row=3,column=3)

b1=Button(window, text="Add Entry", width=12)
b1.grid(row=4,column=3)

b1=Button(window, text="Update Selected", width=12)
b1.grid(row=5,column=3)

b1=Button(window, text="Delete Selected", width=12)
b1.grid(row=6,column=3)

b1=Button(window, text="View All", width=12)
b1.grid(row=7,column=3)

















































