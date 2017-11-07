from ubasic_gram import parser
from ubasic_lex import lexer
from ubasic_state import state
from grammar_stuff import dump_AST
from ubasic_interp_walk import walk

msg = 'input "Enter a value for x: " , x'
parser.parse(msg , lexer=lexer)
dump_AST(state.AST)
walk(state.AST)

