import python_sudoku_solver
import turtle

# Function to draw a vertical line
def draw_vertical_line(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(360)

# Function to draw a horizontal line
def draw_horizontal_line(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(360)

# Function to draw the entire grid
def draw_grid():
    turtle.speed(0)  # Set the drawing speed to maximum
    turtle.penup()   # Lift the pen up

    turtle.pensize(4)
    # Draw vertical lines
    for i in range(-180, 190, 40):
        draw_vertical_line(i, 180)

    # Draw horizontal lines
    for i in range(-180, 190, 40):
        draw_horizontal_line(-180, i)

# Call the function to execute the code
draw_grid()

turtle.penup()
turtle.goto(-167,142)
for i in range(0,9):
    for j in range(0,9):
        if python_sudoku_solver.grid[i][j] != None:
            turtle.write(python_sudoku_solver.grid[i][j],font=("Arial", 22, "normal"))
        turtle.forward(40)
    turtle.goto(turtle.pos()[0]-360,turtle.pos()[1]-40)
turtle.done()    # Finish drawing