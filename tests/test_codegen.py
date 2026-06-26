import unittest
from minicalc.lexer import tokenize
from minicalc.parser import Parser
from minicalc.codegen import Codegen

class TestCodegen(unittest.TestCase):
    def test_geracao_python(self):
        tokens = tokenize("x = 5 \n print x")
        ast = Parser(tokens).parse()
        codigo = Codegen().gerar(ast)
        
        self.assertIn("x = 5", codigo)
        self.assertIn("print(x)", codigo)

if __name__ == '__main__':
    unittest.main()