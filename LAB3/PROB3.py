import turtle
import math
grosor = 2

# Función para dibujar el círculo
def dibujar_circulo(x, y, radio):
    turtle.color("red")
    turtle.penup()
    turtle.goto(x, y - radio)  # Posiciona la tortuga en la parte inferior del círculo
    turtle.pendown()
    turtle.circle(radio)  # Dibuja el círculo
    turtle.penup()
    turtle.goto(x, y)  # Regresa al centro
    turtle.write(f'Área: {math.pi * radio ** 2:.2f}', align="center")  # Muestra el área

# Solicitar entrada del usuario
x = int(input("Ingrese las coordenadas del centro del círculo (x, y): ").split()[0])
y = int(input("Ingrese las coordenadas del centro del círculo (x, y): ").split()[1])
radio = int(input("Ingrese el radio del círculo: "))

# Configuración de la ventana
turtle.speed(1)  # Velocidad de dibujo
dibujar_circulo(x, y, radio)

turtle.done()  # Finaliza