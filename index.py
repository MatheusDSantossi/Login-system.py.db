#Importar as bibliotecas

from tkinter import *
from tkinter import messagebox, ttk
import database
#Criar nossa janela

janela = Tk()
janela.title("DP System - Acess Panel")
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width=False, height=False)
janela.attributes("-alpha", 0.9)
janela.iconbitmap(default="icons/LogoIcon.ico")


#===== Carregando Imagens

logo = PhotoImage(file="icons/logo.png")

#==== WIDGETS ========

leftFrame = Frame(janela, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
leftFrame.pack(side=LEFT)

rightFrame = Frame(janela, width=390, height=300, bg="MIDNIGHTBLUE", relief="raise")
rightFrame.pack(side=RIGHT)

logoLabel = Label(leftFrame, image=logo, bg="MIDNIGHTBLUE")
logoLabel.place(x=50, y=100)

userLabel = Label(rightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
userLabel.place(x=5, y=100)

userEntry = ttk.Entry(rightFrame, width=30)
userEntry.place(x=150, y=110)

passLabel = Label(rightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
passLabel.place(x=5, y=150)

passEntry =  ttk.Entry(rightFrame, width=30, show="•­")
passEntry.place(x=150, y=160)

#Botoes

def login():
    user = userEntry.get()
    password = passEntry.get()
    
    database.cursor.execute(""" 
    SELECT * FROM Users
    WHERE (User = ? AND Password = ?)
    """, (user, password))
    print("Selected")
    verifyLogin = database.cursor.fetchone()
    try:

        if(user in verifyLogin and password in verifyLogin):
            messagebox.showinfo(title="Login Info", message="Acess Confirmed, Welcome!")
    except:
        messagebox.showinfo(title="Login Info", message="Acces Denied, Check your informations and try again!")
        
loginButton = ttk.Button(rightFrame, text="Login", width=30, command=login)
loginButton.place(x=100, y=225)

def register():
    #Removendo Widgets de Login
    loginButton.place(x=7000)
    registerButton.place(x=7000)
    #Inserindo Widgets de Cadastro
    nomeLabel = Label(rightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    nomeLabel.place(x=5, y=5)

    nomeEntry = ttk.Entry(rightFrame, width=39)
    nomeEntry.place(x=100, y=17)

    emailLabel = Label(rightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    emailLabel.place(x=5, y=55)

    emailEntry = ttk.Entry(rightFrame, width=39)
    emailEntry.place(x=100, y=66)

    def registerToDataBase():
        name = nomeEntry.get()
        email = emailEntry.get()
        user = userEntry.get()
        password = passEntry.get()

        if(name == "" or email == "" or user == "" or password == ""):
            messagebox.showerror(title="Register Error", message="Fill all of the parameters!")
        else:
            database.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password)  VALUES(?,?,?,?)
            """, (name, email, user, password))
            database.connection.commit()
            
            messagebox.showinfo(title="Register Info", message="Account Created!!")
    
    register = ttk.Button(rightFrame, text="Register", width=30, command=registerToDataBase)
    register.place(x=100, y=225)

    def backToLogin():
        #removendo widgets do cadastro

        nomeLabel.place(x=5000)
        nomeEntry.place(x=5000)
        emailLabel.place(x=5000)
        emailEntry.place(x=5000)
        register.place(x=5000)
        back.place(x=5000)

        #Trazendo de volta os widgets de login

        loginButton.place(x=100)
        registerButton.place(x=125)

    back = ttk.Button(rightFrame, text="Back", width=20, command=backToLogin)
    back.place(x=125, y=260)

registerButton = ttk.Button(rightFrame, text="Register", width=20, command=register)
registerButton.place(x=125, y=260)
 

janela.mainloop()
