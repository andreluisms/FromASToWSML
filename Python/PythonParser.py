# -------------------------
# PythonLex.py
#----------------------
import ply.lex as lex

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
   'pass' : 'PASS',
   r'\+':'PLUS',
   '-':'MINUS',
   '\*':'TIMES',
   '\*\*':'EXPONENTATION',
   '/':'DIVISION',
   r'//':'FLOORDIVISION',
   r'%':'MODULUS',
   r'@':'AT',
   r'<<':'BRSHIFT',
   r'>>':'BLSHIFT',
   r'&':'BAND',
   r'|':'BOR',
   r'\^':'BXOR',
   r'~':'BNOT',
   '=':'ASSIGN',
   '+=':'PLUSASSIGN',
   '-=':'MINASSIGN',
   '\*=':'TIMASSIGN',
   '/=':'DIVASSIGN',
   '%=':'MODASSIGN',
   '//=':'FDIVASSIGN',
   '\*\*=':'EXPASSIGN',
   '&=':'BANDASSIGN',
   '|=':'BORASSIGN',
   '^=':'BXORASSIGN',
   '>>=':'BLSHIFTASSIGN',
   '<<=':'BRSHIFTASSIGN',
   r'<':'LESS',
   r'>':'GREATER',
   r'<=':'LESSEQUAL',
   r'>=':'GREATEREQUAL',
   r'==':'EQUAL',
   r'!=':'NOTEQUAL'
}

tokens = ['COMMA', 'SOMA', 'ID', 'NUMBER', 'VEZES', 'POT', 'LPAREN',
          'RPAREN', 'IGUAL', 'LCHAV', 'RCHAV', 'PV', 'P','DP'] + list(keywords.values())



# t_PLUS = '\+'
# t_MINUS = '-'
# t_TIMES = '\*'
# t_EXPONENTATION = '\*\*'
# t_DIVISION = '/'
# t_FLOORDIVISION = r'//'
# t_MODULUS = r'%'
# t_AT = r'@'
# t_BRSHIFT = r'<<'
# t_BLSHIFT = r'>>'
# t_BAND = r'&'
# t_BOR = r'|'
# t_BXOR = r'\^'
# t_BNOT = r'~'
# #t_ r':='
# t_ASSIGN = '='
# t_PLUSASSIGN = '+='
# t_MINASSIGN = '-='
# t_TIMASSIGN = '\*='
# t_DIVASSIGN = '/='
# t_MODASSIGN = '%='
# t_FDIVASSIGN = '//='
# t_EXPASSIGN = '\*\*='
# t_BANDASSIGN = '&='
# t_BORASSIGN = '|='
# t_BXORASSIGN = '^='
# t_BLSHIFTASSIGN = '>>='
# t_BRSHIFTASSIGN = '<<='

# t_LESS = r'<'
# t_GREATER = r'>'
# t_LESSEQUAL = r'<='
# t_GREATEREQUAL = r'>='
# t_EQUAL = r'=='
# t_NOTEQUAL = r'!='


# t_EQUAL= r'='
# t_P = r'\.'
# t_SOMA = r'\+'
# t_VEZES = r'\*'
# t_POT = r'\^'
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_COMMA = r','
# t_LCHAV = r'{'
# t_RCHAV = r'}'
# t_PV = r';'
# t_DP = r':'

def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_ID(t):
   r'[a-zA-Z_][a-zA-Z_0-9]*'
   t.type = keywords.get(t.value,'ID')
   return t

def t_COMMENT(t):
   r'(\'\'\' (.|\n)*? \'\'\') | (\#(.)*)'
   pass

def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

t_ignore = ' \t'


def t_PPP(t):
   r'.+?'
   t.type = keywords.get(t.value,'ERROR')
   if t.type == 'ERROR': 
      print("Illegal character '%s'" % t.value)
   else:
      return t

def t_error(t):
   print("Illegal character '%s'" % t.value)
   t.lexer.skip(1)
   
data = '::::'
lexer = lex.lex()
lexer.input(data)

for tok in lexer:
   print(tok.type, ' : ',tok.value)