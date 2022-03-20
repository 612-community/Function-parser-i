import turtle
pen = turtle.Pen()

a = print('b的长度(无需填)')

b = print('a的长度(无需填)')

c = input('b的位置')
c = float(c)

d = input('a的位置')
d = float(d)

e = input('b的指数')
e = float(e)

f = input('a的指数')
f = float(f)

g = input('b的斜率')
g = float(g)

v = input('a的斜率')
v = float(v)

#控制
#b的位置
m = c
#a的位置
k = d
#b的指数
h = e
#a的指数
H = f
#b的斜率
n = g
#a的斜率
N = v
#大小
s = 10

#r = 2 * (h...) /n
#R =  2 * (h...) /n

pen.goto(-800,0)
pen.goto(800,0)
pen.goto(0,0)
pen.goto(0,400)
pen.goto(0,-400)
pen.goto(0,0)


pen.goto(0,s * k)

pen.pencolor('red')

x = 1
y = 1
i = 0
while x < 800 / s and x > -800 / s and y < 400 / s and y > -400 / s :
    x = 0.1 * i
    i = i + 1
    y = (x ** H) * N + k
    pen.goto(s * x,s * y)


pen.penup()
pen.goto(0,s * k)
pen.pendown()

x = 1
y = 1
i = 0
while x < 800 / s and x > -800 / s and y < 400 / s and y > -400 / s :
    x = 0.1 * (- i)
    i = i + 1
    y = (x ** H) * N + k
    pen.goto(s * x,s * y)
pen.penup()
pen.goto(0,s * m)
pen.pendown()
pen.pencolor('blue')

x = 1
y = 1
a = 0
while x < 800 / s and x > -800 / s and y < 400 / s and y > -400 / s :
    x = 0.1 * a
    a = a + 1
    y = (x ** h) * n + m
    pen.goto(s * x,s * y)

pen.penup()
pen.goto(0,s * m)
pen.pendown()

x = 1
y = 1
a = 0
while x < 800 / s and x > -800 / s and y < 400 / s and y > -400 / s :
    x = 0.1 * (- a)
    a = a + 1
    y = (x ** h) * n + m
    pen.goto(s * x,s * y)

turtle.done()