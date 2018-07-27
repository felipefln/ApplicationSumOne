from tkinter import *
import os
 
users = 'tempfile.temp' # Arquivo para armazenar usuario
 
def Signup(): # Metodo para criar usuário, 
    global pwordE # Variaveis globais sendo declaradas
    global nameE
    global roots
 
    roots = Tk() 
    roots.title('Criar Usuário') 
    intruction = Label(roots, text='Insira suas Informações\n')
    intruction.grid(row=0, column=0, sticky=E) 
 
    nameL = Label(roots, text='Novo Usuário: ') 
    pwordL = Label(roots, text='Nova Senha: ') 
    nameL.grid(row=1, column=0, sticky=W) 
    pwordL.grid(row=2, column=0, sticky=W) 
 
    nameE = Entry(roots)
    pwordE = Entry(roots, show='*')
    nameE.grid(row=1, column=1) 
    pwordE.grid(row=2, column=1)
 
    signupButton = Button(roots, text='Criar', command=FSSignup) 
    signupButton.grid(columnspan=3, sticky=W)
    roots.mainloop() 
 
def FSSignup(): #Metodo que abri, salva e fecha o arquivo users
    with open(users, 'w') as f: 
        f.write(nameE.get()) .
        f.write('\n') 
        f.write(pwordE.get()) 
        f.close() 
 
    roots.destroy() 
    Login() 
 
def Login(): #Metodo para criação da tela Login
    global nameEL
    global pwordEL 
    global rootA
 
    rootA = Tk() 
    rootA.title('Login') 
 
    intruction = Label(rootA, text='Login\n') 
    intruction.grid(sticky=E) 
 
    nameL = Label(rootA, text='Usuário: ')
    pwordL = Label(rootA, text='Senha: ') 
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) 
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Logar no Sistema', command=CheckLogin) 
    loginB.grid(columnspan=2, sticky=W)
 
    rmuser = Button(rootA, text='Excluir Usuário', fg='red', command=DelUser) 
    rmuser.grid(columnspan=2, sticky=W)
    rootA.mainloop()
 
def CheckLogin(): #Metodo 
    with open(users) as f:
        data = f.readlines() 
        uname = data[0].rstrip() 
        pword = data[1].rstrip() 
 
    if nameEL.get() == uname and pwordEL.get() == pword: 
        r = Tk() 
        r.title(':D')
        r.geometry('300x100') 
        rlbl = Label(r, text='\n[+] Usuário Logado')
        rlbl.pack() 
        r.mainloop()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('300x100')
        rlbl = Label(r, text='\n[!] Login Invalido\n')
        rlbl.pack()
        r.mainloop()
 
def DelUser():
    os.remove(users) 
    rootA.destroy() 
    Signup() 
 
if os.path.isfile(users):
    Login()
else:
    Signup()