
from Estudante import Estudante
from Desempenho import (
    calcular_media,
    calcular_frequencia,
    verificar_situacao
)

estudantes = []


def cadastrar_estudante():
    print("\n--- CADASTRO DE ESTUDANTE ---")

    nome = input("Nome: ").strip()
    matricula = input("Matrícula: ").strip()
    turma = input("Turma: ").strip()

    if not nome or not matricula or not turma:
        print("Preencha todos os campos.")
        return

    if any(e.matricula == matricula for e in estudantes):
        print("Essa matrícula já está cadastrada.")
        return

    estudante = Estudante(nome, matricula, turma)
    estudantes.append(estudante)

    print("Estudante cadastrado com sucesso!")


def listar_estudantes():
    print("\n--- LISTA DE ESTUDANTES ---")

    if not estudantes:
        print("Nenhum estudante cadastrado.")
        return

    for estudante in estudantes:
        print(
            f"Matrícula: {estudante.matricula} | "
            f"Nome: {estudante.nome} | "
            f"Turma: {estudante.turma}"
        )


def registrar_notas():
    matricula = input("Digite a matrícula: ").strip()

    for estudante in estudantes:
        if estudante.matricula == matricula:
            try:
                nota1 = float(input("Primeira nota (0 a 10): "))
                nota2 = float(input("Segunda nota (0 a 10): "))

                estudante.registrar_notas(nota1, nota2)
                print("Notas registradas com sucesso!")

            except ValueError as erro:
                print(f"Erro: {erro}")

            return

    print("Estudante não encontrado.")


def registrar_faltas():
    matricula = input("Digite a matrícula: ").strip()

    for estudante in estudantes:
        if estudante.matricula == matricula:
            try:
                total = int(input("Total de aulas: "))
                faltas = int(input("Quantidade de faltas: "))

                estudante.registrar_frequencia(total, faltas)
                print("Frequência registrada com sucesso!")

            except ValueError as erro:
                print(f"Erro: {erro}")

            return

    print("Estudante não encontrado.")


def gerar_relatorio():
    print("\n--- RELATÓRIO ACADÊMICO ---")

    if not estudantes:
        print("Nenhum estudante cadastrado.")
        return

    for estudante in estudantes:
        media = calcular_media(
            estudante.nota1,
            estudante.nota2
        )

        frequencia = calcular_frequencia(
            estudante.total_aulas,
            estudante.faltas
        )

        situacao = verificar_situacao(media, frequencia)

        print("\n------------------------------")
        print(f"Nome: {estudante.nome}")
        print(f"Matrícula: {estudante.matricula}")
        print(f"Turma: {estudante.turma}")
        print(f"Média: {media:.2f}")
        print(f"Frequência: {frequencia:.1f}%")
        print(f"Situação: {situacao}")


def menu():
    while True:
        print("\n===== SISTEMA DE GESTÃO ACADÊMICA =====")
        print("1 - Cadastrar estudante")
        print("2 - Listar estudantes")
        print("3 - Registrar notas")
        print("4 - Registrar frequência")
        print("5 - Gerar relatório")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_estudante()
        elif opcao == "2":
            listar_estudantes()
        elif opcao == "3":
            registrar_notas()
        elif opcao == "4":
            registrar_faltas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
