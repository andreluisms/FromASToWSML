# -------------------------
# ExpressionLanguageLex.py
#----------------------
import ply.lex as lex
reservadas = {
   'while' : 'WHILE',
   'if' : 'IF',
   'True' : 'TRUE',
   'False' : 'FALSE',
   'return' : 'RETURN',
   'class'  : 'CLASS',
   'def'    : 'DEF',
   'pass': 'PASS',
   'self': 'SELF'
}
tokens = ['COMMA', 'SOMA', 'ID', 'NUMBER', 'VEZES', 'POT', 'LPAREN',
          'RPAREN', 'IGUAL', 'LCHAV', 'RCHAV', 'PV', 'P','DP'] + list(reservadas.values())

t_IGUAL= r'='
t_P = r'\.'
t_SOMA = r'\+'
t_VEZES = r'\*'
t_POT = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_LCHAV = r'{'
t_RCHAV = r'}'
t_PV = r';'
t_DP = r':'

def t_IMPORT(t):
   r'(from (.)*) |(import (.)*)'
   pass 

def t_ID(t):
   r'[a-zA-Z_][a-zA-Z_0-9]*'
   t.type = reservadas.get(t.value,'ID')
   return t

def t_COMMENT(t):
   r'(\'\'\' (.|\n)*? \'\'\') | (\#(.)*)'
   pass

def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

t_ignore = ' \t'



def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)

