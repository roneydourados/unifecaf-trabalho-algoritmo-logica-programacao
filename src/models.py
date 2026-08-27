"""Modelos de dados usados pelo sistema de gestão de peças.

Define as estruturas `Peca` e `Caixa`, que representam, respectivamente,
uma peça inspecionada na linha de montagem e uma caixa de armazenamento
de peças aprovadas.

Como não vai existir integração com banco de dados, todas as informações serão mantidas em memória.
Via estruturas de dados em memória, sem persistência em banco de dados.
"""

from dataclasses import dataclass, field

# Classe para representar uma peça produzida e avaliada pela inspeção de qualidade.
@dataclass
class Peca:
    """Representa uma peça produzida e já avaliada pela inspeção de qualidade."""

    id: str = ""  # Identificador único da peça
    peso: float = 0.0  # Peso da peça em gramas
    cor: str = "" # Guarda a cor da peça
    comprimento: float = 0.0 # Comprimento da peça em centímetros
    status: str = "pendente"  # "aprovada" ou "reprovada"
    motivos: list[str] = field(default_factory=lambda: list[str]()) # Monta uma lista de motivos para a reprovação da peça

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

@dataclass
class Caixa:
    """Representa uma caixa de armazenamento de peças aprovadas."""

    numero: int
    capacidade: int = 10
    pecas: list[Peca] = field(default_factory=lambda: list[Peca]())
    fechada: bool = False

   # Propriedades e métodos da classe Caixa.
    @property
    def quantidade(self) -> int:
        return len(self.pecas)
    # Retorna a quantidade de peças atualmente na caixa.

    @property
    def cheia(self) -> bool:
        return self.quantidade >= self.capacidade # Retorna True se a caixa estiver cheia, False caso contrário.

    # método para adicionar uma peça à caixa.
    def adicionar(self, peca: Peca) -> None:
        """Adiciona uma peça à caixa, se não estiver fechada ou cheia."""
        if self.fechada:
            raise ValueError(f"Caixa {self.numero} já está fechada.") # Levanta um erro se a caixa estiver fechada.
        if self.cheia:
            raise ValueError(f"Caixa {self.numero} já atingiu a capacidade máxima.") # Levanta um erro se a caixa estiver cheia.
        self.pecas.append(peca) # Adiciona a peça à lista de peças da caixa.
        if self.cheia:
            self.fechada = True  # Fecha a caixa automaticamente se atingir a capacidade máxima.

    # método para retornar uma representação em string da caixa.
    def __str__(self) -> str:
        situacao = "fechada" if self.fechada else "aberta" # Determina a situação da caixa (fechada ou aberta).
        ids = ", ".join(p.id for p in self.pecas) if self.pecas else "(vazia)" # Lista os IDs das peças na caixa ou indica que está vazia.
        return (
            f"Caixa {self.numero} [{situacao}] - {self.quantidade}/{self.capacidade} "
            f"peças: {ids}"
        ) # Retorna uma representação em string da caixa, incluindo sua situação, quantidade de peças e IDs das peças.
