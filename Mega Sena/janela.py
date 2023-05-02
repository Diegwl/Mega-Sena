import tkinter.messagebox
from tkinter import ttk
from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from conectar import conexao, cursor
from read import listar_jogos, procurar_jogo
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt

janela = Tk()


class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inserts()
        self.lista()
        self.read_user()
        self.grafico()
        janela.mainloop()

    def tela(self):
        self.janela.title("MEGA SENA")
        self.janela.configure(background="cyan")
        self.janela.geometry("700x800")
        self.janela.resizable(True, True)
        self.janela.minsize(width=700, height=700)



    def frames(self):
        self.frame0 = Frame(self.janela, bg="blue")
        self.frame0.place(relheight=0.07, relwidth=0.94, relx=0.03, rely=0.03)
        self.frame1 = Frame(self.janela, bg="blue")
        self.frame1.place(relheight=0.08, relwidth=0.94, relx=0.03, rely=0.115)
        self.frame2 = Frame(self.janela, bg="blue")
        self.frame2.place(relheight=0.25, relwidth=0.94, relx=0.03, rely=0.21)
        self.frame3 = Frame(self.janela, bg="blue")
        self.frame3.place(relheight=0.45, relwidth=0.94, relx=0.03, rely=0.475)

    def botoes(self):
        self.btJogar = Button(self.frame0, text='Jogar', bg="cyan", command=self.jogar)
        self.btJogar.place(relx=0.69, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btClear = Button(self.frame0, text='Limpar', bg="cyan", command=self.limpar)
        self.btClear.place(relx=0.80, rely=0.40, relwidth=0.1, relheight=0.50)

    def labels(self):
        self.lbDuque = Label(self.frame1, text="Duques", background="cyan")
        self.lbDuque.place(relx=0.05, rely=0.03, relwidth=0.1, relheight=0.40)

        self.lbTerno = Label(self.frame1, text="Ternos", bg="cyan")
        self.lbTerno.place(relx=0.25, rely=0.03, relwidth=0.1, relheight=0.40)

        self.lbQuadra = Label(self.frame1, text="Quadras", bg="cyan")
        self.lbQuadra.place(relx=0.45, rely=0.03, relwidth=0.1, relheight=0.40)

        self.lbQuinta = Label(self.frame1, text="Quinas", bg="cyan")
        self.lbQuinta.place(relx=0.65, rely=0.03, relwidth=0.1, relheight=0.40)

        self.lbMega = Label(self.frame1, text="Megas", bg="cyan")
        self.lbMega.place(relx=0.85, rely=0.03, relwidth=0.1, relheight=0.40)

    def inserts(self):
        self.insertN1 = Entry(self.frame0, background="cyan")
        self.insertN1.place(relx=0.05, rely=0.40, relwidth=0.05, relheight=0.47)

        self.insertN2 = Entry(self.frame0, background="cyan")
        self.insertN2.place(relx=0.15, rely=0.40, relwidth=0.05, relheight=0.47)

        self.insertN3 = Entry(self.frame0, background="cyan")
        self.insertN3.place(relx=0.25, rely=0.40, relwidth=0.05, relheight=0.47)

        self.insertN4 = Entry(self.frame0, background="cyan")
        self.insertN4.place(relx=0.35, rely=0.40, relwidth=0.05, relheight=0.47)

        self.insertN5 = Entry(self.frame0, background="cyan")
        self.insertN5.place(relx=0.45, rely=0.40, relwidth=0.05, relheight=0.47)

        self.insertN6 = Entry(self.frame0, background="cyan")
        self.insertN6.place(relx=0.55, rely=0.40, relwidth=0.05, relheight=0.47)

        self.insertDuque = Entry(self.frame1, bg="cyan")
        self.insertDuque.place(relx=0.05, rely=0.48, relwidth=0.10, relheight=0.33)

        self.insertTerno = Entry(self.frame1, bg="cyan")
        self.insertTerno.place(relx=0.25, rely=0.48, relwidth=0.10, relheight=0.33)

        self.insertQuadra = Entry(self.frame1, bg="cyan")
        self.insertQuadra.place(relx=0.45, rely=0.48, relwidth=0.10, relheight=0.33)

        self.insertQuina = Entry(self.frame1, bg="cyan")
        self.insertQuina.place(relx=0.65, rely=0.48, relwidth=0.10, relheight=0.33)

        self.insertMega = Entry(self.frame1, bg="cyan")
        self.insertMega.place(relx=0.85, rely=0.48, relwidth=0.10, relheight=0.33)

    def lista(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))

        self.listaCli.heading('#0', text='Jogo')
        self.listaCli.heading('#1', text='1º Número')
        self.listaCli.heading('#2', text='2º Número')
        self.listaCli.heading('#3', text='3º Número')
        self.listaCli.heading('#4', text='4º Número')
        self.listaCli.heading('#5', text='5º Número')
        self.listaCli.heading('#6', text='6º Número')

        self.listaCli.column('#0', width=50)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=50)
        self.listaCli.column('#3', width=50)
        self.listaCli.column('#4', width=50)
        self.listaCli.column('#5', width=50)
        self.listaCli.column('#6', width=50)

        self.listaCli.place(relx=0.025, rely=0.075, relwidth=0.925, relheight=0.85)

        self.scrollLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.949, rely=0.079, relwidth=0.02, relheight=0.84)
        self.scrollLista.config(command=self.listaCli.yview)

    def delete_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())

    def read_user(self):
        self.delete_lista()
        linhas = listar_jogos()
        for i in range(len(linhas)):
            self.listaCli.insert(index=i, values=[linhas[i][1], linhas[i][2], linhas[i][3], linhas[i][4], linhas[i][5],
                                                  linhas[i][6]], parent="", text=linhas[i][0])

    def limpar(self):
        self.insertN1.delete(0, END)
        self.insertN2.delete(0, END)
        self.insertN3.delete(0, END)
        self.insertN3.delete(0, END)
        self.insertN4.delete(0, END)
        self.insertN5.delete(0, END)
        self.insertN6.delete(0, END)
        self.insertDuque.delete(0, END)
        self.insertTerno.delete(0, END)
        self.insertQuadra.delete(0, END)
        self.insertQuina.delete(0, END)
        self.insertMega.delete(0, END)

    def grafico(self):
        fig = plt.Figure(figsize=(12, 6), dpi=50)
        ax = fig.add_subplot(111)

        numeros = [n for n in range(1, 61)]

        counts = []

        sql = f"SELECT * from jogos"
        cursor.execute(sql)
        linhas = cursor.fetchall()
        for i in range(1, 61):
            cont = 0
            for linha in linhas:
                for j in range(1, 7):
                    if linha[j] == i:
                        cont += 1
            counts.append(cont)

        ax.bar(numeros, counts)

        ax.set_ylabel('Vezes que foi sorteado')
        ax.set_title('Número de vezes que cada número foi sorteado')

        canva = FigureCanvasTkAgg(fig, self.janela)
        canva.get_tk_widget().place(relx=0.05, rely=0.50)

    def jogar(self):
        self.insertDuque.delete(0, END)
        self.insertTerno.delete(0, END)
        self.insertQuadra.delete(0, END)
        self.insertQuina.delete(0, END)
        self.insertMega.delete(0, END)
        if self.insertN1.get().isnumeric() and self.insertN2.get().isnumeric() and self.insertN3.get().isnumeric() and \
                self.insertN4.get().isnumeric() and self.insertN5.get().isnumeric() and self.insertN6.get().isnumeric():
            n1 = int(self.insertN1.get())
            n2 = int(self.insertN2.get())
            n3 = int(self.insertN3.get())
            n4 = int(self.insertN4.get())
            n5 = int(self.insertN5.get())
            n6 = int(self.insertN6.get())
            if 60 >= n1 >= 1 and 60 >= n2 >= 1 and 60 >= n3 >= 1 and 60 >= n4 >= 1 and 60 >= n5 >= 1 and 60 >= n6 >= 1:
                linhas = procurar_jogo(n1, n2, n3, n4, n5, n6)

                self.insertDuque.insert(0, linhas[0])
                self.insertTerno.insert(0, linhas[1])
                self.insertQuadra.insert(0, linhas[2])
                self.insertQuina.insert(0, linhas[3])
                self.insertMega.insert(0, linhas[4])
                id_mega = linhas[5]
                if id_mega != 0:
                    showinfo(f"Parabéns!", f"Você teria ganho a Mega Sena {id_mega}")
                else:
                    showinfo("Que Triste!", "Infelizmente você não teria ganho a Mega Sena")
            else:
                showinfo("Erro!", "Você deve digitar apenas números entre 1 e 60")
        else:
            showinfo("Erro!", "Você deve digitar apenas números")
