usuarios = {}

def cadastrar():
    usuario = input("Crie um usuário: ")
    
    if usuario in usuarios:
        print("Usuário já existe!")
        return
    
    senha = input("Crie uma senha: ")
    usuarios[usuario] = senha
    
    print("Cadastro realizado!")

def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha incorretos.")

while True:
    print("\n1 - Cadastrar")
    print("2 - Login")
    print("0 - Sair")
    
    op = input("Escolha: ")
    
    if op == "1":
        cadastrar()
    elif op == "2":
        login()
    elif op == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida")