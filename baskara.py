import math

print('Digite os coeficientes da equação de 2 grau: ')

a = float(input())
b = float(input())
c = float(input())

#calculando delta
delta = a * b -4 * a * c

if delta < 0:
    print('Essa equação não possui raizes reais!')
else:
    x1 = (-b + math.sqrt(delta) / 2 * a)
    x2 = (-b - math.sqrt(delta) / 2 * a)