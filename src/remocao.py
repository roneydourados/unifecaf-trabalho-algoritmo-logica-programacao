"""Remoção de peças cadastradas.
Este arquivo contém a função `remover_peca`, que permite remover peças cadastradas do sistema, 
tanto da lista de aprovadas quanto da lista de reprovadas, respeitando as regras de armazenamento.
"""

from armazenamento import GerenciadorCaixas
from models import Peca

def remover_peca(
    pecas_aprovadas: list[Peca],
    pecas_reprovadas: list[Peca],
    gerenciador: GerenciadorCaixas,
) -> None:
    peca_id = input("ID da peça a remover: ").strip()

    for peca in pecas_reprovadas:
        if peca.id == peca_id:
            pecas_reprovadas.remove(peca)
            print(f"Peça {peca_id} removida da lista de reprovadas.")
            return

    for peca in pecas_aprovadas:
        if peca.id == peca_id:
            if gerenciador.remover_peca(peca_id):
                pecas_aprovadas.remove(peca)
                print(f"Peça {peca_id} removida da caixa atual.")
            else:
                print(
                    f"Peça {peca_id} está em uma caixa já fechada e não pode ser removida."
                )
            return

    print(f"Nenhuma peça encontrada com o ID '{peca_id}'.")
