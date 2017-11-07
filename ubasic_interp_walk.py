# A tree walker to interpret ubasic programs

from ubasic_state import state
from grammar_stuff import assert_match

#########################################################################
# node functions
#########################################################################
# updated for ubasic
def seq(node):
    
    (SEQ, stmt, stmt_list) = node
    assert_match(SEQ, 'seq')
    
    walk(stmt)
    walk(stmt_list)

#########################################################################
def nil(node):
    
    (NIL,) = node
    assert_match(NIL, 'nil')
    
    # do nothing!
    pass

#########################################################################
# updated for ubasic
def print_stmt(node):
    (PRINT , value , value_list) = node
    assert_match(PRINT , 'print')

    msg = walk(value)

    if not value_list:
        print(msg)
    else:
        msg += str(walk(value_list))
        print(msg)

#########################################################################
# updated for ubasic
def assign_stmt(node):

    (ASSIGN, name, exp) = node
    assert_match(ASSIGN, 'assign')
    
    value = walk(exp)
    state.symbol_table[name] = value

#########################################################################
# updated for ubasic
def input_stmt(node):

    (PUT, opt_string, exp) = node
    assert_match(PUT, 'input')

    state.symbol_table[exp] = int(input(opt_string))
    
#########################################################################
def while_stmt(node):

    (WHILE, cond, body) = node
    assert_match(WHILE, 'while')
    
    value = walk(cond)
    while value != 0:
        walk(body)
        value = walk(cond)

#########################################################################
def if_stmt(node):
    
    try: # try the if-then pattern
        (IF, cond, then_stmt, (NIL,)) = node
        assert_match(IF, 'if')
        assert_match(NIL, 'nil')

    except ValueError: # if-then pattern didn't match
        (IF, cond, then_stmt, else_stmt) = node
        assert_match(IF, 'if')

        value = walk(cond)
        if value != 0:
            walk(then_stmt)
        else:
            walk(else_stmt)
        return
 
    else: # if-then pattern matched
        value = walk(cond)
        if value != 0:
            walk(then_stmt)
        return

#########################################################################
def else_stmt(node):
    (ELSE , stmt_list) = node
    assert_match(ELSE , 'else')

    walk(stmt_list)
#########################################################################
def block_stmt(node):
    
    (BLOCK, stmt_list) = node
    assert_match(BLOCK, 'block')
    
    walk(stmt_list)

#########################################################################
def plus_exp(node):
    
    (PLUS,c1,c2) = node
    assert_match(PLUS, '+')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return v1 + v2

#########################################################################
def minus_exp(node):
    
    (MINUS,c1,c2) = node
    assert_match(MINUS, '-')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return v1 - v2

#########################################################################
def times_exp(node):
    
    (TIMES,c1,c2) = node
    assert_match(TIMES, '*')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return v1 * v2

#########################################################################
def divide_exp(node):
    
    (DIVIDE,c1,c2) = node
    assert_match(DIVIDE, '/')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return v1 // v2

#########################################################################
def eq_exp(node):
    
    (EQ,c1,c2) = node
    assert_match(EQ, '==')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return 1 if v1 == v2 else 0

#########################################################################
def le_exp(node):
    
    (LE,c1,c2) = node
    assert_match(LE, '<=')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return 1 if v1 <= v2 else 0

#########################################################################
def integer_exp(node):

    (INTEGER, value) = node
    assert_match(INTEGER, 'integer')
    
    return value

#########################################################################
def id_exp(node):
    
    (ID, name) = node
    assert_match(ID, 'id')
    
    return state.symbol_table.get(name, 0)

#########################################################################
def uminus_exp(node):
    
    (UMINUS, exp) = node
    assert_match(UMINUS, 'uminus')
    
    val = walk(exp)
    return - val

#########################################################################
def not_exp(node):
    
    (NOT, exp) = node
    assert_match(NOT, 'not')
    
    val = walk(exp)
    return 0 if val != 0 else 1

#########################################################################
def paren_exp(node):
    
    (PAREN, exp) = node
    assert_match(PAREN, 'paren')
    
    # return the value of the parenthesized expression
    return walk(exp)


#########################################################################
# updated for ubasic
def end_stmt(node):
    (END,) = node
    assert_match(END , 'exit')
    
    # do nothing
    quit()

#########################################################################
def for_stmt(node):
    pass

#########################################################################
def value_list(node):
    (VALUE_LIST , value , value_list) = node
    assert_match(VALUE_LIST , 'value_list')
    
    # if value list is None, we can just return value
    if not value_list:
        return walk(value)
    
    values = walk(value_list)
    return value + value_list
#########################################################################
def val_id(node):
    (ID , val) = node
    assert_match(ID , 'id')

    return state.symbol_table[val]
##########################################################################
def val_integer(node):
    (INTEGER , val) = node
    assert_match(INTEGER , 'integer')

    return val
##########################################################################
def val_string(node):
    (STRING , val) = node
    assert_match(STRING , 'string')

    return val


#########################################################################
# walk
#########################################################################
def walk(node):
    # node format: (TYPE, [child1[, child2[, ...]]])
    type = node[0]
    
    if type in dispatch_dict:
        node_function = dispatch_dict[type]
        return node_function(node)
    else:
        raise ValueError("walk: unknown tree node type: " + type)

# a dictionary to associate tree nodes with node functions
'''
dispatch_dict = {
    'seq'     : seq,
    'nil'     : nil,
    'assign'  : assign_stmt,
    'get'     : get_stmt,
    'put'     : put_stmt,
    'while'   : while_stmt,
    'if'      : if_stmt,
    'block'   : block_stmt,
    'integer' : integer_exp,
    'id'      : id_exp,
    'paren'   : paren_exp,
    '+'       : plus_exp,
    '-'       : minus_exp,
    '*'       : times_exp,
    '/'       : divide_exp,
    '=='      : eq_exp,
    '<='      : le_exp,
    'uminus'  : uminus_exp,
    'not'     : not_exp
}
'''

dispatch_dict = {
    'seq'   : seq,
    'nil'   : nil,
    'assign' : assign_stmt,
    'input'     : input_stmt,
    'print'     : print_stmt,
    'exit'       : end_stmt,
    'if'        : if_stmt,
    'else'      : else_stmt,
    'while'     : while_stmt,
    'for'       : for_stmt,
    'value_list' : value_list,
    'id'        : val_id,
    'integer'   : val_integer,
    'string'    : val_string,
    '+'         : plus_exp,
    '-'         : minus_exp,
    '*'         : times_exp,
    '/'         : divide_exp,
    '=='        : eq_exp,
    '<='        : le_exp,
    'uminus'    : uminus_exp,
    'not'       : not_exp
        
        
        
}


