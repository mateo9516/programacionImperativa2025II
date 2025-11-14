import turtle

## crear el lienzo
ventana = turtle.Screen()

ventana.bgcolor("white")
tortuga = turtle.Turtle()

tortuga.color("blue")
## coloreo donde identifique un poligono
tortuga.begin_fill()
for i in range(4):
    tortuga.forward(100)
    tortuga.left(90)
tortuga.end_fill() 
### 

tortuga.penup()
tortuga.goto(80,-40)
tortuga.pendown()

for i in range(5):
    tortuga.forward(100)
    tortuga.right(144)

### Para que la ventana se mantenga abierta
turtle.done()




