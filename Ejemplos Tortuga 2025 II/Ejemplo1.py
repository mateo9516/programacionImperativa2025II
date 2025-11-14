import turtle

### Crear un lienzo
lienzo = turtle.Screen()

### color del fondo del lienzo
lienzo.bgcolor("white")

### declaro la tortuga (lapiz)
tortuga = turtle.Turtle()

### le asigno un color del trazo 
tortuga.color("blue","yellow")

### icono de tortuga
tortuga.shape("turtle")

#### le pongo color de relleno donde identifique un poligono
tortuga.begin_fill()

### Dibujando el cuadrado
for i in range(4):
    tortuga.forward(100)
    tortuga.left(90)

### finaliza el relleno del poligono 

tortuga.penup()
tortuga.goto(100,-100)
tortuga.pendown()

#### pentagono 
for i in range(5):
    tortuga.forward(100)
    tortuga.right(144)
tortuga.end_fill()

### Estrella de israel

### Pentagono al reves? 

### para que la ventana se mantenga abierta
turtle.done()