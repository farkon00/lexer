from tokens import *

class Lexer:
    def __init__(self, code):
        self.code = code

    def lex(self) -> list[Token]:
        return [Token(TokenType.IDENTIFIER, "test", Loc(0, 0, ""))]