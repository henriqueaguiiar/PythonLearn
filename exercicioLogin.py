admin_correto: str = 'admin'
senha_correta: int = 7787


admin = str(input("Username: "))
senha = int(input("Senha: "))

if admin == admin_correto and senha == senha_correta:
    print('Certo: Login OK')
else:
    print('Usuário ou senha incorretos.')



