import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.title("Dibujo de Iniciales")
screen.bgcolor("yellow")

# Creación del objeto turtle
t = turtle.Turtle()
t.color("red")
t.pensize(5)

# Función para dibujar la letra N
def draw_N():
    t.goto(-50, 0) 
    t.left(90) # Posicionar el turtle
    t.pendown()
    t.setheading(270)  # Dirección hacia abajo
    t.forward(100)
    t.setheading(0)    # Dirección hacia la derecha
    t.forward(100)
    t.penup()
    

# Función para dibujar la letra L
def draw_L():
    t.goto(30, 0)  # Posicionar el turtle
    t.pendown()
    t.setheading(270)  # Dirección hacia abajo
    t.forward(100)
    t.setheading(0)    # Dirección hacia la derecha
    t.forward(50)
    t.penup()

# Llamar a las funciones para dibujar las letras
draw_N()
draw_L()

# Volver a la posición inicial
t.home()

# Finalizar el dibujo
turtle.done()