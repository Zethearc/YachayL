from re import match

from YachayLP.token import Token, TokenType

# REGULAR EXPRESIONS

## OPERATORS

t_ASSING  = r'^=$'
t_PLUS    = r'\+$'
t_MINUS   = r'^-$'
t_TIMES   = r'^\*$'
t_DIV     = r'^/$'
t_VOID    = r'^$'

## DELIMITERS

t_LPAREN  = r'^\($'
t_RPAREN  = r'^\)$'
t_LBRACE  = r'^\{$'
t_RBRACE  = r'^\}$'
t_COMMA   = r'^\,$'
t_SEMICOLON   = r'^;$'

class Lexer:

    def __init__(self, source: str) -> None:
        self._source: str = source
        self._character: str = ''
        self._read_position: int = 0
        self._position: int = 0

        self._read_character()

    def next_token(self) -> Token:
        if match(t_ASSING, self._character):
            token = Token(TokenType.ASSIGN, self._character)
        elif match(t_PLUS, self._character):
            token = Token(TokenType.PLUS, self._character)
        elif match(t_MINUS, self._character):
            token = Token(TokenType.MINUS, self._character)
        elif match(t_TIMES, self._character):
            token = Token(TokenType.MULTIPLICATION, self._character)
        elif match(t_DIV, self._character):
            token = Token(TokenType.DIVISION, self._character)
        elif match(t_LPAREN, self._character):
            token = Token(TokenType.LPAREN, self._character)
        elif match(t_RPAREN, self._character):
            token = Token(TokenType.RPAREN, self._character)
        elif match(t_LBRACE, self._character):
            token = Token(TokenType.LBRACE, self._character)
        elif match(t_RBRACE, self._character):
            token = Token(TokenType.RBRACE, self._character)
        elif match(t_COMMA, self._character):
            token = Token(TokenType.COMMA, self._character)
        elif match(t_SEMICOLON, self._character):
            token = Token(TokenType.SEMICOLON, self._character)
        elif match(t_VOID, self._character):
            token = Token(TokenType.EOF, self._character)
        else:
            token = Token(TokenType.ILLEGAL, self._character)

        self._read_character()

        return token

    def _read_character(self) -> None:
        if self._read_position >= len(self._source):
            self._character = ''
        else:
            self._character = self._source[self._read_position]

        self._position = self._read_position
        self._read_position += 1