import turtle

# Configurar la ventana
turtle.bgcolor("yellow")  # Color de fondo
turtle.title("Iniciales A P")

# Configurar la tortuga
t = turtle.Turtle()
t.pensize(7)  # Grosor del trazo
t.speed(1)  # Velocidad de dibujo

# Dibujar la letra "A"
t.color("red")  # Color de la letra A
t.penup()
t.goto(-50, 0)  # Posicionar para la letra A
t.pendown()
t.setheading(75)  # Dirigir hacia arriba
t.forward(100)  # Lado izquierdo de A
t.setheading(-75) 
t.forward(100)  # Lado derecho de A
t.setheading(0)
t.forward(50)  # Barra transversal de A

# Dibujar la letra "P"
t.penup()
t.goto(10, 0)  # Posicionar para la letra P
t.pendown()
t.setheading(90)  # Dirigir hacia arriba
t.forward(100)  # Línea vertical de P
t.setheading(0)
t.circle(-25, 180)  # Media circunferencia para la parte superior de P

# Finalizar
t.hideturtle()  # Ocultar la tortuga
turtle.done()  # Mostrar la ventana