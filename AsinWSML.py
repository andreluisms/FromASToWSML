from AbstractVisitor import AbstractVisitor
from Visitor import Visitor
import SintaxeAbstrata as sa

class ASinWSML(AbstractVisitor):
    # def __init__(self):
    #     self.printer = Visitor()
    counter = 0
    number = 0    

    def printInstance(self, obj):
        print("instance ", self.lstrType(obj),  self.hexAddr(obj),  ' memberOf ', self.strType(obj), sep='')
        self.incTab() 
        for attr in dir(obj):
            if attr[0]!='_' and not callable(getattr(obj, attr)):
                self.prTab()
                attrv = getattr(obj, attr)
                print(attr, 'hasValue ', end='')
                if isinstance(attrv, (int, float, bool)): 
                    print(attrv) 
                elif isinstance(attrv, str):
                    print('"', attrv, '"', sep='')
                else:
                    print(self.lstrType(attrv), self.hexAddr(attrv), sep='')
        print('')
        self.decTab()
                        

    def hexAddr(self, obj):
        return hex(id(obj))

    def strType(self, obj):
        return type(obj).__name__

    def lstrType(self, obj):
        return type(obj).__name__.lower()

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
        self.printInstance(singleClass)
        singleClass.classBody.accept(self)

    
    def visitCompoundClass(self, CompoundClass):
        self.printInstance(CompoundClass)
        CompoundClass.classBody.accept(self)
        CompoundClass.classes.accept(self)
        
        

    def visitClassBody(self, classBody):
        self.printInstance(classBody)
        classBody.declarations.accept(self)

    def visitSingleDeclaration(self, singleDeclaration):
        self.printInstance(singleDeclaration)
        singleDeclaration.declaration.accept(self)

    def visitCompoundDeclaration(self, compoundDeclaration):
        self.printInstance(compoundDeclaration)
        compoundDeclaration.declaration.accept(self)
        compoundDeclaration.declarations.accept(self)

    def visitAttributeDeclaration(self, attributeDeclaration):
        self.printInstance(attributeDeclaration)
        attributeDeclaration.expression.accept(self)

    def visitFunctionDeclaration(self, functionDeclaration):
        self.printInstance(functionDeclaration)
        functionDeclaration.signature.accept(self)
        functionDeclaration.functionBody.accept(self)

    def visitSignature(self, signature):
        self.printInstance(signature)
        signature.parameters.accept(self)


    def visitSingleSigParameter(self, singleSigParameter):
        self.printInstance(singleSigParameter)

    def visitCompoundSigParameter(self, compoundSigParameter):
        self.printInstance(compoundSigParameter)
        compoundSigParameter.parameters.accept(self)

    def visitBody(self, body):
        self.printInstance(body)
        if (body.statements != None):
            body.statements.accept(self)

    def visitSingleStatement(self, singleStatement):
        self.printInstance(singleStatement)
        singleStatement.statement.accept(self)

    def visitCompoundStatement(self, compoundStatement):
        self.printInstance(compoundStatement)
        compoundStatement.statement.accept(self)
        compoundStatement.statements.accept(self)

    def visitExpressionStm(self, expressionStm):
        self.printInstance(expressionStm)
        expressionStm.expression.accept(self)


    def visitWhileStm(self, stmWhile):
        self.printInstance(stmWhile)
        stmWhile.expression.accept(self)
        stmWhile.block.accept(self)
       

    def visitReturnStm(self, stmReturn):
        self.printInstance(stmReturn)
        stmReturn.expression.accept(self)

    def visitAssignExp(self, assignExp):
        self.printInstance(assignExp)
        assignExp.leftExpression.accept(self)
        assignExp.rightExpression.accept(self)

    def visitSomaExp(self, somaExp):
        self.printInstance(somaExp)
        somaExp.leftExpression.accept(self)
        somaExp.rightExpression.accept(self)

    def visitMulExp(self, mulExp):
        self.printInstance(mulExp)
        mulExp.leftExpression.accept(self)
        mulExp.rightExpression.accept(self)

    def visitPotExp(self, potExp):
        self.printInstance(potExp)
        potExp.leftExpression.accept(self)
        potExp.rightExpression.accept(self)

    def visitCallExp(self, callExp):
        self.printInstance(callExp)
        callExp.call.accept(self)

    def visitNumExp(self, numExp):
        self.printInstance(numExp)

    def visitIdExp(self, idExp):
        self.printInstance(idExp)

    def visitBooleanExp(self, booleanExp):
        self.printInstance(booleanExp)
    
    def visitSelfExp(self, selfExp):
        self.printInstance(selfExp)

    def  visitCallWithParameters(self, callWithParameters):
        self.printInstance(callWithParameters)
        callWithParameters.parameters.accept(self)

    def  visitCallWithoutParameters(self, callWithoutParameters):
        self.printInstance(callWithoutParameters)

    def visitCompoundParameter(self, compoundParams):
        self.printInstance(compoundParams)
        compoundParams.expression.accept(self)
        compoundParams.parameters.accept(self)

    def visitSingleParameter(self, singleParam):
        self.printInstance(singleParam)
        singleParam.expression.accept(self)

    def visitAccessExp(self, accessExp):
        self.printInstance(accessExp)
        accessExp.name.accept(self)
        accessExp.expression.accept(self)
                
        
