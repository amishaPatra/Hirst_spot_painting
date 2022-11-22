# import colorgram
# rgb_colors = []
# colors = colorgram.extract('images.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle as t
t.colormode(255)
timmy = t.Turtle()
timmy.shape("triangle")
#timmy.color("white")
timmy.hideturtle()
color_list = [(24, 34, 53), (227, 158, 99), (137, 165, 200), (230, 216, 90), (207, 136, 144), (36, 100, 144), (174, 59, 43), (162, 20, 27), (131, 69, 77), (148, 31, 25), (236, 162, 167), (173, 185, 219), (45, 36, 34), (42, 30, 35), (236, 164, 159), (136, 187, 165), (16, 52, 48), (22, 62, 118), (217, 77, 61), (29, 78, 90), (193, 92, 100), (239, 176, 6), (83, 98, 96), (36, 77, 74), (171, 203, 190), (110, 122, 155)]
timmy.setheading(225)
timmy.penup()
timmy.forward(250)
timmy.setheading(0)
timmy.speed(0)
def dot():
    for i in range(10):

        timmy.dot(20,random.choice(color_list))
        timmy.forward(50)
        #timmy.penup()


def draw_left():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(50)

def draw_right():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(0)
    timmy.forward(50)

def paint(a):
    for i in range(a):
        dot()
        draw_left()
        dot()
        draw_right()

paint(5)




screen = t.Screen()
screen.exitonclick()