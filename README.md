def menu_inicial():
    print("+----------------------------------------+")
    print("|        SISTEMA DE CADASTRO / LOGIN      |")
    print("+----------------------------------------+")
    print("| [1] Cadastrar usuário                  |")
    print("| [2] Login                              |")
    print("| [3] Estatísticas                      |")
    print("| [4] Sair                               |")
    print("+----------------------------------------+")

def cadastrar_usuario(usuarios):
    usuario = input("Digite um nome de usuário: ")

    if usuario in usuarios:
        print("❌ Usuário já cadastrado.\n")
        return

    senha = input("Digite a senha: ")
    usuarios[usuario] = senha
    print("✅ Usuário cadastrado com sucesso!\n")

def login_usuario(usuarios):
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        print("\n✅ Login realizado com sucesso!")
        return True
    else:
        print("\n❌ Usuário ou senha incorretos.\n")
        return False

def mostrar_estatisticas(usuarios):
    total = len(usuarios)

    print("\n========= ESTATÍSTICAS =========")
    print(f"Total de usuários cadastrados: {total}")

    if total > 0:
        media = total / 1  # média simples (1 turma/sistema)
    else:
        media = 0

    print(f"Média de usuários cadastrados: {media:.2f}")
    print("================================\n")

# ---------------- PROGRAMA PRINCIPAL ----------------

usuarios = {}

while True:
    menu_inicial()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario(usuarios)

    elif opcao == "2":
        if not usuarios:
            print("⚠️ Nenhum usuário cadastrado. Cadastre primeiro.\n")
            continue

        if login_usuario(usuarios):
            sair = input("Deseja sair do sistema? (S/N): ").strip().upper()
            if sair == "S":
                print("Encerrando o sistema...")
                break
            else:
                print("Retornando ao menu inicial...\n")

    elif opcao == "3":
        mostrar_estatisticas(usuarios)

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida.\n")
