from dataclasses import dataclass
from enum import Enum, auto

class TokenType(Enum):
    IDENTIFIER = auto()
    KEYWORD = auto()
    INTEGER = auto()

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