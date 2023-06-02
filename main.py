from turtle import *
import random

colormode(255)
color_list = [(211, 154, 98), (53, 107, 131), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98),
              (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128),
              (50, 126,
              121), (199, 123, 143), (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25),
              (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156),
              (165, 202, 210)]

speed("fastest")
penup()
hideturtle()

setheading(225)
forward(250)
setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    dot(20, random.choice(color_list))
    forward(50)

    if dot_count % 10 == 0:
        setheading(90)
        forward(50)
        setheading(180)
        forward(500)
        setheading(0)
exitonclick()
