from tokens import *

class Lexer:
    KEYWORDS = [
        "if", "else", "while", "func", "return", "var", "import"
    ]

    def __init__(self, code, file_name):
        self.code = code
        self.file_name = file_name

        self.tokens = []

        self.index = 0
        self.line = 1
        self.column = 1

        self.is_eof = False

    def advance(self):
        self.column += 1
        self.index += 1
        if self.index >= len(self.code):
            self.is_eof = True
            return ""
        if self.code[self.index] == "\n":
            self.line += 1
            self.column = 1
            return self.advance()
        return self.code[self.index]

    def peek(self):
        return self.code[self.index]
    
    def get_loc(self) -> Loc:
        return Loc(self.line, self.column, self.index, self.file_name)

    def check_keyword(self, keyword: str):
        if self.code[self.index:self.index + len(keyword)] == keyword:
            self.index += len(keyword) - 1
            return True
        return False

    def check_keywords(self) -> Token | None:
        for keyword in self.KEYWORDS:
            if self.check_keyword(keyword):
                return Token(TokenType.KEYWORD, keyword, self.get_loc())

    def lex(self) -> list[Token]:
        while not self.is_eof:
            keyword = self.check_keywords()
            if keyword is not None:
                self.tokens.append(keyword)
            self.advance()
        
        return self.tokens