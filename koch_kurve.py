import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

# Beispielaufruf
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-150, 0)
t.pendown()
koch_curve(t, 3, 300)
screen.exitonclick()
