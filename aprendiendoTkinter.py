import tkinter

# ventana simple
ventana = tkinter.Tk()
ventana.geometry("500x300")  # geometry ayda en dar tamaño a la venta
# poner etiquet o texto
etiqueta = tkinter.Label(ventana, text="aprendiendo en python", bg="blue")
etiqueta.pack(side=tkinter.BOTTOM)
# funcion para el boton
def saludo():
    print("mensaje desde la funcion")


# boton
boton1 = tkinter.Button(
    ventana, text="presina", padx=40, pady=60, bg="grey", command=saludo
)
boton1.pack()

# caja de texto
cajaTexto = tkinter.Entry(
    ventana, font="poppins 20"
)  # para el estilo de la fuente de letra
cajaTexto.pack()

# registro de los succesos en este caso la ventana
ventana.mainloop()
