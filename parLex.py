#SEGURA RONNY

import ply.lex as lex

# Nuestro proyecto va direccionado a la construccion de puentes, facilitaremos el calculo de
# encontrar las dimensiones de los tirantes sabiendo el tipo de geometría parabólica (y=ax^2 +bx +c) que este tiene.

# Crear listas de tokens que se va utilizar
class LA(object):
    tokens = ['TEXT', 'ID', 'EQUALS','NUMBER', 'POT', 'PLUS', 'MINUS', 'DIVIDE','TIMES',
              'LPARENT','RPARENT','COMMA','COLOM','UNEQUALS',
              'LKEY','RKEY','PERCENT', 'BOOL','COMPARATOR','DOT','LCOR','RCOR',
              'LT', 'GT', 'LTE', 'GTE', 'OR', 'AND', 'WHILE', 'FOR', 'IF', 'IN', 'LEN',
              'PRINT', 'INPUT', 'INT', 'BREAK', 'CADENA', 'RANGE']

    t_ignore = ' \t\n'
    t_TEXT = r'[a-z][a-z]*'
    t_PLUS = r'\+'
    t_POT = r'(\*{2} | \^)'
    t_EQUALS = r'='
    t_UNEQUALS = r'!='
    t_MINUS = r'-'
    t_DIVIDE = r'/'
    t_TIMES = r'\*'
    t_LPARENT = r'\('
    t_RPARENT = r'\)'
    t_COMMA = r','
    t_COLOM = r':'
    t_AND = r'\&\&'
    t_OR = r'\|{2}'
    t_LT = r'<'
    t_GT = r'>'
    t_LTE = r'<='
    t_GTE= r'>='
    t_LCOR = r'\['
    t_RCOR = r'\]'
    t_DOT = r'\.'
    t_LKEY  = r'\{'
    t_RKEY = r'\}'
    t_PERCENT = r'%'
    t_BOOL = r'True|False'
    t_COMPARATOR = r'=='


    def t_WHILE(self, t):
        r'while'
        return t

    def t_FOR(self, t):
        r'for'
        return t

    def t_IF(self, t):
        r'if'
        return t

    def t_INT(self, t):
        r'int'
        return t

    def t_RANGE(self, t):
        r'range'
        return t

    def t_LEN(self, t):
        r'len'
        return t

    def t_PRINT(self, t):
        r'print'
        return t

    def t_INPUT(self, t):
        r'input'
        return t

    def t_BREAK(self, t):
        r'break'
        return t

    def t_IN(self, t):
        r'in'
        return t

    def t_ID(self, t):
        r'[A-Z][a-zA-Z0-9_]*'
       # t.type = reserved.get(t.value, 'ID')  # Check for reserved words
        return t

    def t_COMMENT(self, t):
        r'\#.*'
        pass

    def t_CADENA(self, t):
       r'\"(\w+ \ *\w*\d* \ *)\"'
       return t

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t


    def t_error(self, t):
        print ("caracter ilegal '%s' "%t.value[0])
        t.lexer.sikip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def tokenize(self, data):
        tkns = []
        self.lexer.input(data)
        while (True):
            tok = self.lexer.token()
            if not tok:
                break
            if (tok.type != 'newline'):
                tkns.append([tok.type, tok.value])
        return (tkns)


#lex.lex()



#lex.input("x=3*4+5*6")
#while True:
#    tok = lex.token()
#    print(tok)
#    if not tok : break