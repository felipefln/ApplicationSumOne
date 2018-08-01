import sqlite3

def connect():
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS book (id INTERGER PRIMARY KEY, title text, author text, year text, prince text)")
	conn.commit()
	conn.close()
	
	
def insert():
	conn=sqlite3.connect("book.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, prince))
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
	cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? or prince=?"(title, author, year, prince))
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
	cur.execute("UPDATE book set title=?, author=?, year=?, prince=? WHERE id=?", (title, author, prince, id) )
	conn.commit()
	conn.close()
	return rows
		
		