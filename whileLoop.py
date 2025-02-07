print('Digite as 3 distancias: ')

distancia1 = float(input())
distancia2 = float(input())
distancia3 = float(input())

maior_distancia: float = distancia1

if distancia2 > distancia1:
    maior_distancia = distancia2
elif distancia3 > distancia2:
    maior_distancia = distancia3

print(f'A maior distancia é : {maior_distancia:.0}')


