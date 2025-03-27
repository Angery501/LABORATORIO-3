import turtle

def dibujar_triangulo_isosceles(base, altura):
    # Calcular la posición inicial
    turtle.penup()
    turtle.goto(-base / 2, 0)  # Mover a la posición inicial
    turtle.pendown()

    # Dibujar el triángulo
    turtle.forward(base)  # Dibujar la base
    turtle.left(110)  # Girar 120 grados
    turtle.forward(altura)  # Dibujar el lado izquierdo
    turtle.left(145)  # Girar 120 grados
    turtle.forward(altura)  # Dibujar el lado derecho
    turtle.left(120)  # Girar 120 grados para volver a la posición inicial

    turtle.done()  # Terminar el dibujo

def main():
    # Definir la base y la altura del triángulo
    base = 100  # Puedes cambiar este valor
    altura = 170  # Puedes cambiar este valor

    # Configurar la tortuga
    turtle.speed(1)  # Velocidad de dibujo
    turtle.title("Dibujo de un triángulo isósceles")

    # Dibujar el triángulo isósceles
    dibujar_triangulo_isosceles(base, altura)

# Ejecutar el programa
if __name__ == "__main__":
    main()