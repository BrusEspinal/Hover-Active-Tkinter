from tkinter import Tk, Button

def hoverActive(boton, color1, color2, color3):
	boton.configure(bg=color1)
	def fuera(e):
		boton.configure(bg=color1)
	def dentro(e):
		boton.configure(bg=color2)
	def activo(e):
		boton.configure(activebackground=color3)

	boton.bind("<Enter>", dentro)
	boton.bind("<Leave>", fuera)
	boton.bind("<ButtonPress-1>", activo)

ventana = Tk()
ventana.configure(bd=30), ventana.title("Hover - Active")

boton1 = Button(ventana, width=40, height=4, text="HOVER / ACTIVE", bd=0, fg="#fff", cursor="hand2", command=lambda:None)
boton1.grid(column=0, row=0, pady=7)
hoverActive(boton1, "#4fa8fb", "#ffa43a", "#a9fb50")

boton2 = Button(ventana, width=40, height=4, text="HOVER / ACTIVE", bd=0, fg="#fff", cursor="hand2", command=lambda:None)
boton2.grid(column=0, row=1, pady=7)
hoverActive(boton2, "#f86f6f", "#e3605f", "#fe9393")

boton3 = Button(ventana, width=40, height=4, text="HOVER / ACTIVE", bd=0, fg="#fff", cursor="hand2", command=lambda:None)
boton3.grid(column=0, row=2, pady=7)
hoverActive(boton3, "#ff35c2", "#ea2db0", "#ff7dd8")

ventana.mainloop()

 
