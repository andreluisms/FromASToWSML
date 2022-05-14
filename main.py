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



visitor = av.WsmlASTranslator() 
parserConcepts = yacc.yacc()
lexerConcepts = lex.lex()
lexerConcepts.input(data)
tkconcepts = visitor.visitTokens(tokens)
result = parserConcepts.parse()

print(lex.Token)

visitorInstances = aw.ASinWSML()
lexerInstances = lex.lex()
lexerInstances.input(data2)
tkinsconcepts = visitor.visitTokInstances(lexerInstances)
lexerInstances.input(data2)
parserInstances = yacc.yacc()
# for l in lexerInstances:
#     print(l)
result2 = parserInstances.parse()

print("""wsmlVariant _"http://www.wsmo.org/wsml/wsml-syntax/wsml-rule"
namespace { _"http://ufs.br/ontologies#"}
\nontology PythonAbstractSyntax\n""")
print(tkconcepts)
result.accept(visitor)

print()
print(tkinsconcepts)
result2.accept(visitorInstances)


print (tkinsconcepts)
