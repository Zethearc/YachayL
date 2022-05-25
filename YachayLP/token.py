from enum import auto, Enum, unique
from tkinter.tix import AUTO
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
    LET = auto()
    LPAREN = auto()
    PLUS = auto()
    RBRACE = auto()
    RPAREN = auto()
    SEMCLON = auto()

