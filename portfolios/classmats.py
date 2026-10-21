from datetime import datetime
from time import sleep
import classmatsDB as banco


class Materia:
    def __init__(self, nome, data_criacao=None):
        self.nome = nome
        self.data_criacao = data_criacao or datetime.now()


def adicionar_materia():
    nova_materia = input("Qual matéria você deseja adicionar? ").strip()
    if not nova_materia:
        print("Nome da matéria não pode ser vazio.")
        return

    banco.inserir_materia(nova_materia)
    print(f"Adicionando {nova_materia}...")
    sleep(1)
    print(f"{nova_materia} Adicionada!")


def ver_materia():
    print("\n--- Suas Matérias ---")
    materias = banco.listar_materias()
    if not materias:
        print("Nenhuma matéria encontrada no arquivo.")
        return

    for registro in materias:
        materia = Materia(
            registro["nome"],
            datetime.fromisoformat(registro["data_criacao"]),
        )
        print(f"Matéria: {materia.nome} | Data de Criação: {materia.data_criacao}")


def apagar_materia():
    materias = banco.listar_materias()
    if not materias:
        print("Nenhuma matéria cadastrada.")
        return

    ver_materia()
    ap = input("Digite a matéria que deseja remover: ").strip()

    if banco.remover_materia(ap):
        print(f"Matéria '{ap}' removida com sucesso!")
    else:
        print(f"Matéria '{ap}' não encontrada.")


def main():
    banco.criar_tabela()
    while True:
        print("\n 1 - Adicionar | 2 - Ver | 3 - Apagar | Digite -cls- para sair")
        opcao = input("O que deseja? ").strip()

        if opcao == "1":
            adicionar_materia()
        elif opcao == "2":
            ver_materia()
        elif opcao == "3":
            apagar_materia()
        elif opcao.lower() == "cls":
            print("Saindo...")
            sleep(1)
            break
        elif opcao == "":
            print("Nenhuma opção selecionada. Por favor, digite uma opção válida.")
        elif opcao not in ["1", "2", "3", "cls"]:
            print("Opção inválida. Por favor, digite uma opção válida.")


if __name__ == "__main__":
    main()
