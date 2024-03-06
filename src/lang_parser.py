from sly import Parser
from lang_lexer import POWERPLAY_lexer
from lang_builtin import * 
import logging



class POWERPLAY_parser(Parser):

    log = logging.getLogger()
    log.setLevel(logging.ERROR)

    tokens = POWERPLAY_lexer.tokens

    @_('expr PLUS term')
    def expr(self, p):
        return p.expr + p.term

    @_('expr MINUS term')
    def expr(self, p):
        return p.expr - p.term

    @_('term')
    def expr(self, p):
        return p.term

    @_('term TIMES factor')
    def term(self, p):
        return p.term * p.factor

    @_('term DIVIDE factor')
    def term(self, p):
        return p.term / p.factor

    @_('factor')
    def term(self, p):
        return p.factor

    @_('NUMBER')
    def factor(self, p):
        return p.NUMBER

    @_('LPAREN expr RPAREN')
    def factor(self, p):
        return p.expr
    
    @_('ID ASSIGN expr')
    def expr(self, p):
        variables[p.ID] = p.expr
    
    @_('ID')
    def factor(self, p):
        return variables[p.ID]

    @_('ID LPAREN expr RPAREN')
    def expr(self, p):
        functions[p.ID](p.expr)

    


