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
    
    def test_one_character_operator(self) -> None:
        source: str = '=+'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.MINUS, '-'),
            Token(TokenType.DIVISION, '/'),
            Token(TokenType.MULTIPLICATION, '*'),
        ]

        self.assertEquals(tokens, expected_tokens)
'''
    def test_eof(self) -> None:
        source: str = '+'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(len(source) + 1):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.PLUS, '+'),
            Token(TokenType.EOF, ''),
        ]
        
        self.assertEquals(tokens, expected_tokens)'''