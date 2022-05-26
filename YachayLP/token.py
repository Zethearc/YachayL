from enum import auto, Enum, unique
from tkinter.tix import AUTO
from typing import NamedTuple, Dict

@unique
class TokenType(Enum):
    """Tokens used by YachayLP"""
    ASSIGN = auto()         # Assing Operator "="
    COMMA = auto()          # Comma ","
    DIVISION = auto()       # Division Operator "/"
    EOF = auto()
    ELSE = auto()
    FALSE = auto()
    FUNCTION = auto()
    GT = auto()
    IDENT = auto()          # Identifier
    IF = auto()
    ILLEGAL = auto()        # Illegal Token
    INT = auto()            # Integer
    LBRACE = auto()         # Delimiter "{"
    LET = auto()
    LPAREN = auto()         # Delimiter "("
    LT = auto()
    MINUS = auto()          # Sus operator "-"
    MULTIPLICATION = auto() # Multiplication operator "*"
    NOT = auto()
    PLUS = auto()           # Addition operator "+"
    RETURN = auto()
    RBRACE = auto()         # Delimiter "}"
    RPAREN = auto()         # Delimiter ")"
    SEMICOLON = auto()      # SemiColon ";"
    TRUE = auto()

class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}, Literal: {self.literal}'

def lookup_token_type(literal: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'False': TokenType.FALSE,
        'function': TokenType.FUNCTION,
        'return': TokenType.RETURN,
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'var': TokenType.LET,
        'True': TokenType.TRUE,
    }

    return keywords.get(literal, TokenType.IDENT)