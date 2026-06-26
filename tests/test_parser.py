import unittest
from minicalc.lexer import tokenize
from minicalc.parser import Parser
from minicalc.ast_nodes import AtribuicaoNode

class TestParser(unittest.TestCase):
    def test_atribuicao(self):
        tokens = tokenize("nota = 10")
        parser = Parser(tokens)
        ast = parser.parse()
        
        # O programa possui 1 comando
        comando = ast.comandos[0]
        self.assertIsInstance(comando, AtribuicaoNode)
        self.assertEqual(comando.var_nome, "nota")

if __name__ == '__main__':
    unittest.main()