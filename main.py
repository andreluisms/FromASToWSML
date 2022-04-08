from ExpressionLanguageParser import *
import WsmlTranslator as av

# # Input Example
data = ''' 
class SingleClass(Program):
    def __init__(self, className, fatherName, classBody):
        self.className = className
        self.fatherName = fatherName
        self.classBody = classBody
    def accept(self, visitor):
        pass

class CompoundClass(Program):
    def __init__(self, className, fatherName, classBody, classes):
        self.className = className
        self.fatherName = fatherName
        self.classBody = classBody
        self.classes = classes
    def accept(self, visitor):
        pass
'''
lexer = lex.lex()
lexer.input(data)
parser = yacc.yacc()
result = parser.parse(debug=False)


visitor = av.WsmlTranslator()
#visitor = vis.Visitor()
result.accept(visitor)