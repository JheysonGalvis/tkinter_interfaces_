import tkinter as tk

ventana = tk.Tk() #La segunda t va en mayúscula

ventana.title("Mi primer ventana")
ventana.geometry("600x400+500+200")
ventana.minsize(400, 200) #Ancho y alto minimos
ventana.maxsize(800, 600) #Ancho y alto maximos
ventana.iconbitmap("perrito.ico")
ventana.configure(bg="lightgreen")
ventana.resizable(False,False) #Horizontal y Vertical
ventana.attributes("-alpha", 0.9)

ventana.mainloop()