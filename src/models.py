"""Modelos de dados usados pelo sistema de gestão de peças.

Define as estruturas `Peca` e `Caixa`, que representam, respectivamente,
uma peça inspecionada na linha de montagem e uma caixa de armazenamento
de peças aprovadas.
"""

from dataclasses import dataclass, field

@dataclass
class Peca:
    """Representa uma peça produzida e já avaliada pela inspeção de qualidade."""

    id: str = ""  # Identificador único da peça
    peso: float = 0.0  # Peso da peça em gramas
    cor: str # Guarda a cor da peça
    comprimento: float # Comprimento da peça em centímetros
    status: str = "pendente"  # "aprovada" ou "reprovada"
    motivos: list[str] = field(default_factory=list) # Monta uma lista de motivos para a reprovação da peça

    @property
    def aprovada(self) -> bool:
        return self.status == "aprovada"
    # Retorna True se a peça estiver aprovada, False caso contrário.

    # Retorna uma representação em string da peça, incluindo seus atributos e motivos de reprovação, se houver.
    def __str__(self) -> str:
        base = (
            f"Peça {self.id} | peso={self.peso}g | cor={self.cor} | "
            f"comprimento={self.comprimento}cm | status={self.status}"
        )
        if self.motivos:
            base += f" | motivos: {', '.join(self.motivos)}"
        return base
