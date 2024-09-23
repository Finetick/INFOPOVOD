import math

L = int(input("Введите L: "))
g = 9.81
T = 2*math.pi*((L/g)**(1/2))

itog = round(T, 2)

print(itog)
