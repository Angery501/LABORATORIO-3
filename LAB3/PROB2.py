import turtle

# Crear una ventana
turtle.title("Dibuja flechas")
turtle.speed(3)

# Definir el grosor de las flechas
grosor = 5
turtle.pensize(grosor)

# Dibuja la flecha hacia arriba (naranja, en la parte superior derecha)
turtle.color("orange")
turtle.penup()
turtle.goto(50, 50)  # Posiciona la flecha
turtle.setheading(90)
turtle.pendown()
turtle.forward(150)
turtle.right(135)
turtle.forward(20)
turtle.backward(20)
turtle.left(270)
turtle.forward(20)
turtle.backward(20)
turtle.right(135)
turtle.backward(50)

# Dibuja la flecha hacia la izquierda
turtle.color("green")
turtle.penup()
turtle.goto(20, 210)  # Posiciona la flecha
turtle.setheading(180)  # Apunta a la izquierda
turtle.pendown()
turtle.forward(120)
turtle.right(135)
turtle.forward(20)
turtle.backward(20)
turtle.left(270)
turtle.forward(20)
turtle.backward(20)
turtle.right(135)
turtle.backward(50)
# Dibuja la flecha hacia abajo (azul, en la parte inferior izquierda)
turtle.color("blue")
turtle.penup()
turtle.goto(-120, 200)  # Posiciona la flecha
turtle.setheading(270)
turtle.pendown()
turtle.forward(150)
turtle.right(135)
turtle.forward(20)
turtle.backward(20)
turtle.left(270)
turtle.forward(20)
turtle.backward(20)
turtle.right(135)
turtle.backward(50)

# Dibuja la flecha hacia la izquierda (roja, en la parte superior izquierda)
turtle.color("red")
turtle.penup()
turtle.goto(-85, 37)  # Posición de la flecha
turtle.setheading(0)  # Apunta hacia la derecha
turtle.pendown()
turtle.forward(120)  # Dibuja la línea principal de la flecha
turtle.right(135)     # Rote hacia la izquierda para hacer la flecha
turtle.forward(20)   # Dibuja la punta de la flecha
turtle.backward(20)  # Regresa a la línea principal
turtle.left(270)     # Rote hacia la izquierda
turtle.forward(20)   # Dibuja la otra punta de la flecha
turtle.backward(20)  # Regresa
turtle.right(135)    # Rote hacia la derecha
turtle.backward(50)  # Vuelve hacia atrás para finalizar

# Terminar
turtle.done()