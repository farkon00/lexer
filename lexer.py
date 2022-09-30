from tokens import *

class Lexer:
    KEYWORDS = [
        "if", "else", "while", "func", "return", "var", "import"
    ]
    OPERATORS = [
        "+", "-", "*", "/", "&", "|", "!", "<", ">", "==", "="
    ]
    SPECIAL_SYMBOLS = {
        "{" : TokenType.OPEN_BLOCK, 
        "}" : TokenType.CLOSE_BLOCK, 
        "(" : TokenType.OPEN_PAREN,
        ")" : TokenType.CLOSE_PAREN,
        "[" : TokenType.OPEN_BRACKET,
        "]" : TokenType.CLOSE_BRACKET,
        "." : TokenType.DOT,
        "," : TokenType.COMMA,
        ";" : TokenType.SEMICOLON,
    }

    def __init__(self, code, file_name):
        self.code = code
        self.file_name = file_name

        self.tokens = []

        self.index = 0
        self.line = 1
        self.column = 1

        self.curr_iden = ""

        self.is_curr_iden = False
        self.is_eof = False

    def advance(self):
        self.column += 1
        self.index += 1
        if self.index >= len(self.code):
            self.is_eof = True
            return ""
        is_new_line = False
        while self.code[self.index] == "\n":
            self.line += 1
            self.column = 1
            self.index += 1
            is_new_line = True
        if is_new_line:
            self.index -= 1
        return self.code[self.index]

    def peek(self) -> str:
        return self.code[self.index]
    
    def prev(self) -> str:
        return self.code[self.index - 1] if self.index != 0 else ""

    def next(self) -> str:
        return self.code[self.index + 1] if self.index + 1 < len(self.code) else ""

    def is_space(self, char: str) -> bool:
        return char.isspace() or not char

    def get_loc(self) -> Loc:
        return Loc(self.line, self.column, self.index, self.file_name)

    def lex_int(self) -> Token:
        loc = self.get_loc()
        tok = self.peek()
        while self.next().isdigit():
            tok += self.advance()
        return Token(TokenType.INTEGER, tok, loc)

    def check_keyword(self, keyword: str):
        if self.code[self.index:self.index + len(keyword)] == keyword:
            self.index += len(keyword) - 1
            self.column += len(keyword) - 1
            self.advance()
            return True
        return False

    def check_keywords(self) -> Token | None:
        if not self.is_space(self.prev()):
            return

        loc = (self.line, self.column, self.index)

        for keyword in self.KEYWORDS:
            if self.check_keyword(keyword):
                return Token(TokenType.KEYWORD, keyword, Loc(*loc, self.file_name))

    def lex_string(self) -> Token:
        loc = self.get_loc()
        tok = ""
        while self.next() != "\"":
            tok += self.advance()
        self.advance()
        return Token(TokenType.STRING, tok, loc)

    def lex(self) -> list[Token]:
        while not self.is_eof:
            self.is_curr_iden = False
            tok = None
            keyword = self.check_keywords()
            if keyword is not None:
                tok = keyword
            elif self.peek() in self.OPERATORS:
                tok = Token(TokenType.OPERATOR, self.peek(), self.get_loc())
            elif self.peek() in self.SPECIAL_SYMBOLS:
                tok = Token(self.SPECIAL_SYMBOLS[self.peek()], self.peek(), self.get_loc())
            elif self.peek() == "\"":
                tok = self.lex_string()
            elif not self.curr_iden and self.peek().isdigit():
                tok = self.lex_int()
            else:
                if not self.is_space(self.peek()):
                    self.is_curr_iden = True
                    self.curr_iden += self.peek()
            self.advance()

            if not self.is_curr_iden and self.curr_iden:
                self.tokens.append(Token(TokenType.IDENTIFIER, self.curr_iden, self.get_loc()))
                self.curr_iden = ""

            if tok is not None:
                self.tokens.append(tok)
        if self.curr_iden:
            self.tokens.append(Token(TokenType.IDENTIFIER, self.curr_iden, self.get_loc()))
        
        return self.tokens
