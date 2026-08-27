"""Gerenciamento das caixas de armazenamento de peças aprovadas."""

from models import Caixa, Peca


class GerenciadorCaixas:
    """Controla a caixa atualmente aberta e o histórico de caixas fechadas.

    Sempre que a caixa atual atinge a capacidade máxima (10 peças), ela é
    automaticamente fechada e movida para `caixas_fechadas`, e uma nova
    caixa vazia é aberta em seu lugar.
    """

    def __init__(self, capacidade: int = 10) -> None:
        self.capacidade = capacidade
        self._proximo_numero = 1
        self.caixa_atual = Caixa(numero=self._proximo_numero, capacidade=capacidade)
        self.caixas_fechadas: list[Caixa] = []
        # Inicializa o gerenciador com a caixa atual e a lista de caixas fechadas.

    def adicionar_peca_aprovada(self, peca: Peca) -> Caixa:
        """Adiciona a peça aprovada na caixa atual e fecha a caixa se necessário.

        Retorna a caixa em que a peça foi guardada.
        """
        caixa = self.caixa_atual
        caixa.adicionar(peca)

        if caixa.fechada:
            self.caixas_fechadas.append(caixa)
            self._proximo_numero += 1
            self.caixa_atual = Caixa(numero=self._proximo_numero, capacidade=self.capacidade)

        return caixa
        # método para remover uma peça da caixa atual.

    def remover_peca(self, peca_id: str) -> bool:
        """Remove uma peça da caixa atual (ainda aberta) pelo id.

        Peças em caixas já fechadas não podem ser removidas, pois a caixa
        fechada representa um lote já consolidado para expedição/estoque.
        Retorna True se a peça foi encontrada e removida.
        """
        for peca in list(self.caixa_atual.pecas):
            if peca.id == peca_id:
                self.caixa_atual.pecas.remove(peca)
                return True
        return False
    # método para contar o total de caixas utilizadas, incluindo a caixa atual se não estiver vazia.

    def total_caixas_utilizadas(self) -> int:
        """Conta caixas fechadas mais a caixa atual, se ela tiver ao menos uma peça."""
        extra = 1 if self.caixa_atual.quantidade > 0 else 0
        return len(self.caixas_fechadas) + extra
    # método para listar todas as caixas, incluindo a caixa atual e as fechadas.
