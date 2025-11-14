#from tkinter import * ### vamos a importar todo lo que tiene la libreria
import tkinter

### creando el entorno de la GUI
ventana = tkinter.Tk()

### titulo de la ventana
ventana.title('Mi primera ventana')

### Ajusto el tamaño de la ventana
ventana.geometry("400x400")

### etiquetas/labels
texto = tkinter.Label(ventana, text="Esta es mi primera ventana")

### ubicar la ventana en una rejilla 
texto.grid(row=2,column=2,sticky="nsew")

### para que mantenga la ventana abierta
ventana.mainloop()


