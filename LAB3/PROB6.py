import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Función para dibujar una casa
def draw_house():
    turtle.penup()
    turtle.goto(-50, -30)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

    turtle.color("red")
    turtle.begin_fill()
    turtle.goto(0, 20)
    turtle.goto(50, -30)
    turtle.goto(-50, -30)
    turtle.end_fill()

# Función para dibujar el árbol
def draw_tree():
    turtle.penup()
    turtle.goto(-100, -30)
    turtle.pendown()
    turtle.color("saddle brown")
    turtle.begin_fill()
    turtle.goto(-100, -50)
    turtle.goto(-90, -50)
    turtle.goto(-90, -30)
    turtle.end_fill()

    turtle.color("forest green")
    turtle.begin_fill()
    turtle.goto(-120, -30)
    turtle.goto(-80, -30)
    turtle.goto(-100, 30)
    turtle.goto(-120, -30)
    turtle.end_fill()

# Función para dibujar un coche
def draw_car():
    turtle.penup()
    turtle.goto(100, -50)
    turtle.pendown()
    turtle.color("orange")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(30)
        turtle.left(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(110, -50)
    turtle.pendown()
    turtle.color("black")
    turtle.circle(10)

    turtle.penup()
    turtle.goto(140, -50)
    turtle.pendown()
    turtle.circle(10)

# Función para dibujar el semáforo
def draw_traffic_light():
    turtle.penup()
    turtle.goto(80, 0)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
    turtle.end_fill()

    turtle.goto(80, 50)
    turtle.color("green")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

# Llamadas a las funciones
draw_house()
draw_tree()
draw_car()
draw_traffic_light()

# Ocultar la tortuga y finalizar
turtle.hideturtle()
turtle.done()