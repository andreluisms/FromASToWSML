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

visitor2 = aw.ASinWSML()
lexer2 = lex.lex()
lexer2.input(data2)
parser2 = yacc.yacc()
# for l in lexer2:
#     print(l)
result2 = parser2.parse()

print("""wsmlVariant _"http://www.wsmo.org/wsml/wsml-syntax/wsml-rule"
namespace { _"http://ufs.br/ontologies#"}
\nontology PythonAbstractSyntax\n""")
result.accept(visitor)
result2.accept(visitor2)
