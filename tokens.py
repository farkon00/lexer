from dataclasses import dataclass
from enum import Enum, auto

class TokenType(Enum):
    IDENTIFIER = auto()
    KEYWORD = auto()
    INTEGER = auto()
    SEMICOLON = auto()
    OPEN_BLOCK = auto()
    CLOSE_BLOCK = auto()
    OPEN_PAREN = auto()
    CLOSE_PAREN = auto()
    OPEN_BRACKET = auto()
    CLOSE_BRACKET = auto()  
    COMMA = auto()
    ASSIGN = auto()
    DOT = auto()
    STRING = auto()
    OPERATOR = auto()

@dataclass
class Loc:
    line: int
    column: int
    index: int
    file: str

    def __str__(self):
        return f"{self.file}:{self.line}:{self.column}"

@dataclass
class Token:
    type: TokenType
    value: str
    loc: Loc