import tkinter as tk

janela = tk.Tk()
janela.geometry("450x350")
A = tk.Label(text="A")
B = tk.Label(text="B")
C = tk.Label(text="C")
D = tk.Label(text="D")
E = tk.Label(text="E")

A.place(x=80, y=35)
B.place(x=360, y=10)
C.place(x=10, y=260)
D.place(x=360, y=300)
E.place(x=180, y=160)

janela.mainloop()