from turtle import *
from random import *
shape("turtle")
penup()

arget = numinput("Скільки хочете набрати?", "Введіть число:", 1000, minval=3, maxval=59)
# малюємо круги
dot(200)
color('white')
dot(150)
color('black')
dot(100),
color('white')
dot(50)
color('red')
dot(25)

# малюємо цифри
color('green')
goto(90,0)
write('1',font=("Arial",18, "normal"))
color('green')
goto(65,0)
write('5',font=("Arial",14, "normal"))
color('green')
goto(15,15)
write('10',font=("Arial",14, "normal"))
color('green')
goto(5,5)
write('15',font=("Arial",14, "normal"))
color('green')
goto(-6,-6)
write('20',font=("Arial",14, "normal"))

#Запускаємо черепашок
color('blue')
goto(-200,-200)
goto(-140,-140)
stamp()
goto(randint(-100,100),randint(-20,40))
stamp()

if distance(0,0) <= 90 and distance(0,0) >= 65:
    vidmiruvach3 = 1
elif distance(0,0) <= 65 and distance(0,0) >= 45:
    vidmiruvach3 = 5
elif distance(0,0) <= 45 and distance(0,0) >= 25:
    vidmiruvach3 = 10
elif distance(0,0) <= 25 and distance(0,0) >= 5:
    vidmiruvach3 = 15
elif distance(0,0) <= 5 and distance(0,0) >= 0:
    vidmiruvach3 = 20


goto(randint(-100,100),randint(-20,40))
stamp()

if distance(0,0) <= 90 and distance(0,0) >= 65:
    vidmiruvach2 = 1
elif distance(0,0) <= 65 and distance(0,0) >= 45:
    vidmiruvach2 = 5
elif distance(0,0) <= 45 and distance(0,0) >= 25:
    vidmiruvach2 = 10
elif distance(0,0) <= 25 and distance(0,0) >= 5:
    vidmiruvach2 = 15
elif distance(0,0) <= 5 and distance(0,0) >= 0:
    vidmiruvach2 = 20
    

goto(randint(-100,100),randint(-20,40))
stamp()
if distance(0,0) <= 90 and distance(0,0) >= 65:
    vidmiruvach1 = 1
elif distance(0,0) <= 65 and distance(0,0) >= 45:
    vidmiruvach1 = 5
elif distance(0,0) <= 45 and distance(0,0) >= 25:
    vidmiruvach1 = 10
elif distance(0,0) <= 25 and distance(0,0) >= 5:
    vidmiruvach1 = 15
elif distance(0,0) <= 5 and distance(0,0) >= 0:
    vidmiruvach1 = 20
    

goto(170,170)
vidmiruvach = vidmiruvach3+vidmiruvach2+vidmiruvach1
vidmiruvach = int(vidmiruvach)
write(vidmiruvach,font=("Arial",18, "normal"))

if arget > vidmiruvach:
    write('Недобор')
else:
    write('Перебор')
