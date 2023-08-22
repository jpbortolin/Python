from tkinter import *

def impDados():
    print ("Nome =", txtnome.get())
    print ("Telefone =", txttelefone.get())
    print ("Email =", txtemail.get())
    print ("Obs =", txtobs.get("1.0", END))
    
app = Tk()

app.title("Aula Python")
app.geometry("500x300")
app.configure(background='#dde')

lblnome = Label(app, text="Nome", background="#dde", foreground= '#000')
lblnome.place(x=0, y=0, width=100, height=20)
txtnome = Entry(app)
txtnome.place(x=40, y=25, width=200, height=20)

lbltelefone = Label(app, text="Telefone", background="#dde", foreground= '#000')
lbltelefone.place(x=0, y=50, width=100, height=20)
txttelefone = Entry(app)
txttelefone.place(x=40, y=70, width=200, height=20)

lblemail = Label(app, text="Email", background="#dde", foreground= '#000')
lblemail.place(x=0, y=100, width=100, height=20)
txtemail = Entry(app)
txtemail.place(x=40, y=120, width=200, height=20)

lblobs = Label(app, text="Obs", background="#dde", foreground= '#000')
lblobs.place(x=0, y=170, width=100, height=20)
txtobs = Text(app)
txtobs.place(x=10, y=190, width=300, height=20)

btnImp = Button(app, text="Imprimir", command=impDados)
btnImp.place(x=10, y=270, width=100, height=20)

app.mainloop()