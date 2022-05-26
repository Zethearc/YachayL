from re import match

from YachayLP.token import Token, TokenType, lookup_token_type

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

## LETTERS & NUMBERS

t_LETTERS = r'^[a-záéíóóA-ZÁÉÍÓÚñÑ_]$'
t_NUMBERS = r'^\d$'
t_WHITES = r'^\s$'

## BINARY OPERATORS

t_LT = r'^<$'
t_GT = r'^>$'

class Lexer:

    def __init__(self, source: str) -> None:
        self._source: str = source
        self._character: str = ''
        self._read_position: int = 0
        self._position: int = 0

        self._read_character()

    def next_token(self) -> Token:
        self._skip_whitespace()
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
        elif match(t_LT, self._character):
            token = Token(TokenType.LT, self._character)
        elif match(t_GT, self._character):
            token = Token(TokenType.GT, self._character)
        elif self._is_letter(self._character):
            literal = self._read_identifier()
            token_type = lookup_token_type(literal)

            return Token(token_type, literal)
        elif self._is_number(self._character):
            literal = self._read_number()

            return Token(TokenType.INT, literal)
        else:
            token = Token(TokenType.ILLEGAL, self._character)

        self._read_character()

        return token
    
    def _is_letter(self, character: str) -> bool:
        return bool(match(t_LETTERS, character))

    def _is_number(self, character: str) -> bool:
        return bool(match(t_NUMBERS, character))

    def _read_character(self) -> None:
        if self._read_position >= len(self._source):
            self._character = ''
        else:
            self._character = self._source[self._read_position]

        self._position = self._read_position
        self._read_position += 1
    
    def _read_identifier(self) -> str:
        initial_position = self._position
        
        while self._is_letter(self._character):
            self._read_character()
        
        return self._source[initial_position: self._position]
    
    def _read_number(self) -> str:
        initial_position = self._position

        while self._is_number(self._character):
            self._read_character()
        
        return self._source[initial_position:self._position]

    def _skip_whitespace(self) -> None:
        while match(t_WHITES, self._character):
            self._read_character()
