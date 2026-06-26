# Classe principal da AST.
# Ela representa o programa inteiro e guarda a lista de comandos encontrados.
class ProgramaNode:
    def __init__(self, comandos):
        self.comandos = comandos

    def __repr__(self):
        return f"Programa({self.comandos})"


# Representa uma atribuição de valor para uma variável.
# Exemplo: x = 10
class AtribuicaoNode:
    def __init__(self, var_nome, expressao):
        self.var_nome = var_nome
        self.expressao = expressao

    def __repr__(self):
        return f"Atribuicao({self.var_nome} = {self.expressao})"


# Representa um comando de impressão na saída.
# Exemplo: print(x)
class PrintNode:
    def __init__(self, expressao):
        self.expressao = expressao

    def __repr__(self):
        return f"Print({self.expressao})"


# Representa uma operação entre dois operandos.
# Exemplo: 5 + 3 ou x * y
class OperacaoBinariaNode:
    def __init__(self, esq, op, dir):
        self.esq = esq      # Operando da esquerda
        self.op = op        # Operador (+, -, *, /)
        self.dir = dir      # Operando da direita

    def __repr__(self):
        return f"OpBinaria({self.esq} {self.op} {self.dir})"


# Nó utilizado para armazenar valores numéricos.
class NumeroNode:
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return f"Numero({self.valor})"


# Nó utilizado para representar uma variável durante a análise.
class VariavelNode:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"Variavel({self.nome})"