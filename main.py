import sys

from lexer import Lexer
from printer import print_tokens

def main():
    with open(sys.argv[1], "r") as f:
        lexer = Lexer(f.read())

    tokens = lexer.lex()
    print_tokens(tokens)

if __name__ == "__main__":
    main()