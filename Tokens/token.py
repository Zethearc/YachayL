from enum import (
    auto,
    Enum,
    unique
    )
from typing import NamedTuple

@unique
class TokenType(Enum):
    ASSING = auto()
    COMMA = auto()
    EOF = auto()
    FUNCTION = auto()
    IDENT = auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LET = auto()    # Inicializate
    LPAREN = auto()
    PLUS = auto()   # Plus Operator
    RBRACE = auto()
    RPAREN = auto()
    SEMICOLON = auto()

class Token(NamedTuple):
    token_tyoe: TokenType
    literal: str
    
    def __str__(self) -> str:
        return f'Type: {self.token_tyoe}, Literal: {self.literal}'