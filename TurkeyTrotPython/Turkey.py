import turtle
import random
from PIL import Image


class Turkey:
    window = None
    image_width = 150
    image_height = 109

    def __init__(self, x, y, name='', filename='turkey.gif'):
        self.x = x;
        self.y = y - (Turkey.image_height / 4)
        self.size = 100;
        self.minSpeed = 5;
        self.maxSpeed = 15;
        self.image = Image.open(filename)

        self.turkey_name = name

        if Turkey.window is not None:
            Turkey.window.addshape(filename)

        self.turtleObject = turtle.Turtle()
        self.turtleObject.hideturtle()
        self.turtleObject.shape(filename)
        self.turtleObject.penup()
        self.turtleObject.speed(0)
        self.turtleObject.goto(self.x, self.y)
        self.turtleObject.showturtle()

    def check_finish(self):
        return self.x > (Turkey.window.window_width() / 2)

    def trot(self):
        self.x += random.randint(self.minSpeed, self.maxSpeed)
        self.turtleObject.goto(self.x, self.y)

    def winner(self):
        self.turtleObject.hideturtle()
        self.turtleObject.backward(450)
        self.turtleObject.showturtle()
        self.turtleObject.write(arg=self.turkey_name + " is the Winner!!!", move=True, align='left', font=('Arial', 24, 'normal'))
        print( "Winner" )
