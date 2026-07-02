import tkinter as tk

janela = tk.Tk()

for linha in range(10):
    for coluna in range(10):
        texto = f"({linha},{coluna})"

        x= tk.Label(janela,
                     text = texto,
                     relief="solid",
                     pady=10,
                     padx=10)
         
        x.grid(row=linha, column=coluna)
janela.mainloop()