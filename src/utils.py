"""
Funções utilitárias compartilhadas pelo menu interativo.
Este arquivo contém funções auxiliares que podem ser usadas em diferentes partes do sistema.
"""


def ler_float(mensagem: str) -> float:
    """Lê um número decimal do usuário, repetindo a pergunta em caso de erro."""
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Valor inválido. Digite um número (ex.: 98.5).")
