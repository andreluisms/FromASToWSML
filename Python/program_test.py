def t_IDENT(t):
   r'^(\s+)'
   global stack
   lenToken = len(t.value)
   if len(stack) == 0 or stack[-1] < lenToken:
      stack.append(lenToken)
      t.type='IDENT'
      return t
   elif  stack[-1] == lenToken:
      pass   
   elif stack[-1] > lenToken:
      stack.pop()
      t.type = 'DEDENT'
      t.lexer.skip(-lenToken)
      return t
   elif stack[-1] < lenToken:
      print("Illegal DEDENT")
   pass
