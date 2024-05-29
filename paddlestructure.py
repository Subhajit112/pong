from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.goto(x,y)

    def continuous_moving(self):
       ## for i in range(-250,250):

       pass 

    def going_up(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(),newy)

    def going_down(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(),newy)

    

