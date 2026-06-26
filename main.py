import sys
import os
from minicalc.lexer import tokenize
from minicalc.parser import Parser
from minicalc.codegen import Codegen


def main():

    # Define qual arquivo será compilado.
    # Se o usuário passar no terminal, usamos ele.
    # Caso contrário, usamos um arquivo de exemplo padrão.
    if len(sys.argv) > 1:
        caminho_arquivo = sys.argv[1]
    else:
        caminho_arquivo = "examples/ex2_precedencia.calc"

    # Verificação básica para evitar tentar abrir arquivo inexistente.
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        sys.exit(1)

    # Leitura do código fonte (entrada do compilador).
    with open(caminho_arquivo, 'r') as arquivo:
        codigo_fonte = arquivo.read()

    print(f"[{caminho_arquivo}] --- INICIANDO COMPILAÇÃO ---")

    try:
        # =========================
        # FASE 1: ANÁLISE LÉXICA
        # =========================
        print("\n[Fase 1] Gerando Tokens (Lexer)...")

        tokens = tokenize(codigo_fonte)

        # Mostra os tokens gerados (útil para debug do compilador)
        for t in tokens:
            print(f"  {t}")

        # =========================
        # FASE 2: ANÁLISE SINTÁTICA
        # =========================
        print("\n[Fase 2] Montando Árvore (Parser)...")

        parser = Parser(tokens)
        ast = parser.parse()

        # Representação simples da AST para conferência
        print(f"  {ast}")

        # =========================
        # FASE 3: GERAÇÃO DE CÓDIGO
        # =========================
        print("\n[Fase 3] Traduzindo para Python (CodeGen)...")

        gerador = Codegen()
        codigo_python = gerador.gerar(ast)

        print("\n=== CÓDIGO PYTHON GERADO ===")
        print(codigo_python)
        print("============================\n")

        # Execução direta do código gerado para validação
        print("=== EXECUTANDO O CÓDIGO GERADO ===")
        exec(codigo_python)

    except Exception as e:
        # Captura qualquer erro durante as fases do compilador
        print(f"\n[ERRO DE COMPILAÇÃO]: {e}")


if __name__ == "__main__":
    main()