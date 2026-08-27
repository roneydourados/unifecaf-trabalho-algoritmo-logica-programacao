"""
Desafio de Algoritmos e Lógica de Programação:

Você foi convidado por uma empresa do setor industrial para prototipar uma solução de
automação digital que auxilie no controle de produção e qualidade das peças fabricadas
em sua linha de montagem. Atualmente, o processo de inspeção é feito manualmente, o
que gera atrasos, falhas de conferência e aumento no custo de operação.
Sua missão é desenvolver em Python um sistema lógico capaz de:
● Receber os dados de cada peça produzida (id, peso, cor e comprimento).
● Avaliar automaticamente se a peça está aprovada ou reprovada, de acordo com
critérios de qualidade pré-definidos:
o Peso entre 95g e 105g
o Cor azul ou verde
o Comprimento entre 10cm e 20cm
● Armazenar as peças aprovadas em caixas de capacidade limitada (10 peças por
caixa).
● Fechar a caixa quando atingir a capacidade máxima e iniciar uma nova.
● Gerar relatórios consolidados com:
o Total de peças aprovadas
o Total de peças reprovadas e o motivo da reprovação
o Quantidade de caixas utilizadas
"""

MENU = """
===== GESTÃO DE PEÇAS, QUALIDADE E ARMAZENAMENTO =====
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
"""

def ler_float(mensagem: str) -> float:
    """Lê um número decimal do usuário, repetindo a pergunta em caso de erro."""
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Valor inválido. Digite um número (ex.: 98.5).")