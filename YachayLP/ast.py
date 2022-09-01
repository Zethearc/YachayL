from abc import (ABC, abstractmethod)
from typing import List
from YachayLP.token import Token

class ASTNode(ABC):
    
    @abstractmethod
    def token_literal(self)-> str:
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        pass
    
class Statement(ASTNode):
    
    def __init__(self, token: Token) -> None:
        self.token = token
        
    def token_literal(self) -> str:
        return self.token_literal
    
class Expression(ASTNode):
    
    def __init__(self, token: Token) -> None:
        self.token = token
        
    def token_literal(self) -> str:
        return self.token_literal
    
class Program(ASTNode):
    
    def __init__(self, statements: List[Statement]) -> None:
        self.statements = statements
        
    def token_literal(self) -> str:
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        
        return ''
    
    def __str__(self) -> str:
        out: List[str] = []
        for statements in self.statements:
            out.append(str(statements))
            
        return ''.join(out)