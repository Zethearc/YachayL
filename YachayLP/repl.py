from typing import List
from YachayLP.lexer import Lexer
from YachayLP.evaluator import evaluate
from YachayLP.token import Token, TokenType
from YachayLP.parser import Parser

EOF_TOKEN: Token = Token(TokenType.EOF, '')

def _print_parse_errors(errors: List[str]):
    for error in errors:
        print(error)

def start_repl() -> None:
    while (source := input('>> ')) != 'salir()':
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        if len(parser.errors) > 0:
            _print_parse_errors(parser.errors)
            continue

        evaluated = evaluate(program)

        if evaluated is not None:
            print(evaluated.inspect())