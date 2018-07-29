import sqlite3

class books():
	def __init__:
		self.title = title
		self.author = author
		self.year = year
		self.prince = prince

	def connect(self):
		conn=sqlite3.connect("book.db")
		cur.conn.cursor()
		cur.execute("CREATE TABLE IF NOT EXIST book (id INTERGER PRIMARY KEY, title text, author text, year text, prince text"))
		conn.commit()
		conn.close()
		
		
	def insert(self.title,self.author, self.year,self.prince):
		conn=sqlite3.connect("book.db")
		cur=conn.cursor()
		cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, prince))
		conn.commit()
		conn.close()
		
	def view():
		conn=sqlite3.connect("book.db")
		cur=conn.cursor()
		cur.execute("SELEC * FROM book")
		rows=cur.fetchall()
		conn.close()
		return rows
		
	def search(self.title="", self.author="", self.year="", self.prince=""):
		conn=sqlite3.connect("book.db")
		cur=conn.cursor()
		cur.execute("SELEC * FROM book WHERE title=? OR author=? OR year=? or prince=?"(title, author, year, prince))
		rows=cur.fetchall()
		conn.close()
		return rows
		
	def delete(self.id):
		conn=sqlite3.connect("book.db")
		cur=conn.cursor()
		cur.execute("DELETE * FROM book WHERE id = ?,(id))
		conn.close()
		return rows
		
	def update(self.id, self.title, self.author, self.year, self.prince):
		conn=sqlite3.connect("book.db")
		cur=conn.cursor()
		cur.execute("UPDATE book set title=?, author=?, year=?, prince=? WHERE id=?", (title, author, prince, id) )
		conn.commit()
		conn.close()
		return rows
		
		