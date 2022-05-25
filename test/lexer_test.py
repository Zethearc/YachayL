from unittest import TestCase
from typing import List
from YachayLP.token import Token, TokenType
from YachayLP.lexer import Lexer

class LexerTest(TestCase):

    def test_illegal(self) -> None:
        source: str = '¡¿@'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
                Token(TokenType.ILLEGAL, '¡'),
                Token(TokenType.ILLEGAL, '¿'),
                Token(TokenType.ILLEGAL, '@'),
        ]
        self.assertEqual(tokens, expected_tokens)