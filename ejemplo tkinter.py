import tkinter as tk
import turtle
import random

def setup_turtle_for_drawing():
    """Prepara a la tortuga para dibujar una nueva figura."""
    turtle_screen.penup()
    
    # Usamos las dimensiones del lienzo para el posicionamiento aleatorio
    canvas_width = 580
    canvas_height = 500
    try:
        # Intenta obtener el tamaño real del lienzo
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
    except tk.TclError:
        # Usa valores por defecto si la ventana no está lista
        pass 

    margin = 50
    x = random.randint(-canvas_width // 2 + margin, canvas_width // 2 - margin)
    y = random.randint(-canvas_height // 2 + margin, canvas_height // 2 - margin)
    turtle_screen.goto(x, y)

    # Color aleatorio
    r = random.random()
    g = random.random()
    b = random.random()
    turtle_screen.pencolor(r, g, b)
    turtle_screen.fillcolor(r, g, b)
    turtle_screen.pendown()
    
def draw_circle():
    """Dibuja un círculo con radio aleatorio."""
    setup_turtle_for_drawing()
    turtle_screen.begin_fill()
    turtle_screen.circle(random.randint(20, 50))
    turtle_screen.end_fill()

def draw_square():
    """Dibuja un cuadrado con lado de tamaño aleatorio."""
    setup_turtle_for_drawing()
    side = random.randint(40, 100)
    turtle_screen.begin_fill()
    for _ in range(4):
        turtle_screen.forward(side)
        turtle_screen.right(90)
    turtle_screen.end_fill()

def draw_triangle():
    """Dibuja un triángulo equilátero con lado de tamaño aleatorio."""
    setup_turtle_for_drawing()
    side = random.randint(40, 100)
    turtle_screen.begin_fill()
    for _ in range(3):
        turtle_screen.forward(side)
        turtle_screen.left(120)
    turtle_screen.end_fill()

def clear_canvas():
    """Limpia el lienzo de la tortuga."""
    turtle_screen.clear()

# --- Configuración de la GUI ---
ventana = tk.Tk()
ventana.title("Dibujando Figuras con Turtle")
ventana.geometry('600x600')

# Lienzo para la tortuga
canvas = tk.Canvas(ventana)
## Hace que el lienzo se expanda para llenar todo el espacio disponible en la ventana, tanto horizontal como verticalmente.
## expand=True: Hace que el lienzo se expanda para llenar todo el espacio disponible en la ventana, tanto horizontal como verticalmente.
## padx=5, pady=5: Agrega un margen de 5 píxeles entre el lienzo y los bordes de la ventana.
canvas.pack(fill="both", expand=True, padx=5, pady=5)

# Configuración de la pantalla de tortuga en el lienzo
turtle_screen = turtle.RawTurtle(canvas)
turtle_screen.speed("fastest")

# Frame para los botones
button_frame = tk.Frame(ventana)
## side="bottom": Posiciona el frame en la parte inferior de la ventana.
## pady=10: Agrega un margen de 10 píxeles entre el frame y los bordes de la ventana.
button_frame.pack(side="bottom", pady=10)

# Botones
circle_button = tk.Button(button_frame, text="Círculo", command=draw_circle)

circle_button.grid(row=0, column=0, padx=5)

square_button = tk.Button(button_frame, text="Cuadrado", command=draw_square)
square_button.grid(row=0, column=1, padx=5)

triangle_button = tk.Button(button_frame, text="Triángulo", command=draw_triangle)
triangle_button.grid(row=0, column=2, padx=5)

clear_button = tk.Button(button_frame, text="Limpiar", command=clear_canvas)
clear_button.grid(row=0, column=3, padx=5)

# --- Bucle principal de la ventana ---
ventana.mainloop()