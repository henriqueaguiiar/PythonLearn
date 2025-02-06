
valorDaCompra = float(input('Digite o valor da compra: '))
desconto: float

if valorDaCompra > 100.00:
    desconto = valorDaCompra * 0.1
elif valorDaCompra > 200.00:
    desconto = valorDaCompra * 0.2
else:
    desconto = valorDaCompra * 0.05

print(f'O valor da compra é: R$:{valorDaCompra}\nO valor do desconto: R$:{desconto:.2f}')