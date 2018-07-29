import sqlite3

def connect():
	conn=sqlite3.connect("books.db")
	cur.conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXIST book (id INTERGER PRIMARY KEY, title text, author text, year text, prince text"))
	conn.commit()
	conn.close()
	
	
def insert(title, author, year, prince):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, prince))
	conn.commit()
	conn.close()
	
def view():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELEC * FROM books")
	rows=cur.fetchall()
	conn.close()
	return rows
	
def search(title="", author="", year="", prince=""):
	
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("SELEC * FROM book WHERE title=? OR author=? OR year=? or prince=?"(title, author, year, prince))
	rows=cur.fetchall()
	conn.close()
	return rows
	
def delete(id):
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("DELETE * FROM book WHERE id = ?,(id))
	conn.close()
	return rows
	
def update(id, title, author, year, prince):
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("UPDATE book set title=?, author=?, year=?, prince=? WHERE id=?", (title, author, prince, id) )
	conn.commit()
	conn.close()
	return rows
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	