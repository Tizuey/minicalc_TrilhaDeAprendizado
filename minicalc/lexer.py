import re

# Representa um token identificado durante a análise léxica.
# Cada token possui um tipo e o valor encontrado no código fonte.
class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"Token({self.tipo}, {repr(self.valor)})"


def tokenize(codigo):
    """
    Recebe o código fonte e o divide em tokens que serão
    utilizados nas próximas etapas da compilação.
    """

    # Define todos os padrões reconhecidos pela linguagem.
    especificacao_tokens = [
        ('NUM',     r'\d+(\.\d*)?'),  # Números inteiros e decimais
        ('PRINT',   r'print\b'),      # Comando de impressão
        ('ID',      r'[A-Za-z_]\w*'), # Identificadores (nomes de variáveis)
        ('ASSIGN',  r'='),            # Operador de atribuição
        ('PLUS',    r'\+'),           # Soma
        ('MINUS',   r'-'),            # Subtração
        ('MUL',     r'\*'),           # Multiplicação
        ('DIV',     r'/'),            # Divisão
        ('LPAREN',  r'\('),           # Abre parêntese
        ('RPAREN',  r'\)'),           # Fecha parêntese
        ('SKIP',    r'[ \t\n]+'),     # Espaços em branco e quebras de linha
        ('MISMATCH',r'.'),            # Qualquer caractere não reconhecido
    ]

    # Combina todos os padrões em uma única expressão regular.
    regex_tokens = '|'.join(
        '(?P<%s>%s)' % par
        for par in especificacao_tokens
    )

    tokens = []

    # Percorre o código identificando os padrões definidos acima.
    for match in re.finditer(regex_tokens, codigo):
        tipo = match.lastgroup
        valor = match.group()

        # Espaços e quebras de linha não geram tokens.
        if tipo == 'SKIP':
            continue

        # Qualquer caractere inválido interrompe a análise.
        elif tipo == 'MISMATCH':
            raise RuntimeError(
                f"Erro Léxico: Caractere inesperado '{valor}'"
            )

        else:
            # Converte números para int ou float antes de armazená-los.
            if tipo == 'NUM':
                valor = float(valor) if '.' in valor else int(valor)

            tokens.append(Token(tipo, valor))

    return tokens