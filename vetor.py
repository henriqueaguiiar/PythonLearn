
n = int(input('Quantos numeros vai digitar: '))

vect = [i for i in range(n)]

for i in range(n):
    numero = float(input('Digite um numero: '))

for i in range(n):
    print('Valores')
    print(f'{vect[i]:.1f}')

soma = 0

for i in range(n):
    soma = soma + vect[i]

print(f'SOMA = {soma:.2f}')

media = soma / n

print(f'MEDIA = {media:.2f}')