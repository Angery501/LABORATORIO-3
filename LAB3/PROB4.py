import turtle

turtle.bgcolor("yellow") 
turtle.title("Iniciales A P")

t = turtle.Turtle()
t.pensize(7) 
t.speed(1)  

t.color("red") 
t.penup()
t.goto(-50, 0) 
t.pendown()
t.setheading(75)  
t.forward(100)  
t.setheading(-75) 
t.forward(100)  
t.setheading(0)
t.forward(50) 

t.penup()
t.goto(10, 0) 
t.pendown()
t.setheading(90) 
t.forward(100)  
t.setheading(0)
t.circle(-25, 180)  

t.hideturtle()  
turtle.done()  
