usuarios = {
    "ana": "123456",
    "joao": "senha123",
    "maria": "abc123"
}


def login(usuario, senha):
    if usuario in usuarios:
        if usuarios[usuario] == senha:
            print("Login realizado com sucesso")
            return True
        else:
            print("Senha incorreta")
    else:
        print("Usuário não encontrado")

    return False
def cadastrar_usuario(nome, senha):
    if nome in usuarios:
        print("Usuário já cadastrado")
    else:
        usuarios[nome] = senha
        print("Usuário cadastrado")