"""Geração do relatório consolidado de produção.

Este arquivo contém a função `gerar_relatorio`, que monta o texto 
do relatório final com totais de peças aprovadas, reprovadas e caixas utilizadas, 
incluindo os motivos de reprovação.
"""

from collections import Counter

from armazenamento import GerenciadorCaixas
from models import Peca

def gerar_relatorio(
    pecas_aprovadas: list[Peca],
    pecas_reprovadas: list[Peca],
    gerenciador: GerenciadorCaixas,
) -> str:
    """Monta o texto do relatório final com totais e motivos de reprovação."""

    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas)
    total_caixas = gerenciador.total_caixas_utilizadas()

    linhas = [
        "===== RELATÓRIO FINAL =====",
        f"Total de peças aprovadas: {total_aprovadas}",
        f"Total de peças reprovadas: {total_reprovadas}",
    ]

    if pecas_reprovadas:
        linhas.append("Motivos de reprovação:")
        contador_motivos: Counter[str] = Counter()
        for peca in pecas_reprovadas:
            for motivo in peca.motivos:
                contador_motivos[motivo] += 1
        for motivo, quantidade in contador_motivos.most_common():
            linhas.append(f"  - {motivo}: {quantidade} ocorrência(s)")

    linhas.append(f"Quantidade de caixas utilizadas: {total_caixas}")
    linhas.append("============================")

    return "\n".join(linhas)
