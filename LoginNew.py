import sqlite3
from tkinter import *
from tkinter import messagebox as ms

with sqlite3.connect("quit.db") as db:
	cursur = db.cursor()
cursur.execute("CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL, password TEXT NOT NULL);")
cursur.execute("SELECT * FROM user")
db.commit()
db.close()

class main():
	def __init__(self, master):
		self.master = master
		self.username = StringVar()
		self.password = StringVar()
		self.newUsername = StringVar()
		self.newPassword = StringVar()
		self.widgets()
		
		
	def login(self):
		with sqlite3.connect("quit.db") as db:
			cursur = db.cursor()
		find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
		cursur.execute(find_user, [(self.username.get()), (self.password.get())])
		results = cursur.fetchall()
		if results:
			self.logf.pack_forget()
			self.head["text"] = self.username.get() + "\nLogado(a)"
			self.head['pady'] = 150
		else:
			ms.showerror("Username não encontrado")
			self.logf()
			
	def new_user(self):
		with sqlite3.connect("quit.db") as db:
			cursur = db.cursor()
		find_user = ("SELECT * FROM user WHERE username = ?")
		cursur.execute(find_user, [(self.username.get())])
		if cursur.fetchall():
			ms.showerror("Ops", "Username já utilizado")
			
		else:
			ms.showinfo("Show", "Login criado")
			self.log()
			
		insert = 'INSERT INTO user(username, password) VALUES(?, ?)'
		cursur.execute(insert, [(self.newUsername.get()), (self.newPassword.get())])
		db.commit()
		
	def log(self):
		self.username.get("")
		self.password.get("")
		self.logf.pack_forget()
		self.head["text"] = "Login"
		self.crf.pack()
		
		
	def cr(self):
		self.newUsername.set("")
		self.newPassword.set("")
		self.logf.pack_forget()
		self.head['text'] = "Conta criada"
		self.crf.pack()
	
		
	def widgets(self):
		self.head = Label(self.master, text="LOGIN", font = ('freesansbold', 35), pady=40)
		self.head.pack()
		
		self.logf = Frame(self.master, padx = 10, pady = 10)
		Label(self.logf, text = "Username", font = ('freesansbold', 15),padx=5,  pady=5).grid(sticky=W)
		Entry(self.logf, textvariable =self.username, bd=8, font= ('calibri',15,'bold')).grid(row=0, column=1, stick=E)
		Label(self.logf, text = "Password", font = ('freesansbold', 15),padx=5,  pady=5).grid(row=1, column=0, sticky=W)
		Entry(self.logf, textvariable =self.password, bd=8, font= ('calibri',15,'bold'),show = "*").grid(row=1, column=1, stick=E)
		Button(self.logf, text= "Login", bd=7, font = ("monaco", 15, 'bold'), padx=5, pady=5, command=self.login).grid(row=2)
		Button(self.logf, text= "   Criar nova conta    ", bd=7, font = ("monaco", 15, 'bold'), padx=5, pady=5, command=self.cr).grid(row=2, column=1)
		self.logf.pack()
		
		self.crf = Frame(self.master, padx = 10, pady = 10)
		Label(self.crf, text = "Username", font = ('freesansbold', 20),padx=5,  pady=5).grid(sticky=W)
		Entry(self.crf, textvariable =self.newUsername, bd=8, font= ('calibri',15,'bold')).grid(row=0, column=1, stick=E)
		Label(self.crf, text = "Password", font = ('freesansbold', 20),padx=5,  pady=5).grid(row=1, column=0, sticky=W)
		Entry(self.crf, textvariable =self.newPassword, bd=8, font= ('calibri',15,'bold'),show = "*").grid(row=1, column=1, stick=E)
		Button(self.crf, text= "Criar conta", bd=7, font = ("monaco", 15, 'bold'), padx=5, pady=5, command=self.log).grid(row=2)
		Button(self.crf, text= "Logar", bd=7, font = ("monaco", 15, 'bold'), padx=5, pady=5, command=self.new_user).grid(row=2, column=1)
		self.logf.pack()
		
		
root = Tk()
main(root)
root.geometry("400x350+350+150")
root.mainloop()