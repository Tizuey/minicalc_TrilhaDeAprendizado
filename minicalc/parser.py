from minicalc.ast_nodes import (
    ProgramaNode, AtribuicaoNode, PrintNode,
    OperacaoBinariaNode, NumeroNode, VariavelNode
)

# Responsável por analisar a sequência de tokens e
# construir a Árvore Sintática Abstrata (AST).
class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    # Retorna o token que está sendo analisado no momento.
    def token_atual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    # Avança para o próximo token da lista.
    def avancar(self):
        self.pos += 1

    # Garante que o token atual seja do tipo esperado.
    # Caso contrário, interrompe a análise com erro.
    def consumir(self, tipo_esperado):
        token = self.token_atual()

        if token and token.tipo == tipo_esperado:
            self.avancar()
            return token

        raise SyntaxError(
            f"Erro Sintático: Esperado '{tipo_esperado}', "
            f"encontrado '{token.tipo if token else 'EOF'}'"
        )

    # Ponto de entrada da análise sintática.
    def parse(self):
        return self.parse_programa()

    # Processa todos os comandos encontrados no código fonte.
    def parse_programa(self):
        comandos = []

        while self.token_atual() is not None:
            comandos.append(self.parse_comando())

        return ProgramaNode(comandos)

    # Reconhece comandos de atribuição e impressão.
    def parse_comando(self):
        token = self.token_atual()

        if token.tipo == 'PRINT':
            self.avancar()

            expr = self.parse_expressao()
            return PrintNode(expr)

        elif token.tipo == 'ID':
            var_nome = token.valor

            self.avancar()
            self.consumir('ASSIGN')

            expr = self.parse_expressao()
            return AtribuicaoNode(var_nome, expr)

        raise SyntaxError(
            f"Erro Sintático: Comando inválido iniciando com {token.tipo}"
        )

    # Analisa expressões envolvendo soma e subtração.
    # Exemplo: a + b - c
    def parse_expressao(self):
        nodo = self.parse_termo()

        while (
            self.token_atual()
            and self.token_atual().tipo in ('PLUS', 'MINUS')
        ):
            op = self.token_atual()
            self.avancar()

            dir_nodo = self.parse_termo()
            nodo = OperacaoBinariaNode(nodo, op.valor, dir_nodo)

        return nodo

    # Analisa operações de multiplicação e divisão.
    # Possui precedência maior que soma e subtração.
    def parse_termo(self):
        nodo = self.parse_fator()

        while (
            self.token_atual()
            and self.token_atual().tipo in ('MUL', 'DIV')
        ):
            op = self.token_atual()
            self.avancar()

            dir_nodo = self.parse_fator()
            nodo = OperacaoBinariaNode(nodo, op.valor, dir_nodo)

        return nodo

    # Analisa os elementos básicos das expressões:
    # números, variáveis e expressões entre parênteses.
    def parse_fator(self):
        token = self.token_atual()

        if token is None:
            raise SyntaxError(
                "Erro Sintático: Fim de arquivo inesperado"
            )

        if token.tipo == 'NUM':
            self.avancar()
            return NumeroNode(token.valor)

        elif token.tipo == 'ID':
            self.avancar()
            return VariavelNode(token.valor)

        elif token.tipo == 'LPAREN':
            self.avancar()

            nodo = self.parse_expressao()

            self.consumir('RPAREN')
            return nodo

        raise SyntaxError(
            f"Erro Sintático: Fator inválido '{token.valor}'"
        )