# -------------------------
# ExpressionLanguageLex.py
#----------------------
from xmlrpc.client import FastUnmarshaller
import ply.lex as lex

stack = [0]
isDedent = False
openExp = False
emptyLine = False
isComment = False
# \\\n -> Junção de Linhas físicas
# não válido para comentários
# Elementos entre Chave ou Parentesis também representam junção de linhas físicas
# linhas em branco (somente brancos  ou comments) não geram NEWLINE
#  tabulacoes e espacos em branco no inicio de uma linha logica = IDENT
#

states = (
   ('identdedent', 'exclusive'),
)


reservadas = {
   'while' : 'WHILE',
   'if' : 'IF',
   'True' : 'TRUE',
   'False' : 'FALSE',
   'return' : 'RETURN',
   'class'  : 'CLASS',
   'def'    : 'DEF',
   'pass': 'PASS',
   'self': 'SELF',
   'for' : 'FOR',
   'in' : 'IN'
}
tokens = ['COMMA', 'SOMA', 'ID', 'NUMBER', 'VEZES', 'POT', 'LPAREN',
          'RPAREN', 'IGUAL', 'LCHAV', 'RCHAV', 'PV', 'P','DP', 'IDENT', 'DEDENT', 'STRING', 'LBRACKETS', 'RBRACKETS',
          'LESS', 'NEWLINE'] + list(reservadas.values())

t_IGUAL= r'='
t_P = r'\.'
t_SOMA = r'\+'
t_VEZES = r'\*'
t_POT = r'\^'
t_COMMA = r','
t_LCHAV = r'{'
t_RCHAV = r'}'
t_PV = r';'
t_DP = r':'


# t_PLUS = '\+'
# t_MINUS = '\-'
# t_TIMES = '\*'
# t_EXPONENTATION = '\*\*'
# t_DIVISION = '/'
# t_FLOORDIVISION = r'//'
# t_MODULUS = '%'
# t_AT = '@'
# t_BRSHIFT = '<<'
# t_BLSHIFT = '>>'
# t_BAND = '&'
# t_BOR = '\|'
# t_BXOR = '\^'
# t_BNOT = '\~'
# t_ASSIGN = '='
# t_PLUSASSIGN='\+='
# t_MINASSIGN='-='
# t_TIMASSIGN='\*='
# t_EXPASSIGN='\*\*='
# t_DIVASSIGN='/='
# t_MODASSIGN = '%='
# t_FDIVASSIGN = '//='
# t_BANDASSIGN = '&='
# t_BORASSIGN = '\|='
# t_BXORASSIGN = '\^='
# t_BLSHIFTASSIGN = '>>='
# t_BRSHIFTASSIGN = '<<='
# t_LESS = '<'
# t_GREATER = '>'
# t_LESSEQUAL = '<='
# t_GREATEREQUAL ='>='
# t_EQUAL = '=='
# t_NOTEQUAL = '!='
# t_LPAREN = '\('
# t_RPAREN = '\)'

# t_LBRACES = '{'
# t_RBRACES = '}'
# t_COMMA=','
# t_DOT = '\.'
# t_COLLON = ':'
# t_SEMICOLON = ';'

def t_LBRACKETS(t):
   '\['
   global openExp
   openExp = True
   return t

def t_RBRACKETS(t):
   '\]'
   global openExp
   openExp = False
   return t

def t_LPAREN(t):
   '\('
   global openExp
   openExp = True
   return t

def t_RPAREN(t):
   '\)'
   global openExp
   openExp = False
   return t

# def t_identdedent_IMPORT(t):
#    r'(from (.)*) |(import (.)*)'
#    global isComment
#    isComment = True
#    pass 

def t_identdedent_noblanks(t):
   r'[^ \s]'
   # print("identdedent_noblanks")
   global isDedent
   lenToken = len(t.value)
   if 0 < stack[-1]:
      isDedent = True
      stack.pop()
      t.type = 'DEDENT'
      t.lexer.skip(-(lenToken))
      return t
   else:
      if isDedent: isDedent = False
      t.lexer.skip(-(lenToken))
      t.lexer.begin('INITIAL')
 
def t_identdedent_blanks(t):
   r'[ \t]+[^ \t\n]'
   global stack
   global isDedent
   lenToken = len(t.value)-1
   #Nao ha identacao
   if lenToken == stack[-1]:
      if isDedent: isDedent = False
      t.lexer.skip(-1)
      t.lexer.begin('INITIAL')
   #Gerar IDENT
   elif lenToken > stack[-1]:
      if isDedent: 
         isDedent = False
         t.lexer.skip(-1)
         t.lexer.begin('INITIAL')
         print("ERRO DE DEDENTACAO")
      else:
         stack.append(lenToken)
         t.type='IDENT'
         t.lexer.skip(-1)
         t.lexer.begin('INITIAL')
         t.value = t.value[:-1]
         return t
   #Gerar DEDENT
   elif lenToken < stack[-1]:
      isDedent = True
      stack.pop()
      t.type = 'DEDENT'
      t.lexer.skip(-(lenToken+1))
      t.value = t.value[:-1]
      return t

def t_identdedent_onlyblanks(t):
   r'[ \t]+'
   global emptyLine
   emptyLine = True
   t.lexer.begin('INITIAL')

def t_identdedent_onlybreakline(t):
   r'\n'
   global emptyLine
   emptyLine = True
   t.lexer.skip(-1)
   t.lexer.begin('INITIAL')

def t_identdedent_eof(t):
   global isDedent
   lenToken = len(t.value)
   if 0 < stack[-1]:
      isDedent = True
      stack.pop()
      t.type = 'DEDENT'
      t.lexer.skip(-(lenToken))
      return t
   else:
      if isDedent: isDedent = False
      t.lexer.begin('INITIAL')


def t_eof(t):
   global isDedent
   lenToken = len(t.value)
   if 0 < stack[-1]:
      isDedent = True
      stack.pop()
      t.type = 'DEDENT'
      t.lexer.skip(-(lenToken))
      return t
   else:
      if isDedent: isDedent = False
      t.lexer.begin('INITIAL')

def t_IMPORT(t):
   r'(from (.)*) |(import (.)*)'
   global isComment
   isComment = True
   pass 



def t_ID(t):
   r'[a-zA-Z_][a-zA-Z_0-9]*'
   t.type = reservadas.get(t.value,'ID')
   return t

def t_COMMENT(t):
   r'(\'\'\' (.|\n)*? \'\'\') | (\#(.)*)'
   global isComment
   isComment = True
   pass

def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_STRING(t):
   r'r?(\"([^\\\n]|(\\.))*?\") | r?(\'([^\\\n]|(\\.))*?\') | r?(\"\"\"([^\\\n]|(\\.))*?\"\"\")'
   return t

def t_MULTILINE(t):
   r'\\\n'
   t.lexer.lineno += 1


def t_NEWLINE(t):
   r'\n'
   t.lexer.lineno += 1
   global emptyLine
   global isComment
   if not openExp and not emptyLine and not isComment:
      t.lexer.begin('identdedent')
      return t
   elif emptyLine:
      emptyLine = False
   elif isComment:
      isComment = False
   t.lexer.begin('identdedent')


t_ignore = ' \t'


def t_ANY_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)

# lexer = lex.lex()
# data = 'if alguma : [3, 7\n,8, 10\n,20]\n\tteste  \n\t\tteste2  \n\t\n'
# lexer.input(data)
# for l in lexer:
#    print (l)