from enum import auto, Enum, unique
from tkinter.tix import AUTO
from typing import NamedTuple

@unique
class TokenType(Enum):
    ASSIGN = auto()         # Assing Operator "="
    COMMA = auto()          # Comma ","
    DIVISION = auto()       # Division Operator "/"
    EOF = auto()
    FUNCTION = auto()
    IDENT = auto()          # Identifier
    ILLEGAL = auto()        # Illegal Token
    INT = auto()            # Integer
    LBRACE = auto()         # Delimiter "{"
    LET = auto()
    LPAREN = auto()         # Delimiter "("
    MINUS = auto()          # Sus operator "-"
    MULTIPLICATION = auto() # Multiplication operator "*"
    PLUS = auto()           # Addition operator "+"
    RBRACE = auto()         # Delimiter "}"
    RPAREN = auto()         # Delimiter ")"
    SEMICOLON = auto()       # SemiColon ";"

class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}, Literal: {self.literal}'