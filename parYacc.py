#SEGURA RONNY
from tkinter import *
from tkinter import ttk
import ply.yacc as yacc
from parLex import LA
tokens = LA.tokens

precedence =(
    ('left', 'PLUS', 'MINUS'),
    ('left', 'LPARENT', 'RPARENT'),
    ('nonassoc','UMINUS'),
    ('left', 'LT','LTE','GT','GTE'),
    #('nonassoc','POT'),
)

def p_program(p):
    '''program : statement
                | statement program'''
    if (len(p) == 3):
        p[0] = ("Progra", p[1], p[2])
    else:
        p[0] = ("Progra", p[1])

def p_statement(p):
    '''statement : assing
                  | statementWhile
                  | statementFor
                  | statementIf
                  | callPrint
                  | callInput
                  | BREAK'''
    p[0] = p[1]

def p_assing(p):
    '''assing : id EQUALS expr
                | id EQUALS callInput
                | id PLUS PLUS
                | id MINUS MINUS'''
    if p[2] == '=':
        p[0] = ("Assignation", p[1], str(p[2]), p[3])
    else:
        p[0] = ("AutoId", p[1], p[2], p[3])

def p_id(p):
    'id : ID'
    p[0] = ("Identificador", p[1])

def p_expr(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term'''
    if (len(p) == 4):
        p[0] = ("Operation",p[1], str(p[2]), p[3])
    else:
        p[0] = ("Expresion", p[1])

def p_expr_uminus(p):
    'expr : MINUS expr %prec UMINUS'
    p[0] = -p[1]

def p_term(p):
    '''term : term TIMES factor
            | term POT factor
            | term DIVIDE factor
            | term PERCENT factor
            | factor'''
    if (len(p) == 4):
        p[0] = ("Operation2", p[1], str(p[2]), p[3])
    else:
        p[0] =  p[1]


#detecta textos numeros
def p_factor(p):
    '''factor : NUMBER
                | ID
                | TEXT
                | CADENA
                | group'''
    p[0] = ("Valor", p[1])


#llamada de funciones print
def p_callPrint(p):
    '''callPrint : PRINT LPARENT term COMMA ID RPARENT
                 | PRINT group
                 | PRINT LPARENT RPARENT
                 | callPrint statement'''
    if (len(p) == 7):
        p[0] = ("Print", p[3], ",", p[5])
    elif (len(p) == 3):
        p[0] = ("Print", p[2])
    else:
        p[0] = ("Print", "new line")

#gramatica del grupo de expresiones a usar
def p_group(p):
    '''group : LPARENT expr RPARENT'''
    p[0] = ("FormGroup", str(p[1]), p[2], str(p[3]))

#llamada de funciones imput
def p_callInput(p):
    '''callInput : INPUT group
                 | int LPARENT INPUT group RPARENT
                 | callInput statement'''
    if (len(p) == 3):
        p[0] = ("Input", p[2])
    else:
        p[0] = ("IntInput", str(p[1]),p[4])

def p_break(p):
    'break : BREAK'
    p[0] = ("break")

def p_int(p):
    'int : INT'
    p[0] = ("Integer", p[1])

#llamada de funciones IF
def p_statementIf(p):
    '''statementIf : IF condition  COLOM statement'''
    p[0] = ("if", p[2], p[4])


#gramatica que valida el while
def p_statementWhile(p):
    '''statementWhile : WHILE condition COLOM statement
                      | WHILE condition COLOM statement break
                      | WHILE condition COLOM statement break statement'''
    if (len(p) == 5):
        p[0] = ("IteratoWhile", p[2], ":", p[4])
    elif (len(p) == 7):
        p[0] = ("IteratoWhile", p[2], ":", p[4], p[5], p[6])
    else:
        p[0] = ("IteratoWhile", p[2], ":", p[4], p[5])

#gramatkca para condiciones
def p_condition(p):
    '''condition : comparation
                | comparation andor condition '''
    if len(p)==4:
        p[0] = ("Condition", p[1], p[2],p[3])
    else:
        p[0] = ("Condition", p[1])

#valoda las comparaciones menor, mayor, igual
def p_comparation(p):
    '''comparation : factor compara factor'''
    p[0] = ("Comparation", p[1], p[2], p[3])

def p_compara(p):
    '''compara :  LT
            | GT
            | LTE
            | GTE
            | COMPARATOR
            | UNEQUALS'''
    p[0] = ("Compara", p[1])

def p_andor(p):
    '''andor : OR
             | AND'''
    p[0] = ("andor", p[1])

#gramatica que valida el for
def p_statementFor(p):
    '''statementFor : FOR TEXT IN ID COLOM statement
                    | FOR TEXT IN form'''
    p[0] = ("For", p[2], p[3], p[4])

def p_form(p):
    '''form : RANGE LPARENT NUMBER RPARENT COLOM statement
            | RANGE LPARENT ID RPARENT COLOM
            | RANGE LPARENT LEN LPARENT id RPARENT RPARENT COLOM statement'''
    if (len(p) == 9):
        p[0] = ("GroupRangeLen", p[1], p[3],p[5],str(p[8]),p[9])
    elif (len(p) == 7):
        p[0] = ("GroupRange", p[1], p[3],str(p[5]),p[6])
    else:
        p[0] = ("Groupfor", p[1], str(p[2]),p[3])

def p_error(p):
    #print("error de sintaxis",p)
    #print("error de linea "+ str(p.lineno))
    try:
        if p:

            print("Error sintactico de tipo {} en el valor {} en la linea {}" .format(str(p.type), str(p.value), str(p.lineno)))

            #txterror.delete(1.0, END)
            txtsemantic.delete(1.0, END)
            txterror.insert(END, "Error sintactico de tipo {} valor {} linea {}".format(str(p.type), str(p.value), str(p.lineno)) + "\n")

    except:
        #txterror.delete(1.0, END)
        txtsemantic.delete(1.0, END)
        print("Error sintactico {} linea {}".format(str(p.type), str(p.lineno)))
        txterror.insert(END, "Error sintactico {} linea {}".format(str(p.type), str(p.lineno)))

l = LA()
le = l.build()

parser = yacc.yacc()
#result = parser.parse("for a in range(5): print() ")
#print(result)

raiz = Tk()
raiz.geometry('1500x700')
raiz.configure(bg = 'sky blue')
raiz.title('PROYECTO LP')

# Controles
message = Message(raiz, text="Bienvenido al Analizador", width=150)
message.grid(column=5, row=0)

lblPrograma1 = Label(raiz, text='Programa')
lblPrograma1.place(x=250, y=25, width=350, height=25)
txtPrograma1 = Text(raiz)
txtPrograma1.place(x=250, y=50, width=350, height=300)

lbllexico2 = Label(raiz, text='Analisis Lexico')
#lbllexico2.place(x=775, y=75, width=250, height=25)
lbllexico2.place(x=50, y=375, width=300, height=25)
txtlexico = Text(raiz)
#txtlexico.place(x=775, y=100, width=250, height=220)
txtlexico.place(x=50, y=400, width=300, height=220)

lblsemantic = Label(raiz, text='Analisis Sintactico')
lblsemantic.place(x=500, y=375, width=300, height=25)
txtsemantic = Text(raiz)
txtsemantic.place(x=500, y=400, width=300, height=220)

lblerror = Label(raiz, text='Error')
lblerror.place(x=900, y=250, width=350, height=25)
txterror = Text(raiz)
txterror.place(x=900, y=275, width=350, height=150)

ast = txtPrograma1.get(1.0, END)

def lexico():
    txterror.delete(1.0, END)
    data = txtPrograma1.get(1.0,END)
    tks = l.tokenize(data)
    txtlexico.delete(1.0,END)
    txtlexico.insert(1.0,tks)

def sintactico():
    txterror.delete(1.0, END)
    data = txtPrograma1.get(1.0, END)
    global ast
    ast = parser.parse(data, lexer=le)
    txtsemantic.delete(1.0, END)
    txtsemantic.insert(1.0, ast)

def clear():
    txterror.delete(1.0, END)
    txtPrograma1.delete(1.0, END)
    txtsemantic.delete(1.0, END)
    txtlexico.delete(1.0, END)

#btnClear = Button(raiz, text='Clear', command=lambda :txtPrograma1.delete(1.0,END))
btnClear = Button(raiz, text='Clear', command=clear)
btnClear.place(x=375, y=450, width=100, height=25)
btnLexico = Button(raiz, text='léxico', command=lexico)
btnLexico.place(x=375, y=400, width=100, height=25)
btnSintactico = Button(raiz, text='Sintáctico', command=sintactico)
btnSintactico.place(x=375, y=500, width=100, height=25)

raiz.mainloop()
