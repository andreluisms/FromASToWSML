from AbstractVisitor import AbstractVisitor
from Visitor import Visitor
import SintaxeAbstrata as sa

class WsmlASTranslator(AbstractVisitor):
    # def __init__(self):
    #     self.printer = Visitor()
    counter = 0
    
    def visitTokens(self, tokens):
        str = ''
        for l in tokens:
            str+="concept " + l
            str+="\n   value ofType _string\n\n"
        return str


    def prTab(self):
        for a in range(self.counter):
            print(' ', end='')

    def incTab(self):
        self.counter += 3

    def decTab(self):
        self.counter -= 3 

    
    def visitPassStm(self, passStm):
        pass

    def visitSingleClass(self, singleClass):
        print("concept ", singleClass.className, end='')
        if singleClass.fatherName != None:
            print(" subConceptOf", singleClass.fatherName, end='')
        self.incTab()
        singleClass.classBody.accept(self)
        print('')
        self.decTab()
    
    def visitCompoundClass(self, CompoundClass):
        print("concept ", CompoundClass.className, end='')
        if CompoundClass.fatherName != None:
            print(" subConceptOf", CompoundClass.fatherName, end='')
        self.incTab()
        CompoundClass.classBody.accept(self)
        print('')
        print('')
        self.decTab()
        CompoundClass.classes.accept(self)
        
        

    def visitClassBody(self, classBody):
        classBody.declarations.accept(self)

    def visitSingleDeclaration(self, singleDeclaration):
        singleDeclaration.declaration.accept(self)

    def visitCompoundDeclaration(self, compoundDeclaration):
        compoundDeclaration.declaration.accept(self)
        compoundDeclaration.declarations.accept(self)

    def visitAttributeDeclaration(self, attributeDeclaration):
        pass

    def visitFunctionDeclaration(self, functionDeclaration):
       #functionDeclaration.signature.accept(self)
       functionDeclaration.functionBody.accept(self)

    def visitSignature(self, signature):
        pass

    def visitSingleSigParameter(self, singleSigParameter):
        pass

    def visitCompoundSigParameter(self, compoundSigParameter):
        pass

    def visitBody(self, body):
        if (body.statements != None):
            body.statements.accept(self)

    def visitSingleStatement(self, singleStatement):
        singleStatement.statement.accept(self)

    def visitCompoundStatement(self, compoundStatement):
        compoundStatement.statement.accept(self)
        compoundStatement.statements.accept(self)

    def visitExpressionStm(self, expressionStm):
        expressionStm.expression.accept(self)


    def visitWhileStm(self, stmWhile):
       pass

    def visitReturnStm(self, stmReturn):
       pass

    def visitAssignExp(self, assignExp):
        print('')
        self.prTab()
        assignExp.leftExpression.accept(self)
        print(' ofType ', end='')
        assignExp.rightExpression.accept(self)

    def visitSomaExp(self, somaExp):
        pass

    def visitMulExp(self, mulExp):
        pass

    def visitPotExp(self, potExp):
        pass

    def visitCallExp(self, callExp):
        pass

    def visitNumExp(self, numExp):
        pass

    def visitIdExp(self, idExp):
        p = idExp.id
        if (p[len(p)-1].isdigit()):
            print(p[:-1], end='')
        else:
            print(p, end='')

    def visitBooleanExp(self, booleanExp):
        pass
    
    def visitSelfExp(self, selfExp):
        pass

    def  visitCallWithParameters(self, paramsCall):
        pass

    def  visitCallWithoutParameters(self, simpleCall):
        pass

    def visitCompoundParameter(self, compoundParams):
        pass

    def visitSingleParameter(self, singleParam):
        pass 

    def visitAccessExp(self, accessExp):
        if isinstance(accessExp.name, sa.SelfExp):
            accessExp.expression.accept(self)
        else:
            print(accessExp.name)
                
        
