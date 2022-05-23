from enum import (
    auto,
    Enum,
    unique
    )
from typing import NameTuple

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

class Token(NameTuple):
    token_tyoe: TokenType
    litelar: str
    
    def __str__(self) -> str:
        return f'Type: {self.token_type}, Literal: {self.literal}'