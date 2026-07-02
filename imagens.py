import tkinter as tk

janela = tk.Tk()

sorriso = tk.PhotoImage(file="smiley.png")

titulo = tk.Label(text="Tabela", padx=20,pady=20)
p10 = tk.Label(text="nome:", padx=20, pady=20)
p11 = tk.Label(text="Emily", padx=20, pady=20)
p20 = tk.Label(text="Foto:", padx=20,pady=20)
p21 = tk.Label(image=sorriso)

titulo.grid(row=0,column=0,columnspan=2)
p10.grid(row=1,column=0)
p11.grid(row=1,column=1)
p20.grid(row=2,column=0)
p21.grid(row=2,column=1)

janela.mainloop()
