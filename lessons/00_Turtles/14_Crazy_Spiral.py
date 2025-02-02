"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""

... # Copy code to make a turtle and set up the window
import random
import turtle
t = turtle.Turtle() # Create a turtle named t
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["pink", "blue", "red", "yellow", "orange"]


def getNextColor(i):
    return colors[i % len(colors)]


t.shape("turtle") 

t.width(2) 

t.speed(0) 

for i in range(25):
    t.pencolor(getRandomColor())

    t.fillcolor(getRandomColor()) 
   
    t.begin_fill()

    t.forward(40) 

    t.right(45) 

    t.forward(20) 

    t.right(30) 

    t.forward(20) 

    t.left(30) 

    t.forward(20) 
    t.right(20)
    t.forward(20)
    t.right(10)
    t.forward(10)
    t.end_fill()

t.hideturtle() 

turtle.done() 


# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.
import random
import turtle
t = turtle.Turtle() # Create a turtle named t
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["pink", "blue", "red", "yellow", "orange"]


def getNextColor(i):
    return colors[i % len(colors)]


t.shape("turtle") 

t.width(2) 

t.speed(0)  
def make_a_shape(t):
    """Make a shape with turtle t. Make it go left or right or forward"""    
    for i in range(25):
        t.pencolor(getRandomColor())

        t.fillcolor(getRandomColor()) 
   
        t.begin_fill()

        t.forward(40) 

        t.right(45) 

        t.forward(20) 

        t.right(30) 

        t.forward(20) 

        t.left(30) 

        t.forward(20) 
        t.right(20)
        t.forward(20)
        t.right(10)
        t.forward(10)
        t.end_fill()

make_a_shape(5)

t.hideturtle() 

# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.

num_shapes = ...

for i in range(...):
    make_a_shape(t)
    t.right(360/num_shapes)
