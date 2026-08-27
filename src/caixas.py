"""Listagem de caixas fechadas.

Este arquivo contém a função `listar_caixas_fechadas`, que exibe todas as caixas que foram fechadas no sistema.
"""

from armazenamento import GerenciadorCaixas


def listar_caixas_fechadas(gerenciador: GerenciadorCaixas) -> None:
    print("\n-- Caixas fechadas --")
    if not gerenciador.caixas_fechadas:
        print("Nenhuma caixa fechada até o momento.")
    for caixa in gerenciador.caixas_fechadas:
        print(caixa)
# Retorna a lista de caixas fechadas
