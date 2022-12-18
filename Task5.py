# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.


x1 = float(input('Координата X1 = '))
y1 = float(input('Координата Y1 = '))

x2 = float(input('Координата X2 = '))
y2 = float(input('Координата Y2 = '))

import math
distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

distance = round(distance, 3)



print(distance)