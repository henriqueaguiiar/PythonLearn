horaDoDia = float(input('Digite a hora do dia: '))

if horaDoDia < 12.00:
    print(f'Hora do dia: {horaDoDia} Bom dia')
elif horaDoDia < 18.00:
    print(f'Hora do dia: {horaDoDia} Boa Tarde')
else:
    print(f'Hora do dia: {horaDoDia} Boa noite')
