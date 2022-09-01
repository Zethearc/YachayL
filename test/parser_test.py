from unittest import TestCase

from YachayLP.lexer import Lexer
from YachayLP.parser import Parser
from YachayLP.ast import Program

class ParserTest(TestCase):
    
    def test_parse_program(self) -> None:
        source: str = 'var x = 5;'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
        
        program: Program = parser.parse_program()
        
        self.assertIsNotNone(program)
        self.assertIsInstance