import turtle
turtle.title("Dibuja flechas")
turtle.speed(3)
grosor = 5
turtle.pensize(grosor)

turtle.color("orange")
turtle.penup()
turtle.goto(50, 50)  
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

turtle.color("green")
turtle.penup()
turtle.goto(20, 210)  
turtle.setheading(180) 
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

turtle.color("blue")
turtle.penup()
turtle.goto(-120, 200)  
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

turtle.color("red")
turtle.penup()
turtle.goto(-85, 37)  
turtle.setheading(0) 
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


turtle.done()
