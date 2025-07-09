import turtle

turtle.speed(1)
turtle.forward(100)    # Move forward 100 pixels
turtle.right(90)       # Turn right 90 degrees
turtle.forward(100)

turtle.penup()         # Lift pen (no drawing)
turtle.goto(-100, 100) # Move to new position
turtle.pendown()       # Put pen back down
turtle.forward(50)

turtle.color("black", "red")  # Pen color (outline), Fill color
turtle.begin_fill()           # Start filling
turtle.circle(30)             # Draw a circle
turtle.end_fill()             # Stop filling

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.color("black", "green")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()




turtle.done()