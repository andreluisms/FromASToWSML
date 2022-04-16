# -------------------------
# PythonLex.py
#----------------------
import ply.lex as lex

stack = [0]
isDedent = False

keywords = {
   'False' : 'FALSE',
   'def' : 'DEF',
   'if' : 'IF',
   'raise' : 'RAISE',
   'None' : 'NONE',
   'del' : 'DEL',
   'import' : 'IMPORT',
   'return' : 'RETURN',
   'True' : 'TRUE',
   'elif' : 'ELIF',
   'in' : 'IN',
   'try' : 'TRY',
   'and' : 'AND',
   'else' : 'ELSE',
   'is' : 'IS',
   'while' : 'WHILE',
   'as' : 'AS',
   'except' : 'EXCEPT',
   'lambda' : 'LAMBDA',
   'with' : 'WITH',
   'assert' : 'ASSERT',
   'finally' : 'FINALLY',
   'nonlocal' : 'NONLOCAL',
   'yield' : 'YIELD',
   'break' : 'BREAK',
   'for' : 'FOR',
   'not' : 'NOT',
   'class' : 'CLASS',
   'from' : 'FROM',
   'or' : 'OR',
   'continue' : 'CONTINUE',
   'global' : 'GLOBAL',
   'pass' : 'PASS'
}

tokens = ['PLUS','MINUS','TIMES','EXPONENTATION','DIVISION','FLOORDIVISION',
          'MODULUS','AT','BRSHIFT','BLSHIFT','BAND','BOR','BXOR','BNOT',
          'ASSIGN','PLUSASSIGN','MINASSIGN','TIMASSIGN','DIVASSIGN','MODASSIGN',
          'FDIVASSIGN','EXPASSIGN','BANDASSIGN','BORASSIGN','BXORASSIGN',
          'BLSHIFTASSIGN','BRSHIFTASSIGN','LESS','GREATER','LESSEQUAL','GREATEREQUAL',
          'EQUAL','NOTEQUAL', 'STRING', 'NUMBER', 'OCTALNUMBER', 'ID', 
          'LPAREN','RPAREN','LBRACKETS','RBRACKETS','LBRACES','RBRACES','COMMA','DOT',
          'COLLON','SEMICOLON', 'IDENT', 'DEDENT'] + list(keywords.values())

t_PLUS = '\+'
t_MINUS = '\-'
t_TIMES = '\*'
t_EXPONENTATION = '\*\*'
t_DIVISION = '/'
t_FLOORDIVISION = r'//'
t_MODULUS = '%'
t_AT = '@'
t_BRSHIFT = '<<'
t_BLSHIFT = '>>'
t_BAND = '&'
t_BOR = '\|'
t_BXOR = '\^'
t_BNOT = '\~'
t_ASSIGN = '='
t_PLUSASSIGN='\+='
t_MINASSIGN='-='
t_TIMASSIGN='\*='
t_EXPASSIGN='\*\*='
t_DIVASSIGN='/='
t_MODASSIGN = '%='
t_FDIVASSIGN = '//='
t_BANDASSIGN = '&='
t_BORASSIGN = '\|='
t_BXORASSIGN = '\^='
t_BLSHIFTASSIGN = '>>='
t_BRSHIFTASSIGN = '<<='
t_LESS = '<'
t_GREATER = '>'
t_LESSEQUAL = '<='
t_GREATEREQUAL ='>='
t_EQUAL = '=='
t_NOTEQUAL = '!='
t_LPAREN = '\('
t_RPAREN = '\)'
t_LBRACKETS = '\['
t_RBRACKETS = '\]'
t_LBRACES = '{'
t_RBRACES = '}'
t_COMMA=','
t_DOT = '\.'
t_COLLON = ':'
t_SEMICOLON = ';'


def t_IDENT(t):
   r'^(\s)+ |\n(\s)*'
   global stack
   global isDedent
   lenToken = len(t.value)-1
   if stack[-1] < lenToken and not isDedent:
      stack.append(lenToken)
      t.type='IDENT'
      return t
   elif  stack[-1] == lenToken:
      if isDedent:
         isDedent = False
      pass   
   elif stack[-1] > lenToken:
      stack.pop()
      isDedent = True
      t.type = 'DEDENT'
      print(-(lenToken+1))
      t.lexer.skip(-(lenToken+1))
      return t
   elif stack[-1] < lenToken and isDedent:
      print("Illegal DEDENT")
      pass

def t_BINARYNUMBER(t):
   r'0b[0-1]+'
   print('[t_BINARYNUMBER] ' , t.lexer.lexpos)
   t.value = int(t.value,2)
   t.type="NUMBER"
   return t

def t_OCTANUMBER(t):
   r'0o[0-7]+'
   t.value = int(t.value,8)
   t.type="NUMBER"
   return t

def t_HEXANUMBER(t):
   r'0x[0-9a-fA-F]+'
   t.value = int(t.value,16)
   t.type="NUMBER"
   return t

def t_NUMBER(t):
   r'[0-9]+(\.[0-9]+)?([eE][+-]?\d+)?' 
   t.value = float(t.value)
   return t

def t_STRING(t):
   r'r?(\"([^\\\n]|(\\.))*?\") | r?(\'([^\\\n]|(\\.))*?\') | r?(\"\"\"([^\\\n]|(\\.))*?\"\"\")'
   return t

def t_ID(t):
   r'[a-zA-Z_][a-zA-Z_0-9]*'
   t.type = keywords.get(t.value,'ID')
   return t

def t_COMMENT(t):
   r'(\'\'\'(.|\n)*?\'\'\') | (\#(.)*)'
   pass

def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)


def t_space(t):
   r'[ \t]'
   pass


# t_ignore = ' \t'


def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)


data=''
with open('program_test.py') as f:
    lines = f.readlines()

for l in lines:
    data = data + l


# data = ' 0b110 123.32'
lexer = lex.lex()
lexer.input(data)

for tok in lexer:
   if (tok.type == 'IDENT') or (tok.type == 'DEDENT'):
      print(tok.type, ' : ',tok.value)