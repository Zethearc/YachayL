from typing import List

from YachayLP.ast import Program
from YachayLP.evaluator import evaluate
from YachayLP.lexer import Lexer
from YachayLP.object import Environment
from YachayLP.parser import Parser
from YachayLP.token import (
    Token,
    TokenType,
)


EOF_TOKEN: Token = Token(TokenType.EOF, '')


def _print_parse_errors(errors: List[str]):
    for error in errors:
        print(error)

def start_repl() -> None:
    scanned: List[str] = []

    while (source := input('>> ')) != 'salir()':
        scanned.append(source)
        lexer: Lexer = Lexer(' '.join(scanned))
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()
        env: Environment = Environment()

        if len(parser.errors) > 0:
            _print_parse_errors(parser.errors)
            continue

        evaluated = evaluate(program, env)

        if evaluated is not None:
            print(evaluated.inspect())