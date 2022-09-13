from unittest import TestCase

from YachayLP.lexer import Lexer
from YachayLP.parser import Parser
from YachayLP.ast import LetStatement, Program

class ParserTest(TestCase):
    
    def test_parse_program(self) -> None:
        source: str = 'var x = 5;'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
        
        program: Program = parser.parse_program()
        
        self.assertIsNotNone(program)
        self.assertIsInstance
    
    def test_let_statements(self) -> None:
        source: str = '''
            var x = 5;
            var y = 10;
            var foo = 20;
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
        
        program: Program = parser.parse_program()
        
        for statement in program.statements:
            self.assertEqual(statement.token_literal(), 'variable')
            self.assertIsInstance(statement, LetStatement)