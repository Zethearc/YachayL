from unittest import TestCase
from typing import List
from Tokens.token import (
    Token,
    TokenType,   
)
from Token.lexer import Lexer

class LexerTest(TestCase):
    def test_illegals(self) -> None:
        source: str = '@'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source):)
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] =[
            Token(TokenType.ILLEGAL, '@')
        ]

        self.assertEquals(tokens, expected_tokens)