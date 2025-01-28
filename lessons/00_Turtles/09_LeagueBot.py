""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()

def set_turtle_image(image, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()

set_turtle_image(t, "leaguebot_bolt.gif")
t.shapesize(stretch_wid=10, stretch_len=10)
t.fillcolor("blue")
t.pencolor("blue")
t.pendown()
def draw_hexagon(sides, distance):
    angle = 360/sides
    for i in range(sides):
        t.forward(distance)
        t.left(angle)

draw_hexagon(6, 100)

turtle.exitonclick()