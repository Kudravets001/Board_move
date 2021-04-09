from turtle import *
import math
import decimal

trt = Turtle()
trt.screen.setup(800, 800)


def coordinates():
    trt.hideturtle()
    trt.speed(0)
    trt.up()
    trt.goto(-800, 0)
    trt.down()
    trt.fd(1600)
    trt.up()
    trt.goto(0, 400)
    trt.down()
    trt.left(270)
    trt.fd(1600)
    trt.up()
    trt.goto(0, 0)
    trt.down()
    trt.speed("normal")
    trt.showturtle()




K = 1
 #R = float(input("Введите радиус шара(в метрах):\n")) # радиус шара.
H = float(input("Введите глубину,погруженной в воду(в метрах):\n"))

s = 1500 # коэффициент сопротивления.
g = 9.81  # ускорение свободного падения.
Pm_temp = str(input("""Выберите один из указанных материалов:
    1.Аллюминий
    2.Дерево(сосна)\n
    """))


def material(Pm_temp):
    global Pm
    # if Pm_temp == "0":
    #     Pm = 7800
    if Pm_temp == "1":
        Pm = 2700
    elif Pm_temp == "2":
        Pm = 400
    else:
        Pm_temp1 = str(input("Ошибка. Введите корректное значение( 1 или 2)\n"))
        material(Pm_temp1)
material(Pm_temp)
v0 = float(input("Введите начальную скорость (м/c)"))  # начальная скорость броска.
while v0 < 0:
    v0 = float(input("Начальная скорость не может быть отрицательной\nВведите начальную скорость (м/c)"))
A1 = float(input("Введите длину палубы,погруженной в воду (м)"))
while A1 < 0:
    A1 = float(input("Введите длину палубы,погруженной в воду (м)"))
B1 = float(input("Введите ширину палубы,погруженной в воду (м)"))
while B1 < 0:
    B1 = float(input("Введите длину палубы,погруженной в воду (м)"))
A2 = float(input("Введите длину дна палубы (м)"))
while A2 < 0:
    A2 = float(input("Введите длину дна палубы (м)"))
B2 = float(input("Введите ширину дна палубы,погруженной в воду (м)"))
while B2 < 0:
    B2 = float(input("Введите ширину дна палубы,погруженной в воду (м)"))
S1 = A1*B1
S2 = A2*B2
V = 1/3*H*(S1+S2+(math.sqrt(S1*S2)))
 # angle = int(input("Введите угол под которым совершается бросок(градусы)"))  # угол броска.
m = float(V*Pm)  # масса шара.
print(m, 'кг')
G = 9.81

alfa = 0  # math.radians(angle)  # угол подбрасывания (в радианах).
dt = 1/30
hmax = 0  # вводим переменные для определения координат.
xmax = 0
v = v0      # начальная скорость.
t = 0       # начальное время.
y = 0 # начальная ордината шара.
h = 0       # начальная высота
x = 0       # // начальная абсцисса шара.
# раскладываем вектор скорости на проекции на оси.
vx = v * math.cos(alfa)
vy = 0 #v * math.sin(alfa)
xk = 400
coordinates()
trt.speed(10)
Fcx = -s*H*vx

while (Fcx <= -3000):
    #yk = 590 - K * y
    xk = 100 + x
    Fcx = - s * H * vx
    Fcy = 0#- s * R * vy
    ay = 0#Fcy / m - g
    ax = Fcx / m
    y = 0#y + vy * dt + ay * G*dt * dt / 2
    h = y
    vy = 0 #vy + ay * dt
    x = x + vx * dt + ax * dt * dt / 2
    vx = vx + ax * dt
    v = math.sqrt(vx * vx + vy * vy)
    t = t + dt

    if (h > hmax):
        hmax = h
    if (x > xmax):
        xmax = x

    trt.goto(x, y+50)

print("Time: ",t)
# print("Max height: ",hmax)
print("Lenght: ",xmax)
trt.screen.exitonclick()
trt.screen.mainloop()