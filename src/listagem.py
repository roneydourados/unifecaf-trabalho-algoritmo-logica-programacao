"""Listagem de peças cadastradas.
Este arquivo contém a função `listar_pecas`, que exibe todas as peças 
cadastradas no sistema, separando-as em aprovadas e reprovadas.
"""

from models import Peca


def listar_pecas(pecas_aprovadas: list[Peca], pecas_reprovadas: list[Peca]) -> None:
    print("\n-- Peças aprovadas --")
    if not pecas_aprovadas:
        print("Nenhuma peça aprovada até o momento.")
    for peca in pecas_aprovadas:
        print(peca)

    print("\n-- Peças reprovadas --")
    if not pecas_reprovadas:
        print("Nenhuma peça reprovada até o momento.")
    for peca in pecas_reprovadas:
        print(peca)
# Retorna a lista de peças cadastradas, separando-as em aprovadas e reprovadas.
