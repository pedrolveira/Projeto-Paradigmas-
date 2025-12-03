def sistema_provas(usuario):
    print("\n=== SISTEMA DE PROVAS ===")

    notas = []

    a1 = float(input("Digite a nota A1: "))
    a2 = float(input("Digite a nota A2: "))

    notas.extend([a1, a2])
    media = (a1 + a2) / 2

    if media < 6:
        print("\n⚠ Média insuficiente. Digite a nota da A3:")
        a3 = float(input("Digite a nota A3: "))
        notas.append(a3)

        notas.sort()
        media = (notas[1] + notas[2]) / 2

    situacao = "APROVADO" if media >= 6 else "REPROVADO"

    usuario["notas"] = notas

    print("\n=== RESULTADO ===")
    print(f"Notas: {notas}")
    print(f"Média final: {media:.2f}")
    print(f"Situação: {situacao}")
    print(f"Nota mais baixa: {min(notas)}\n")
