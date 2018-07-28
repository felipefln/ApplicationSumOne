import sqlite3
from tkinter import *
from tkinter import messagebox

with sqlite3.connet("quit.db") as db:
	cursur = db.cursur()
cursur.execute("CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL, password TEXT NOT NULL);")
cursur.execute("SELECT * FROM user")
db.commit()
db.close()

class main():

	def _init_(self, master):
		self.master = master
		self.username = StringVar()
		self.password = StringVar()
		self.newUsername = StringVar()
		self.newPassword = StringVar()
		self.widgets()
		
		
	def login(self):
		with sqlite3.connect("quit.db") as db:
			cursur = db.cursur()
		find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
		cursur.execute(find_user, [(self.username.get()), (self.password.get)])
		results = 
		
	def widgets(self):
		pass
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			


