import turtle
def dibujar_cuadrado():
    turtle.begin_fill()
    turtle.fillcolor("red")
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

def dibujar_triangulo():
    turtle.begin_fill()
    turtle.fillcolor("blue")
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()

def dibujar_circulo():
    turtle.begin_fill()
    turtle.fillcolor("green")
    turtle.circle(50)
    turtle.end_fill()
def dibujar_rombo():
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    for _ in range(2):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)
    turtle.end_fill()

turtle.speed(1)
dibujar_triangulo()
turtle.penup()
turtle.goto(150, 0)
turtle.pendown()
dibujar_cuadrado()
turtle.penup()
turtle.goto(300, 0)  
turtle.pendown()
dibujar_circulo()
turtle.penup()
turtle.goto(450, 0) 
turtle.pendown()
dibujar_rombo()

turtle.done()
