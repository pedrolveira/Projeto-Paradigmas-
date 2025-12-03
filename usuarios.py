from provas import sistema_provas


def cadastrar_usuario(usuarios):
    print("\n=== CADASTRO ===")
    nome = input("Nome: ")
    email = input("E-mail: ")
    cpf = input("CPF: ")
    senha = input("Senha: ")

    if email in usuarios:
        print("Usuário já cadastrado.\n")
        return

    usuarios[email] = {
        "nome": nome,
        "senha": senha,
        "cpf": cpf,
        "notas": []
    }

    print("✅ Usuário cadastrado com sucesso!\n")


def login_usuario(usuarios):
    email = input("E-mail: ")
    senha = input("Senha: ")

    if email in usuarios and usuarios[email]["senha"] == senha:
        print(f"\n✅ Bem-vindo, {usuarios[email]['nome']}!")
        sistema_provas(usuarios[email])
    else:
        print("\n❌ E-mail ou senha incorretos.\n")


def mostrar_estatisticas(usuarios):
    print("\n=== ESTATÍSTICAS ===")
    print(f"Total de usuários cadastrados: {len(usuarios)}")

    notas_gerais = []

    for u in usuarios.values():
        notas_gerais.extend(u["notas"])

    if notas_gerais:
        print(f"Nota mais baixa do sistema: {min(notas_gerais)}")
    else:
        print("Nenhuma prova registrada.")
    print("====================\n")
