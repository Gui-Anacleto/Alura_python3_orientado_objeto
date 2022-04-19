from funcs import Funcs
from tkinter import *
from tkinter import ttk

root = Tk()
class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.limpa_tela()
        self.montaTabelas()
        self.select_lista()
        self.menus()
        root.mainloop()

    def tela(self):
        self.root.title("Principal")
        self.root.resizable(False, False)
        self.root.geometry("700x500")
        self.root.resizable(True,True)
        self.root.configure(background = "");
        self.root.maxsize(width= 900, height=700)
        self.root.minsize(width= 500, height=400)
        
    def frame_da_tela(self):
        self.frame1 = Frame(self.root, bd=4, highlightbackground="#6495ED", highlightthickness=2)
        self.frame1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bd=4, highlightbackground="#6495ED", highlightthickness=2)
        self.frame2.place(relx=0.02 , rely=0.5, relwidth=0.96, relheight=0.46)
        
    def widgets_frame1(self):
        self.bt_limpar = Button(self.frame1, text="Limpar", bd=2, bg="#DCDCDC" , fg = "Black" , font =("Arial", 11), command= self.limpa_tela)
        self.bt_limpar.place(relx = 0.2, rely=0.1, relwidth=0.1 , relheight=0.15)
        
        self.bt_buscar = Button(self.frame1, text="Buscar", bd=2, bg="#DCDCDC" , fg = "Black" , font =("Arial", 11), command= self.busca_Cliente)
        self.bt_buscar.place(relx = 0.3, rely=0.1, relwidth=0.1 , relheight=0.15)

        self.bt_novo = Button(self.frame1, text="Novo", bd=2, bg="#DCDCDC" , fg = "Black" , font =("Arial", 11) , command=self.add_Cliente)
        self.bt_novo.place(relx = 0.5, rely=0.1, relwidth=0.1 , relheight=0.15)
       
        self.bt_alterar = Button(self.frame1, text="Alterar", bd=2, bg="#DCDCDC" , fg = "Black" , font =("Arial", 11), command= self.alterar_cliete)
        self.bt_alterar.place(relx = 0.6, rely=0.1, relwidth=0.1 , relheight=0.15)

        self.bt_apagar = Button(self.frame1, text="Apagar", bd=2, bg="#DCDCDC" , fg = "Black" , font =("Arial", 11), command=self.deleta_cliente)
        self.bt_apagar.place(relx = 0.7, rely=0.1, relwidth=0.1 , relheight=0.15)

        self.lb_cod = Label(self.frame1, text="Código", fg = "Black" , font =("Arial", 11))
        self.lb_cod.place(relx = 0.05, rely=0.05)

        self.cod = Entry(self.frame1, bg="lightgray", font=("Arial", 10, "bold"))
        self.cod.place(relx = 0.04, rely=0.15,relwidth=0.11)

        self.lb_nome = Label(self.frame1, text="Nome", fg = "Black" , font =("Arial", 11))
        self.lb_nome.place(relx = 0.05, rely=0.35)

        self.nome = Entry(self.frame1)
        self.nome.place(relx = 0.04, rely=0.45,relwidth=0.86)

        self.lb_Telefone = Label(self.frame1, text="Telefone",fg = "Black" , font =("Arial", 11))
        self.lb_Telefone.place(relx = 0.05, rely=0.6)

        self.telefone = Entry(self.frame1)
        self.telefone.place(relx = 0.04, rely=0.7,relwidth=0.4)

        self.lb_Cidade = Label(self.frame1, text="Cidade",fg = "Black" , font =("Arial", 11))
        self.lb_Cidade.place(relx = 0.5, rely=0.6)

        self.cidade = Entry(self.frame1)
        self.cidade.place(relx = 0.5, rely=0.7,relwidth=0.4)

    def lista_frame2(self):

        self.listaCli = ttk.Treeview(self.frame2, height=3, column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx = 0.01, rely=0.1, relwidth=0.95 , relheight=0.85)

        self.scrooLista = Scrollbar(self.frame2, orient="vertical")
        self.listaCli.configure(yscroll=self.scrooLista.set)
        self.scrooLista.place(relx=0.96, rely=0.1 , relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()
        menubar.add_cascade(label="Opções", menu= filemenu)
        menubar.add_cascade(label="Sobre", menu= filemenu2)

        filemenu.add_cascade(label="Sair", command=Quit)
        filemenu2.add_cascade(label="Limpa Cliente", command=self.limpa_tela)

Application()