
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftANDORleftEQLEleftPLUSMINUSleftTIMESDIVIDErightUMINUSNOTPLUS MINUS TIMES DIVIDE EQ LE AND OR NOT INTEGER ID STRING INPUT PRINT END IF THEN ELSE ENDIF WHILE ENDWHILE FOR TO STEP NEXT\n    prog : stmt_list\n    \n    stmt_list : stmt stmt_list\n            | stmt\n    \n    stmt : ID '=' exp\n         | INPUT opt_string ID\n         | PRINT value value_list\n         | END\n         | IF exp THEN stmt_list opt_else ENDIF\n         | WHILE exp stmt_list ENDWHILE\n         | FOR ID '=' exp TO exp opt_step stmt_list NEXT ID\n    \n    opt_step : STEP exp\n             | empty\n    \n    opt_string : STRING ','\n               | empty\n    \n    opt_else : ELSE stmt_list\n             | empty\n    \n    value_list : ',' value value_list\n               | empty\n    \n    value : ID\n          | INTEGER\n          | STRING\n    \n    exp : exp PLUS exp\n        | exp MINUS exp\n        | exp TIMES exp\n        | exp DIVIDE exp\n        | exp EQ exp\n        | exp LE exp\n        | exp AND exp\n        | exp OR exp\n    \n    exp : '(' exp ')'\n    \n    exp : MINUS exp %prec UMINUS\n    \n    exp : NOT exp\n    \n    exp : INTEGER\n    \n    exp : ID\n    empty :"
    
_lr_action_items = {'ID':([0,3,5,6,7,8,9,10,12,13,15,16,17,18,19,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,47,48,50,51,52,53,54,55,56,57,58,59,61,63,65,66,68,69,70,71,73,74,75,],[4,4,-35,17,-7,25,25,27,25,29,-14,-35,-19,-20,-21,25,25,25,-33,-34,4,-4,-5,-13,-6,17,-18,4,25,25,25,25,25,25,25,25,-31,-32,25,-35,-22,-23,-24,-25,-26,-27,-28,-29,-30,-9,-17,4,25,-8,-35,4,25,-12,-11,75,-10,]),'INPUT':([0,3,7,16,17,18,19,24,25,26,28,29,31,33,34,43,45,48,50,51,52,53,54,55,56,57,58,59,61,63,66,68,69,71,73,75,],[5,5,-7,-35,-19,-20,-21,-33,-34,5,-4,-5,-6,-18,5,-31,-32,-35,-22,-23,-24,-25,-26,-27,-28,-29,-30,-9,-17,5,-8,-35,5,-12,-11,-10,]),'PRINT':([0,3,7,16,17,18,19,24,25,26,28,29,31,33,34,43,45,48,50,51,52,53,54,55,56,57,58,59,61,63,66,68,69,71,73,75,],[6,6,-7,-35,-19,-20,-21,-33,-34,6,-4,-5,-6,-18,6,-31,-32,-35,-22,-23,-24,-25,-26,-27,-28,-29,-30,-9,-17,6,-8,-35,6,-12,-11,-10,]),'END':([0,3,7,16,17,18,19,24,25,26,28,29,31,33,34,43,45,48,50,51,52,53,54,55,56,57,58,59,61,63,66,68,69,71,73,75,],[7,7,-7,-35,-19,-20,-21,-33,-34,7,-4,-5,-6,-18,7,-31,-32,-35,-22,-23,-24,-25,-26,-27,-28,-29,-30,-9,-17,7,-8,-35,7,-12,-11,-10,]),'IF':([0,3,7,16,17,18,19,24,25,26,28,29,31,33,34,43,45,48,50,51,52,53,54,55,56,57,58,59,61,63,66,68,69,71,73,75,],[8,8,-7,-35,-19,-20,-21,-33,-34,8,-4,-5,-6,-18,8,-31,-32,-35,-22,-23,-24,-25,-26,-27,-28,-29,-30,-9,-17,8,-8,-35,8,-12,-11,-10,]),'WHILE':([0,3,7,16,17,18,19,24,25,26,28,29,31,33,34,43,45,48,50,51,52,53,54,55,56,57,58,59,61,63,66,68,69,71,73,75,],[9,9,-7,-35,-19,-20,-21,-33,-34,9,-4,-5,-6,-18,9,-31,-32,-35,-22,-23,-24,-25,-26,-27,-28,-29,-30,-9,-17,9,-8,-35,9,-12,-11,-10,]),'FOR':([0,3,7,16,17,18,19,24,25,26,28,29,31,33,34,43,45,48,50,51,52,53,54,55,56,57,58,59,61,63,66,68,69,71,73,75,],[10,10,-7,-35,-19,-20,-21,-33,-34,10,-4,-5,-6,-18,10,-31,-32,-35,-22,-23,-24,-25,-26,-27,-28,-29,-30,-9,-17,10,-8,-35,10,-12,-11,-10,]),'$end':([1,2,3,7,11,16,17,18,19,24,25,28,29,31,33,43,45,48,50,51,52,53,54,55,56,57,58,59,61,66,75,],[0,-1,-3,-7,-2,-35,-19,-20,-21,-33,-34,-4,-5,-6,-18,-31,-32,-35,-22,-23,-24,-25,-26,-27,-28,-29,-30,-9,-17,-8,-10,]),'ENDWHILE':([3,7,11,16,17,18,19,24,25,28,29,31,33,43,45,46,48,50,51,52,53,54,55,56,57,58,59,61,66,75,],[-3,-7,-2,-35,-19,-20,-21,-33,-34,-4,-5,-6,-18,-31,-32,59,-35,-22,-23,-24,-25,-26,-27,-28,-29,-30,-9,-17,-8,-10,]),'ELSE':([3,7,11,16,17,18,19,24,25,28,29,31,33,43,45,48,49,50,51,52,53,54,55,56,57,58,59,61,66,75,],[-3,-7,-2,-35,-19,-20,-21,-33,-34,-4,-5,-6,-18,-31,-32,-35,63,-22,-23,-24,-25,-26,-27,-28,-29,-30,-9,-17,-8,-10,]),'ENDIF':([3,7,11,16,17,18,19,24,25,28,29,31,33,43,45,48,49,50,51,52,53,54,55,56,57,58,59,61,62,64,66,67,75,],[-3,-7,-2,-35,-19,-20,-21,-33,-34,-4,-5,-6,-18,-31,-32,-35,-35,-22,-23,-24,-25,-26,-27,-28,-29,-30,-9,-17,66,-16,-8,-15,-10,]),'NEXT':([3,7,11,16,17,18,19,24,25,28,29,31,33,43,45,48,50,51,52,53,54,55,56,57,58,59,61,66,72,75,],[-3,-7,-2,-35,-19,-20,-21,-33,-34,-4,-5,-6,-18,-31,-32,-35,-22,-23,-24,-25,-26,-27,-28,-29,-30,-9,-17,-8,74,-10,]),'=':([4,27,],[12,47,]),'STRING':([5,6,32,],[14,19,19,]),'INTEGER':([6,8,9,12,21,22,23,32,35,36,37,38,39,40,41,42,47,65,70,],[18,24,24,24,24,24,24,18,24,24,24,24,24,24,24,24,24,24,24,]),'(':([8,9,12,21,22,23,35,36,37,38,39,40,41,42,47,65,70,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'MINUS':([8,9,12,20,21,22,23,24,25,26,28,35,36,37,38,39,40,41,42,43,44,45,47,50,51,52,53,54,55,56,57,58,60,65,68,70,73,],[21,21,21,36,21,21,21,-33,-34,36,36,21,21,21,21,21,21,21,21,-31,36,-32,21,-22,-23,-24,-25,36,36,36,36,-30,36,21,36,21,36,]),'NOT':([8,9,12,21,22,23,35,36,37,38,39,40,41,42,47,65,70,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),',':([14,16,17,18,19,48,],[30,32,-19,-20,-21,32,]),'THEN':([20,24,25,43,45,50,51,52,53,54,55,56,57,58,],[34,-33,-34,-31,-32,-22,-23,-24,-25,-26,-27,-28,-29,-30,]),'PLUS':([20,24,25,26,28,43,44,45,50,51,52,53,54,55,56,57,58,60,68,73,],[35,-33,-34,35,35,-31,35,-32,-22,-23,-24,-25,35,35,35,35,-30,35,35,35,]),'TIMES':([20,24,25,26,28,43,44,45,50,51,52,53,54,55,56,57,58,60,68,73,],[37,-33,-34,37,37,-31,37,-32,37,37,-24,-25,37,37,37,37,-30,37,37,37,]),'DIVIDE':([20,24,25,26,28,43,44,45,50,51,52,53,54,55,56,57,58,60,68,73,],[38,-33,-34,38,38,-31,38,-32,38,38,-24,-25,38,38,38,38,-30,38,38,38,]),'EQ':([20,24,25,26,28,43,44,45,50,51,52,53,54,55,56,57,58,60,68,73,],[39,-33,-34,39,39,-31,39,-32,-22,-23,-24,-25,-26,-27,39,39,-30,39,39,39,]),'LE':([20,24,25,26,28,43,44,45,50,51,52,53,54,55,56,57,58,60,68,73,],[40,-33,-34,40,40,-31,40,-32,-22,-23,-24,-25,-26,-27,40,40,-30,40,40,40,]),'AND':([20,24,25,26,28,43,44,45,50,51,52,53,54,55,56,57,58,60,68,73,],[41,-33,-34,41,41,-31,41,-32,-22,-23,-24,-25,-26,-27,-28,-29,-30,41,41,41,]),'OR':([20,24,25,26,28,43,44,45,50,51,52,53,54,55,56,57,58,60,68,73,],[42,-33,-34,42,42,-31,42,-32,-22,-23,-24,-25,-26,-27,-28,-29,-30,42,42,42,]),')':([24,25,43,44,45,50,51,52,53,54,55,56,57,58,],[-33,-34,-31,58,-32,-22,-23,-24,-25,-26,-27,-28,-29,-30,]),'TO':([24,25,43,45,50,51,52,53,54,55,56,57,58,60,],[-33,-34,-31,-32,-22,-23,-24,-25,-26,-27,-28,-29,-30,65,]),'STEP':([24,25,43,45,50,51,52,53,54,55,56,57,58,68,],[-33,-34,-31,-32,-22,-23,-24,-25,-26,-27,-28,-29,-30,70,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'stmt_list':([0,3,26,34,63,69,],[2,11,46,49,67,72,]),'stmt':([0,3,26,34,63,69,],[3,3,3,3,3,3,]),'opt_string':([5,],[13,]),'empty':([5,16,48,49,68,],[15,33,33,64,71,]),'value':([6,32,],[16,48,]),'exp':([8,9,12,21,22,23,35,36,37,38,39,40,41,42,47,65,70,],[20,26,28,43,44,45,50,51,52,53,54,55,56,57,60,68,73,]),'value_list':([16,48,],[31,61,]),'opt_else':([49,],[62,]),'opt_step':([68,],[69,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> stmt_list','prog',1,'p_prog','ubasic_gram.py',25),
  ('stmt_list -> stmt stmt_list','stmt_list',2,'p_stmt_list','ubasic_gram.py',31),
  ('stmt_list -> stmt','stmt_list',1,'p_stmt_list','ubasic_gram.py',32),
  ('stmt -> ID = exp','stmt',3,'p_stmt','ubasic_gram.py',41),
  ('stmt -> INPUT opt_string ID','stmt',3,'p_stmt','ubasic_gram.py',42),
  ('stmt -> PRINT value value_list','stmt',3,'p_stmt','ubasic_gram.py',43),
  ('stmt -> END','stmt',1,'p_stmt','ubasic_gram.py',44),
  ('stmt -> IF exp THEN stmt_list opt_else ENDIF','stmt',6,'p_stmt','ubasic_gram.py',45),
  ('stmt -> WHILE exp stmt_list ENDWHILE','stmt',4,'p_stmt','ubasic_gram.py',46),
  ('stmt -> FOR ID = exp TO exp opt_step stmt_list NEXT ID','stmt',10,'p_stmt','ubasic_gram.py',47),
  ('opt_step -> STEP exp','opt_step',2,'p_opt_step','ubasic_gram.py',66),
  ('opt_step -> empty','opt_step',1,'p_opt_step','ubasic_gram.py',67),
  ('opt_string -> STRING ,','opt_string',2,'p_opt_string','ubasic_gram.py',78),
  ('opt_string -> empty','opt_string',1,'p_opt_string','ubasic_gram.py',79),
  ('opt_else -> ELSE stmt_list','opt_else',2,'p_opt_else','ubasic_gram.py',85),
  ('opt_else -> empty','opt_else',1,'p_opt_else','ubasic_gram.py',86),
  ('value_list -> , value value_list','value_list',3,'p_value_list','ubasic_gram.py',95),
  ('value_list -> empty','value_list',1,'p_value_list','ubasic_gram.py',96),
  ('value -> ID','value',1,'p_value','ubasic_gram.py',103),
  ('value -> INTEGER','value',1,'p_value','ubasic_gram.py',104),
  ('value -> STRING','value',1,'p_value','ubasic_gram.py',105),
  ('exp -> exp PLUS exp','exp',3,'p_exp_binary_exp','ubasic_gram.py',111),
  ('exp -> exp MINUS exp','exp',3,'p_exp_binary_exp','ubasic_gram.py',112),
  ('exp -> exp TIMES exp','exp',3,'p_exp_binary_exp','ubasic_gram.py',113),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp_binary_exp','ubasic_gram.py',114),
  ('exp -> exp EQ exp','exp',3,'p_exp_binary_exp','ubasic_gram.py',115),
  ('exp -> exp LE exp','exp',3,'p_exp_binary_exp','ubasic_gram.py',116),
  ('exp -> exp AND exp','exp',3,'p_exp_binary_exp','ubasic_gram.py',117),
  ('exp -> exp OR exp','exp',3,'p_exp_binary_exp','ubasic_gram.py',118),
  ('exp -> ( exp )','exp',3,'p_exp_paren','ubasic_gram.py',124),
  ('exp -> MINUS exp','exp',2,'p_uminus_exp','ubasic_gram.py',130),
  ('exp -> NOT exp','exp',2,'p_not_exp','ubasic_gram.py',136),
  ('exp -> INTEGER','exp',1,'p_exp_integer','ubasic_gram.py',142),
  ('exp -> ID','exp',1,'p_exp_id','ubasic_gram.py',148),
  ('empty -> <empty>','empty',0,'p_empty','ubasic_gram.py',155),
]