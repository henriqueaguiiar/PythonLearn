codPeca = int(input("Enter the id of piece: "))
numPeca = int(input("Enther the number pieces: "))
valuePeca = float(input("Enter the value: "))

codPeca2 = int(input("Enter the id of piece: "))
numPeca2 = int(input("Enther the number pieces: "))
valuePeca2= float(input("Enter the value: "))

finalValue = float((numPeca*valuePeca)+(numPeca2*valuePeca2))

print(f"VALOR A PAGAR: R$ {finalValue:.2f}")