#!/usr/bin/env python
# coding: utf-8

# In[1]:


from turtle import *

speed(0)
setup(800, 500)

#making the red background
bgcolor("red")

#Drawing the white lines, similar to a cross
penup()
goto(-400, -50)
pendown()

color("white")
begin_fill()
forward(800)
left(90)
forward(100)
left(90)
forward(800)
end_fill()

penup()
goto(-100, -250)
pendown()

begin_fill()
forward(100)
right(90)
forward(500)
right(90)
forward(100)
end_fill()

#Drawing the white lines, similar to a cross next to the white one
penup()
goto(-400, -25)
pendown()

color("midnightblue")
begin_fill()
forward(800)
left(90)
forward(50)
left(90)
forward(800)
end_fill()

penup()
goto(-125, -250)
pendown()

begin_fill()
forward(50)
right(90)
forward(500)
right(90)
forward(50)
end_fill()

hideturtle()


# In[ ]:


import turtle

#1st function: defining rectangle

def draw_rectangle(length, height, x, y, color):
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()

    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

    turtle.end_fill()


# In[5]:


#2nd function: defining star

def draw_star(size, x, y, color):
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()

    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()

    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

    turtle.end_fill()


# In[6]:


#3rd function: defining colors

def get_color(color):
    if color=='red':
        return 1,0,0
    elif color=='blue':
        return 0,0,1
    elif color=='white':
        return 1,1,1


# In[7]:


#4th function: defining the flag itself

def draw_flag(height):
    #top left corner cooredinates
    locx=-300
    locy=200

    x=locx
    y=locy
    #flag length
    length=600
    #red rectangle stripes
    for stripe in range(1,14):
        if stripe%2==0:
            color='white'

        if stripe%2==1:
            color='red'

        draw_rectangle(length, height, x,y, color)
        y-=height

    #blue top left box
    x=locx
    y=locy
    draw_rectangle(250,height*7,x,y,'blue')

    #white stars
    y-=10
    nextline=-19
    for rows in range(1,10):
        if rows%2==1:
            loop=7
            x = locx+5

        if rows%2==0:
            loop=6
            x= locx+25

        for row in range(1,loop):
            draw_star(17,x,y,'white')
            x+=45
        y+=nextline

    #flag border
    x=locx
    y=locy
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()

    turtle.pencolor('black')

    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(height*13)
        turtle.right(90)


# In[8]:


#5th required function: main function
def main():
    turtle.setup(900,800)
    turtle.speed(0)
    height = 25
    draw_flag(height)
    print('Coordinates of red color is {}'.format(get_color('red')))
    turtle.exitonclick()

#Required call to main function
if __name__ == "__main__":
    main()

