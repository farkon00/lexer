import sys

from lexer import Lexer
from printer import print_tokens

def main():
    if len(sys.argv) < 2:
        print("ERROR: No input file provided.")
        exit(1)

    with open(sys.argv[1], "r") as f:
        lexer = Lexer(f.read(), sys.argv[1])

    tokens = lexer.lex()
    print_tokens(tokens)

if __name__ == "__main__":
    main()