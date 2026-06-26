import unittest
from minicalc.lexer import tokenize

class TestLexer(unittest.TestCase):
    def test_tokens_basicos(self):
        tokens = tokenize("x = 10 + 2")
        tipos = [t.tipo for t in tokens]
        self.assertEqual(tipos, ['ID', 'ASSIGN', 'NUM', 'PLUS', 'NUM'])

if __name__ == '__main__':
    unittest.main()