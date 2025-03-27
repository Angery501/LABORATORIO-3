import turtle
import math
grosor = 2

def dibujar_circulo(x, y, radio):
    turtle.color("red")
    turtle.penup()
    turtle.goto(x, y - radio)  
    turtle.pendown()
    turtle.circle(radio)  
    turtle.penup()
    turtle.goto(x, y)  
    turtle.write(f'Área: {math.pi * radio ** 2:.2f}', align="center")  

x = int(input("Ingrese las coordenadas del centro del círculo (x, y): ").split()[0])
y = int(input("Ingrese las coordenadas del centro del círculo (x, y): ").split()[1])
radio = int(input("Ingrese el radio del círculo: "))

turtle.speed(1)  
dibujar_circulo(x, y, radio)

turtle.done() 
