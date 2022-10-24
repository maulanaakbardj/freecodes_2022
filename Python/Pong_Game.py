import os  
import turtle  
   
# First, we will create screen  
screen_1 = turtle.Screen()  
screen_1.title("Ping-Pong Game")  
screen_1.bgcolor("Yellow")  
screen_1.setup(width = 1050, height = 650)  
   
   
# Left paddle  
left_paddle = turtle.Turtle()  
left_paddle.speed(0)  
left_paddle.shape("square")  
left_paddle.color("Red")  
left_paddle.shapesize(stretch_wid = 6, stretch_len = 2)  
left_paddle.penup()  
left_paddle.goto(-400, 0)  
   
   
# Right paddle  
right_paddle = turtle.Turtle()  
right_paddle.speed(0)  
right_paddle.shape("square")  
right_paddle.color("Blue")  
right_paddle.shapesize(stretch_wid = 6, stretch_len = 2)  
right_paddle.penup()  
right_paddle.goto(400, 0)  
   
   
# Ball of circle shape  
hit_ball = turtle.Turtle()  
hit_ball.speed(45)  
hit_ball.shape("circle")  
hit_ball.color("White")  
hit_ball.penup()  
hit_ball.goto(0, 0)  
hit_ball.dx = 5  
hit_ball.dy = -5  
