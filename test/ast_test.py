from unittest import TestCase

from YachayLP.ast import ExpressionStatement, Identifier, Integer, LetStatement, Program, ReturnStatement
from YachayLP.token import Token, TokenType

class ASTTest(TestCase):

    def test_let_statement(self) -> None:
        program: Program = Program(statements=[
            LetStatement(
                token=Token(TokenType.LET, literal='var'),
                name=Identifier(
                    token=Token(TokenType.IDENT, literal='mi_var'),
                    value='mi_var'
                ),
                value=Identifier(
                    token=Token(TokenType.IDENT, literal='otra_var'),
                    value='otra_var'
                )
            ),
        ])
        
        program_str = str(program)

        self.assertEquals(program_str, 'var mi_var = otra_var;')

    def test_return_statement(self) -> None:
        program: Program = Program(statements=[
            ReturnStatement(
                token=Token(TokenType.RETURN, literal='return'),
                return_value=Identifier(
                    token=Token(TokenType.IDENT, literal='mi_var'),
                    value='mi_var'
                )
            ),
        ])

        program_str = str(program)

        self.assertEquals(program_str, 'return mi_var;')

    def test_integer_expressions(self) -> None:
        program: Program = Program(statements=[
            ExpressionStatement(
                token=Token(TokenType.INT, literal='5'),
                expression=Integer(
                    token=Token(TokenType.INT, literal='5'),
                    value=5
                )
            ),
        ])
        
        program_str = str(program)

        self.assertEquals(program_str, '5')