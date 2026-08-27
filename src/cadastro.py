"""
Cadastro de novas peças no sistema.
Este arquivo contém a função para cadastrar novas peças no sistema, 
avaliando se são aprovadas ou reprovadas e armazenando-as adequadamente.
"""

from armazenamento import GerenciadorCaixas
from inspecao import avaliar_peca
from models import Peca
from utils import ler_float


def cadastrar_peca(
    pecas_aprovadas: list[Peca],
    pecas_reprovadas: list[Peca],
    gerenciador: GerenciadorCaixas,
) -> None:
    peca_id = input("ID da peça: ").strip()
    if not peca_id:
        print("ID não pode ser vazio. Cadastro cancelado.")
        return

    todos_ids = {p.id for p in pecas_aprovadas} | {p.id for p in pecas_reprovadas}
    if peca_id in todos_ids:
        print(f"Já existe uma peça cadastrada com o ID '{peca_id}'. Cadastro cancelado.")
        return

    peso = ler_float("Peso (g): ")
    cor = input("Cor: ").strip()
    comprimento = ler_float("Comprimento (cm): ")

    aprovada, motivos = avaliar_peca(peso, cor, comprimento)
    peca = Peca(
        id=peca_id,
        peso=peso,
        cor=cor,
        comprimento=comprimento,
        status="aprovada" if aprovada else "reprovada",
        motivos=motivos,
    )

    if aprovada:
        caixa = gerenciador.adicionar_peca_aprovada(peca)
        pecas_aprovadas.append(peca)
        print(f"Peça {peca_id} APROVADA e armazenada na caixa {caixa.numero}.")
        if caixa.fechada:
            print(f"Caixa {caixa.numero} atingiu a capacidade máxima e foi fechada.")
    else:
        pecas_reprovadas.append(peca)
        print(f"Peça {peca_id} REPROVADA. Motivos: {', '.join(motivos)}")
