from minicalc.ast_nodes import (
    ProgramaNode, AtribuicaoNode, PrintNode,
    OperacaoBinariaNode, NumeroNode, VariavelNode
)

# Responsável por percorrer a AST e transformar seus nós
# em código Python equivalente.
class Codegen:

    def gerar(self, node):

        # O programa é composto por uma sequência de comandos.
        # Cada comando gerado é separado por uma quebra de linha.
        if isinstance(node, ProgramaNode):
            return "\n".join(self.gerar(cmd) for cmd in node.comandos)

        # Gera uma instrução de atribuição.
        # Exemplo: x = 10
        elif isinstance(node, AtribuicaoNode):
            return f"{node.var_nome} = {self.gerar(node.expressao)}"

        # Gera uma chamada para impressão na saída.
        # Exemplo: print(x)
        elif isinstance(node, PrintNode):
            return f"print({self.gerar(node.expressao)})"

        # Gera uma operação matemática entre dois operandos.
        # Os parênteses ajudam a preservar a ordem da expressão.
        elif isinstance(node, OperacaoBinariaNode):
            return f"({self.gerar(node.esq)} {node.op} {self.gerar(node.dir)})"

        # Para números, basta retornar seu valor em formato de texto.
        elif isinstance(node, NumeroNode):
            return str(node.valor)

        # Para variáveis, retorna apenas o nome que será usado no código gerado.
        elif isinstance(node, VariavelNode):
            return node.nome

        # Caso apareça um tipo de nó não tratado pelo gerador.
        else:
            raise TypeError(
                f"Tipo de nó AST desconhecido no gerador de código: {type(node)}"
            )