from math import trunc
from operator import truediv

# Utilizando Números
for i in range (1, 6):
    print(i)


#Utilizando Strings


nome: str = 'henrique'

for i in nome:
    print(f' {i}', end='')


#for com if else

compra_confirmada = False
dados_compra = 'Compra no valor de R$12.50 e entrega confirmada'

for i in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu e-mail')
        break
else:
    print('Falha na compra')



linha = 6
colunas = 6
simnolo = '@'

for i in range(linha):
    for j in range(colunas):
        print(simnolo, end='')
    print()