import turtle

def dibujar_triangulo_isosceles(base, altura):
    
    turtle.penup()
    turtle.goto(-base / 2, 0)  
    turtle.pendown()

    
    turtle.forward(base)  
    turtle.left(110)  
    turtle.forward(altura) 
    turtle.left(145)  
    turtle.forward(altura)  
    turtle.left(120)  

    turtle.done()  

def main():
    
    base = 100  
    altura = 170  

    
    turtle.speed(1) 
    turtle.title("Dibujo de un triángulo isósceles")

    dibujar_triangulo_isosceles(base, altura)
if __name__ == "__main__":
    main()
