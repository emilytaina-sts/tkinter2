import tkinter as tk

janela = tk.Tk()
janela.geometry("350x250")

sorriso = tk.PhotoImage(file="smiley.png")
titulo = tk.Label(text="Imagens!", pady=30)
titulo.config(font=["Arial",12,"bold",])
img1=tk.Label(text="figura 1",
              image=sorriso,
              compound="bottom",
              pady=30,
              padx=10)

img2=tk.Label(text="figura 2",
              image=sorriso,
              compound="top",
              pady=30,
              padx=60)

img3=tk.Label(text="figura 3",
               image=sorriso,
               compound="center",
               padx=30)


titulo.grid(row=0,column=1,)
img1.grid(row=3, column=0)
img2.grid(row=3, column=1)
img3.grid(row=3, column=2)
janela.mainloop()