dados = input('Digite seu nome, idade e altura: ').split() #Função split é usada para dividir ou quebrar uma string com base em um separador especifico
nome = dados[0]
idade = dados[1]
altura = dados[2]

print(f'Meu nome é {nome.upper()}, tenho {idade} anos de idade e minha altura é de {altura} metros')