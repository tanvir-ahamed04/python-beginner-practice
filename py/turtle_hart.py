import turtle as t

# Function to draw heart shape
def draw_heart():
    t.fillcolor('red')
    t.begin_fill()
    t.left(140)
    t.forward(224)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.forward(224)
    t.end_fill()

# Function to draw a boy
def draw_boy():
    # Head
    t.fillcolor('blue')
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    # Eyes
    t.penup()
    t.goto(-20, 20)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    t.penup()
    t.goto(20, 20)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    # Nose
    t.penup()
    t.goto(0, 10)
    t.pendown()
    t.setheading(270)
    t.forward(10)
    t.setheading(0)

    # Body
    t.penup()
    t.goto(0, -30)
    t.pendown()
    t.setheading(270)
    t.forward(60)

    # Arms
    t.penup()
    t.goto(0, -30)
    t.pendown()
    t.setheading(225)
    t.forward(30)

    t.penup()
    t.goto(0, -30)
    t.pendown()
    t.setheading(315)
    t.forward(30)

    # Legs
    t.penup()
    t.goto(0, -90)
    t.pendown()
    t.setheading(270)
    t.forward(30)

    t.penup()
    t.goto(0, -90)
    t.pendown()
    t.setheading(240)
    t.forward(20)

    t.penup()
    t.goto(0, -90)
    t.pendown()
    t.setheading(300)
    t.forward(20)

# Function to draw a girl
def draw_girl():
    # Head
    t.fillcolor('pink')
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    # Eyes
    t.penup()
    t.goto(-20, 20)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    t.penup()
    t.goto(20, 20)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    # Nose
    t.penup()
    t.goto(0, 10)
    t.pendown()
    t.setheading(270)
    t.forward(10)
    t.setheading(0)

    # Body
    t.penup()
    t.goto(0, -30)
    t.pendown()
    t.setheading(270)
    t.forward(60)

    # Arms
    t.penup()
    t.goto(0, -30)
    t.pendown()
    t.setheading(225)
    t.forward(30)

    t.penup()
    t.goto(0, -30)
    t.pendown()
    t.setheading(315)
    t.forward(30)

    # Legs
    t.penup()
    t.goto(0, -90)
    t.pendown()
    t.setheading(270)
    t.forward(30)

    t.penup()
    t.goto(0, -90)
    t.pendown()
    t.setheading(240)
    t.forward(20)

    t.penup()
    t.goto(0, -90)
    t.pendown()
    t.setheading(300)
    t.forward(20)

# Initialize Turtle
t.speed(1)
t.penup()
t.goto(-150, 0)  # Position for the heart
t.pendown()

# Draw heart shape
draw_heart()

# Draw boy
t.penup()
t.goto(-100, -150)  # Position for the boy
t.pendown()
draw_boy()

# Draw girl
t.penup()
t.goto(50, -150)  # Position for the girl
t.pendown()
draw_girl()

# Display message
t.penup()
t.goto(-200, 200)
t.write("hello - ?", font=("Arial", 16, "normal"))

# Hide turtle and display the result
t.hideturtle()
t.done()
