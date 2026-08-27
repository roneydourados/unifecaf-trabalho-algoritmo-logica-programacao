"""Regras de qualidade usadas para aprovar ou reprovar uma peça.

Critérios (todos precisam ser atendidos para aprovação):
    - Peso entre 95g e 105g (inclusive)
    - Cor azul ou verde
    - Comprimento entre 10cm e 20cm (inclusive)

Este arquivo contém a função `avaliar_peca`, que verifica se uma peça atende aos critérios de qualidade definidos.
"""

PESO_MIN = 95.0
PESO_MAX = 105.0
CORES_APROVADAS = {"azul", "verde"}
COMPRIMENTO_MIN = 10.0
COMPRIMENTO_MAX = 20.0


def avaliar_peca(peso: float, cor: str, comprimento: float) -> tuple[bool, list[str]]:
    """Avalia uma peça segundo os critérios de qualidade.

    Retorna uma tupla (aprovada, motivos). `motivos` fica vazia quando a peça
    é aprovada; caso contrário, contém uma mensagem para cada critério não
    atendido (uma peça pode falhar em mais de um critério simultaneamente).
    """
    motivos: list[str] = []

    if not (PESO_MIN <= peso <= PESO_MAX):
        motivos.append(
            f"peso fora do padrão ({peso}g; esperado entre {PESO_MIN}g e {PESO_MAX}g)"
        )

    if cor.strip().lower() not in CORES_APROVADAS:
        motivos.append(f"cor não permitida ({cor}; esperado azul ou verde)")

    if not (COMPRIMENTO_MIN <= comprimento <= COMPRIMENTO_MAX):
        motivos.append(
            f"comprimento fora do padrão ({comprimento}cm; esperado entre "
            f"{COMPRIMENTO_MIN}cm e {COMPRIMENTO_MAX}cm)"
        )

    aprovada = len(motivos) == 0
    return aprovada, motivos
