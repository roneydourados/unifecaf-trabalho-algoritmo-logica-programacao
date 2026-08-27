"""Menu interativo do sistema de gestão de peças, qualidade e armazenamento.

Execução: `python3 src/main.py` a partir da raiz do projeto.

Sobre o Desafio:

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

from armazenamento import GerenciadorCaixas
from cadastro import cadastrar_peca
from caixas import listar_caixas_fechadas
from listagem import listar_pecas
from models import Peca
from relatorios import gerar_relatorio
from remocao import remover_peca

MENU = """
===== GESTÃO DE PEÇAS, QUALIDADE E ARMAZENAMENTO =====
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
"""


def main() -> None:
    pecas_aprovadas: list[Peca] = []
    pecas_reprovadas: list[Peca] = []
    gerenciador = GerenciadorCaixas(capacidade=10)

    while True:
        print(MENU)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_peca(pecas_aprovadas, pecas_reprovadas, gerenciador)
        elif opcao == "2":
            listar_pecas(pecas_aprovadas, pecas_reprovadas)
        elif opcao == "3":
            remover_peca(pecas_aprovadas, pecas_reprovadas, gerenciador)
        elif opcao == "4":
            listar_caixas_fechadas(gerenciador)
        elif opcao == "5":
            print(gerar_relatorio(pecas_aprovadas, pecas_reprovadas, gerenciador))
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
