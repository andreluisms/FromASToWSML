from ExpressionLanguageParser import *
import WsmlASTranslator as av

data=''
with open('SintaxeAbstrata.py') as f:
    lines = f.readlines()

for l in lines:
    data = data + l

lexer = lex.lex()
lexer.input(data)
parser = yacc.yacc()
result = parser.parse(debug=False)


visitor = av.WsmlASTranslator()
result.accept(visitor)