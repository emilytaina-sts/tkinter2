import tkinter as tk

janela = tk.Tk()
janela.geometry("155x180")
titulo= tk.Label(text="Tabela",
                 relief="solid",
                 pady=20,
                 padx=20)

letraA= tk.Label(text="A",
            pady=20,
            padx=20,
            relief="solid")
letraB= tk.Label(text="B",
            pady=20,
            padx=20,
            relief="solid")
letraC= tk.Label(text="C",
            pady=20,
            padx=20,
            relief="solid")
letraD= tk.Label(text="D",
            pady=20,
            padx=20,
            relief="solid")

letraA.grid(row=2, column=0, rowspan=2)
titulo.grid(row=0, column=0,columnspan=3)
letraB.grid(row=2,column=1)
letraC.grid(row=2,column=2)
letraD.grid(row=3,column=1, columnspan=2)


janela.mainloop()