# grammar for uBasic

from ply import yacc
from ubasic_lex import tokens, lexer
from ubasic_state import state

################################################################
# set precedence and associativity
# NOTE: all arithmetic operator need to have tokens
#       so that we can put them into the precedence table
precedence = (
              ('left', 'AND', 'OR'),
              ('left', 'EQ', 'LE'),
              ('left', 'PLUS', 'MINUS'),
              ('left', 'TIMES', 'DIVIDE'),
              ('right', 'UMINUS', 'NOT')
              )

################################################################
# gramar rules with embedded actions
################################################################

def p_prog(p):
    '''
    prog : stmt_list
    '''
    state.AST = p[1]

def p_stmt_list(p):
    '''
    stmt_list : stmt stmt_list
            | stmt
    '''
    if len(p) == 3:
        p[0] = ('seq' , p[1] , p[2])
    elif len(p) == 2:
        p[0] = p[1]

def p_stmt(p):
    '''
    stmt : ID '=' exp
         | INPUT opt_string ID
         | PRINT value value_list
         | END
         | IF exp THEN stmt_list opt_else ENDIF
         | WHILE exp stmt_list ENDWHILE
         | FOR ID '=' exp TO exp opt_step stmt_list NEXT ID
    '''
    if p[2] == '=':
        p[0] = ('assign' , p[1] , p[3])
    elif p[1] == 'input':
        p[0] = ('input' , p[2] , p[3])
    elif p[1] == 'print':
        p[0] = ('print' , p[2] , p[3])
    elif p[1] == 'end':
        p[0] = ('end')
    elif p[1] == 'if':
        p[0] = ('if' , p[2] , p[4], p[5]) 
    elif p[1] == 'while':
        p[0] = ('while' , p[2] , p[3])
    elif p[1] == 'for':
        p[0] = ('for' , p[2] , p[4] , p[6] , p[7] , p[8])

def p_opt_step(p):
    '''
    opt_step : STEP exp
             | empty
    '''
    if len(p) == 3:
        p[0] = ('step' , p[2])
    else:
        p[0] = p[1]



def p_opt_string(p):
    '''
    opt_string : STRING ','
               | empty
    '''
    p[0] = p[1]

def p_opt_else(p):
    '''
    opt_else : ELSE stmt_list
             | empty
    '''
    if len(p) == 3:
        p[0] = ('else' , p[2])
    else:
        p[0] = ('nil',)

def p_value_list(p):
    '''
    value_list : ',' value value_list
               | empty
    '''
    if len(p) == 4:
        p[0] = ('value_list' , p[2] , p[3])
    else:
        p[0] = p[1]

def p_value_id(p):
    '''
    value : ID
    '''
    p[0] = ('id' , p[1])

def p_value_integer(p):
    '''
    value : INTEGER
    '''
    p[0] = ('integer' , p[1])

def p_value_string(p):
    '''
    value : STRING
    '''
    p[0] = ('string' , p[1])

def p_exp_binary_exp(p):
    '''
    exp : exp PLUS exp
        | exp MINUS exp
        | exp TIMES exp
        | exp DIVIDE exp
        | exp EQ exp
        | exp LE exp
        | exp AND exp
        | exp OR exp
    '''
    p[0] = (p[2] , p[1] , p[3])

def p_exp_paren(p):
    '''
    exp : '(' exp ')'
    '''
    p[0] = ('paren' , p[2])

def p_uminus_exp(p):
    '''
    exp : MINUS exp %prec UMINUS
    '''
    p[0] = ('uminus' , p[2])

def p_not_exp(p):
    '''
    exp : NOT exp
    '''
    p[0] = ('not' , p[2])

def p_exp_integer(p):
    '''
    exp : INTEGER
    '''
    p[0] = ('integer' , int(p[1]))

def p_exp_id(p):
    '''
    exp : ID
    '''
    p[0] = ('id' , p[1])



def p_empty(p):
    'empty :'
    pass

def p_error(t):
    print("Syntax error at '%s'" % t.value)

### build the parser
parser = yacc.yacc(debug=False)
