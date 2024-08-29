import turtle
import random
import time

contar = 0
turtle = turtle.Turtle("turtle")
while True:
  turtle.penup()
  turtle.goto(40,70)
  turtle.width(random.randrange(2,30))
  turtle.pendown()
  i=0
  lado = random.randrange(1,10)
  angulo = random.randrange(30,270)
  red = 0
  green = 0
  blue = 0
  turtle.speed(5000)
  while i<500:
    red=random.randrange(0,255)
    blue=random.randrange(0,255)
    green=random.randrange(0,255)
    turtle.color(red,green,blue)
    turtle.forward(lado)
    turtle.right(angulo)
    i=i+1
    lado=lado+1
  time.sleep(2)
  contar=contar+1
  print(contar)
  turtle.penup()
  turtle.clear()