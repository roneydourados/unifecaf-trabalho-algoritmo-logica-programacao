# Gestão de Peças, Qualidade e Armazenamento

Protótipo em Python de um sistema de automação digital para controle de produção e
qualidade de peças em uma linha de montagem industrial. O sistema recebe os dados de
cada peça, avalia automaticamente se ela é aprovada ou reprovada, armazena as peças
aprovadas em caixas de capacidade fixa e gera relatórios consolidados.

Trabalho da disciplina **Algoritmos e Lógica de Programação**.

## Funcionalidades

O programa roda em um menu interativo no terminal com as seguintes opções:

1. **Cadastrar nova peça** — informa ID, peso (g), cor e comprimento (cm) de uma peça.
   O sistema avalia automaticamente a peça e informa se foi aprovada ou reprovada
   (com o(s) motivo(s), se reprovada).
2. **Listar peças aprovadas/reprovadas** — mostra todas as peças cadastradas,
   separadas por status; peças reprovadas exibem os motivos da reprovação.
3. **Remover peça cadastrada** — remove uma peça pelo ID. Peças reprovadas podem
   ser removidas a qualquer momento; peças aprovadas só podem ser removidas
   enquanto ainda estiverem na caixa em aberto — uma vez que a caixa é fechada
   (atinge 10 peças), seu conteúdo é considerado consolidado e não pode mais
   ser alterado.
4. **Listar caixas fechadas** — exibe todas as caixas que já atingiram a
   capacidade máxima (10 peças) e foram fechadas, com os IDs das peças de cada uma.
5. **Gerar relatório final** — exibe total de peças aprovadas, total de peças
   reprovadas (agrupadas por motivo) e a quantidade de caixas utilizadas.
6. **Sair** — encerra o programa.

### Critérios de aprovação

Uma peça é aprovada somente se atender **todos** os critérios abaixo:

| Critério    | Faixa válida                  |
| ----------- | ----------------------------- |
| Peso        | entre 95g e 105g (inclusive)  |
| Cor         | azul ou verde                 |
| Comprimento | entre 10cm e 20cm (inclusive) |

Se a peça falhar em mais de um critério, todos os motivos são registrados e
exibidos.

### Armazenamento em caixas

- Cada caixa comporta no máximo **10 peças aprovadas**.
- Ao atingir a capacidade, a caixa é fechada automaticamente e uma nova caixa
  é aberta para receber as próximas peças aprovadas.

## Estrutura do projeto

```
src/
├── main.py            # menu interativo (ponto de entrada)
├── models.py          # dataclasses Peca e Caixa
├── inspecao.py         # regras de aprovação/reprovação
├── armazenamento.py    # gerenciamento das caixas (GerenciadorCaixas)
├── cadastro.py          # cadastro de novas peças (avalia e armazena)
├── listagem.py          # listagem de peças aprovadas/reprovadas
├── caixas.py             # listagem de caixas fechadas
├── remocao.py            # remoção de peças cadastradas
├── relatorios.py         # geração do relatório final
└── utils.py               # funções utilitárias (ex.: leitura de float)
```

## Como rodar

Requer apenas **Python 3.10+** (usa apenas a biblioteca padrão — nenhuma
dependência externa é necessária para executar o programa).

```bash
# a partir da raiz do projeto
python3 src/main.py
```

No menu, digite o número da opção desejada e pressione Enter. Para
cadastrar uma peça, informe os dados quando solicitado (use ponto ou
vírgula para números decimais, ex.: `98.5` ou `98,5`).

## Exemplo de uso

```
===== GESTÃO DE PEÇAS, QUALIDADE E ARMAZENAMENTO =====
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair

Escolha uma opção: 1
ID da peça: P1
Peso (g): 100
Cor: azul
Comprimento (cm): 15
Peça P1 APROVADA e armazenada na caixa 1.

Escolha uma opção: 1
ID da peça: P2
Peso (g): 50
Cor: vermelho
Comprimento (cm): 15
Peça P2 REPROVADA. Motivos: peso fora do padrão (50.0g; esperado entre 95.0g e 105.0g), cor não permitida (vermelho; esperado azul ou verde)

Escolha uma opção: 5
===== RELATÓRIO FINAL =====
Total de peças aprovadas: 1
Total de peças reprovadas: 1
Motivos de reprovação:
  - peso fora do padrão (50.0g; esperado entre 95.0g e 105.0g): 1 ocorrência(s)
  - cor não permitida (vermelho; esperado azul ou verde): 1 ocorrência(s)
Quantidade de caixas utilizadas: 1
============================
```

## Documentação do desafio

O enunciado do desafio proposto pela disciplina está em
[`docs/Desafio.pdf`](docs/Desafio.pdf).
