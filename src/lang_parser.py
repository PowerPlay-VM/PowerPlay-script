from ast import expr
from sly import Parser
from lang_lexer import POWERPLAY_lexer
from lang_builtin import * 
from lang_ast import *
import logging



class POWERPLAY_parser(Parser):

    log = logging.getLogger()
    log.setLevel(logging.ERROR)

    tokens = POWERPLAY_lexer.tokens

    precedence = (
       ('left', PLUS, MINUS),
       ('left', TIMES, DIVIDE),
    )

    @_('expr expr')
    def expr(self, p):
        return Statements_node(p.expr0,p.expr1)

    @_('expr PLUS expr')
    def expr(self, p):
        return Add_node(p.expr0,p.expr1)

    @_('expr MINUS expr')
    def expr(self, p):
        return Sub_node(p.expr0,p.expr1)
    
    @_('expr TIMES expr')
    def expr(self, p):
        return Mul_node(p.expr0,p.expr1)
    
    @_('expr DIVIDE expr')
    def expr(self, p):
        return Div_node(p.expr0,p.expr1)

    @_('term')
    def expr(self, p):
        return p.term
    
    @_('expr EQ expr')
    def term(self, p):
        return Equal_node(p.expr0,p.expr1)

    @_('expr NE expr')
    def term(self, p):
        return Not_equal_node(p.expr0,p.expr1)
    
    @_('expr LT expr')
    def term(self, p):
        return Little_than_node(p.expr0,p.expr1)
        
    @_('expr LE expr')
    def term(self, p):
        return Little_equal_node(p.expr0,p.expr1)
    
    @_('expr GT expr')
    def term(self, p):
        return Greater_than_node(p.expr0,p.expr1)
    
    @_('expr GE expr')
    def term(self, p):
        return Greater_equal_node(p.expr0,p.expr1)

    @_('factor')
    def term(self, p):
        return p.factor

    @_('NUMBER')
    def factor(self, p):
        return Value_node(p.NUMBER)
    
    @_('STRING')
    def factor(self, p):
        return Value_node(p.STRING)

    @_('LPAREN expr RPAREN')
    def factor(self, p):
        return p.expr
    
    @_('ID ASSIGN expr')
    def expr(self, p):
        return Assign_node(p.ID,p.expr)
    
    @_('ID')
    def factor(self, p):
        return Id_node(p.ID)

    @_('IF expr LBRACE expr RBRACE')
    def expr(self, p):
        return If_node(p.expr0,p.expr1,None)
    
    @_('IF expr LBRACE expr RBRACE ELSE LBRACE expr RBRACE')
    def expr(self, p):
        return If_node(p.expr0,p.expr1,p.expr2)
                    
    @_('ID LPAREN expr RPAREN')
    def expr(self, p):
        return Call_node(p.ID,p.expr)


