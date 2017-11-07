from ubasic_gram import parser
from ubasic_lex import lexer
from ubasic_state import state
from grammar_stuff import dump_AST
from ubasic_interp_walk import walk

msg =\
'''
    input "enter value for a: " , a
    if a == 5 then
        print "a is equal to 5"
        print "goodbye"
    else
        print "a is not equal to 5"
        print "suck on that"
    endif
'''

msg2 = \
'''
    input "Enter a value for variable x: " , x
    print "The value of variable x is " , x
'''

msg3 = \
'''
    a = 1
    while a <= 100
        print a
        a = a + 1
    endwhile
'''

testEnd = \
'''
    a = 1
    while a <= 10
        print a
        a = a + 1
        if a == 7 then
            end
        endif
    endwhile
'''

testErr = \
'''
    input "enter value for a"
'''

parser.parse(testEnd , lexer=lexer)
print(state.AST)
dump_AST(state.AST)
walk(state.AST)
#print(state.symbol_table)

