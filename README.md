# Compilador MiniCalc 🧮

Este repositório contém o projeto final da disciplina de Teoria da Computação e Compiladores (Projeto A3). Trata-se de um protótipo funcional de um compilador (transpilador) desenvolvido do zero, que ilustra os conceitos de análise léxica, análise sintática e geração de código.

## 🎯 Sobre o Projeto

O MiniCalc é uma linguagem matemática simples que suporta atribuição de variáveis e impressão de resultados. O compilador processa arquivos com a extensão .calc e gera código Python 3 válido como saída.

O projeto foi construído em fases estritas e modulares:

Analisador Léxico (Scanner): Utiliza expressões regulares (re) para converter o código-fonte bruto em Tokens.

Analisador Sintático (Parser): Utiliza a técnica de Descida Recursiva Preditiva para validar a gramática LL(1) e gerar uma Árvore Sintática Abstrata (AST).

Gerador de Código (CodeGen): Percorre a AST e transpila a estrutura validada para código Python executável.

## 🛠️ Tecnologias Utilizadas

Python 3 (Linguagem base)

Expressões Regulares (re)

Testes Unitários (unittest)

## 📂 Estrutura do Repositório

| Pastas | O que tem |
| ------------- |:-----------------------------------------------------------------------------------:|
| minicalc/     | Módulos do núcleo do compilador (lexer.py, parser.py, ast_nodes.py, codegen.py).    |
| examples/     | Códigos-fonte de exemplo na linguagem MiniCalc (.calc).                             |
| tests/        | Bateria de testes unitários para cada fase.                                         |
| docs/         | Documentação técnica e relatórios do projeto.                                       |


## 🚀 Como Executar

Certifique-se de ter o Python 3 instalado em sua máquina.

Clone o repositório:
```
git clone https://github.com/Tizuey/minicalc_TrilhaDeAprendizado
cd minicalc_TrilhaDeAprendizado
```

Execute o compilador passando um arquivo de exemplo:
```
python main.py examples/ex2_precedencia.calc
```

## 🧪 Como Rodar os Testes

Para garantir que todas as fases (Léxica, Sintática e CodeGen) estão funcionando isoladamente, execute:

```
python -m unittest discover
```

