# validação de usuários 

login = "MariaSilva"
senha = "12340987"
seu_login = input("Nome do usuário: ")
sua_senha = input("Digita sua senha: ")

if seu_login == login and sua_senha == senha:
    print("Seja bem vindo(a)")
else:
    print("Usuário ou senha inválidos! Tente novamente.")