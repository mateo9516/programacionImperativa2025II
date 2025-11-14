import turtle

ventana = turtle.Screen()
lapiz = turtle.Turtle()

def arriba():
    lapiz.setheading(90)
    lapiz.forward(100)

def derecha():
    lapiz.setheading(0)
    lapiz.forward(100)

def izquierda():
    lapiz.setheading(180)
    lapiz.forward(100)

def abajo():
    lapiz.setheading(270)
    lapiz.forward(100)

### Eventos
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

### alistese que van a realizar accion
ventana.listen()

turtle.done()

