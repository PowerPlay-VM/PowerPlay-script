from sly import Lexer

class POWERPLAY_lexer(Lexer):
    tokens = { NUMBER, STRING, ID, WHILE, IF, ELSE, FOR, PRINT,
               PLUS, MINUS, TIMES, DIVIDE, ASSIGN, LPAREN, RPAREN, LBRACE, RBRACE,
               EQ, LT, LE, GT, GE, NE }


    literals = { '(', ')', '{', '}', ';' }

    ignore = ' \t'

    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    LPAREN  = r'\('
    RPAREN  = r'\)'
    LBRACE  = r'\{'
    RBRACE  = r'\}'
    EQ      = r'=='
    ASSIGN  = r'='
    LE      = r'<='
    LT      = r'<'
    GE      = r'>='
    GT      = r'>'
    NE      = r'!='

    @_(r'\d+(?:\.\d+)?')
    def NUMBER(self, t):
        t.value = float(t.value)

        if (t.value).is_integer():
            t.value = int(t.value)

        return t
    
    @_(r'\".*\"')
    def STRING(self, t):
        t.value = str(t.value).strip('\"')

        return t

    # Identifiers and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['for'] = FOR

    ignore_comment = r'\#.*'

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

