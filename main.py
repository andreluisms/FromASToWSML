from ExpressionLanguageParser import *
import WsmlASTranslator as av
import AsinWSML as aw

data=''
with open('SintaxeAbstrata.py') as f:
    lines = f.readlines()
for l in lines:
    data = data + l
data = data + "\n"

data2=''
with open('code.py') as f:
    lines = f.readlines()
for l in lines:
    data2 = data2 + l
data2 = data2 + "\n"



lexer = lex.lex()
lexer.input(data)
parser = yacc.yacc()
result = parser.parse()
visitor = av.WsmlASTranslator() 
result.accept(visitor)

visitor2 = aw.ASinWSML()
lexer = lex.lex()
lexer.input(data2)
# for l in lexer:
#     print(l)
result = parser.parse()
result.accept(visitor2)