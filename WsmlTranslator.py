from AbstractVisitor import AbstractVisitor
from Visitor import Visitor
import SintaxeAbstrata as sa

class WsmlTranslator(AbstractVisitor):
    # def __init__(self):
    #     self.printer = Visitor()
    self.counter = 0
    
    def prTab():
        for a in range(self.counter):
            print(' ', end='')

    def incTab():
        self.counter += 3

    def decTab():
        self.counter -= 3 

    def visitSingleClass(self, singleClass):
        print("concept ", singleClass.className, end='')
        if singleClass.fatherName != None:
            print("subConceptOf ", singleClass.fatherName, end='')
        incTab()
        singleClass.classBody.accept(self)
    
    def visitCompoundClass(self, CompoundClass):
        print("concept ", CompoundClass.className, end='')
        if singleClass.fatherName != None:
            print("subConceptOf ", CompoundClass.fatherName, end='')
        incTab()
        CompoundClass.classBody.accept(self)
        CompoundClass.classes.accept(self)
        

    def visitClassBodyConcrete(self, funcDecl):
        pass

    def visitSingleDecl(self, funcDecl):
        pass

    def visitCompoundDecl(self, funcDecl):
        pass

    def visitAttributeDef(self, funcDecl):
        pass

    def visitFuncDeclConcrete(self, funcDeclConcrete):
        funcDeclConcrete.signature.accept(self)
        funcDeclConcrete.body.accept(self)

    def visitSignatureConcrete(self, signatureConcrete):
        print (blank(), signatureConcrete.type, ' ', end='', sep='')
        print(signatureConcrete.id, '(', end = '', sep='')
        if (signatureConcrete.sigParams != None):
            signatureConcrete.sigParams.accept(self)
        print(')', end = '')

    def visitSingleSigParams(self, singleSigParams):
        print(singleSigParams.type, ' ', end='', sep='')
        print(singleSigParams.id, end='', sep='')

    def visitCompoundSigParams(self, compoundSigParams):
        print(compoundSigParams.type, ' ', end='', sep='')
        print(compoundSigParams.id, ', ', end='', sep='')
        compoundSigParams.sigParams.accept(self)

    def visitBodyConcrete(self, bodyConcrete):
        global tab
        print ('{ ')
        tab =  tab + 3
        if (bodyConcrete.stms != None):
            bodyConcrete.stms.accept(self)
        tab =  tab - 3
        print (blank(), '} ', sep='')

    def visitSingleStm(self, singleStm):
        singleStm.stm.accept(self)

    def visitCompoundStm(self, compoundStm):
        compoundStm.stm.accept(self)
        compoundStm.stms.accept(self)

    def visitStmExp(self, stmExp):
        print(blank(),sep='',end='')
        stmExp.exp.accept(self)
        print('')

    def visitStmWhile(self, stmWhile):
        print (blank(), 'while (', end='', sep='')
        stmWhile.exp.accept(self)
        print (')', end='', sep='')
        stmWhile.block.accept(self)

    def visitStmReturn(self, stmReturn):
        print (blank(), 'return ', end='', sep='')
        stmReturn.exp.accept(self)
        print (';')

    def visitAssignExp(self, assignExp):
        # print("visitAssignExp")
        assignExp.exp1.accept(self)
        print(' = ', end='')
        assignExp.exp2.accept(self)

    def visitSomaExp(self, somaExp):
        # print("visitSomaExp")
        somaExp.exp1.accept(self)
        print(' + ', end='')
        somaExp.exp2.accept(self)

    def visitMulExp(self, mulExp):
        # print("visitMulExp")
        mulExp.exp1.accept(self)
        print(' * ', end='')
        mulExp.exp2.accept(self)

    def visitPotExp(self, potExp):
        # print("visitPotExp")
        potExp.exp1.accept(self)
        print(' ^ ', end='')
        potExp.exp2.accept(self)

    def visitCallExp(self, callExp):
        # print("visitCallExp")
        callExp.call.accept(self)

    def visitNumExp(self, numExp):
        # print("visitNumExp")
        print(numExp.num, end='')

    def visitIdExp(self, idExp):
        # print("visitIdExp")
        print(idExp.id, end='')

    def visitBooleanExp(self, booleanExp):
        print(booleanExp.boolValue, end='')

    def visitParamsCall(self, paramsCall):
        # print("visitParamsCall")
        print(paramsCall.id, '(', end='', sep='')
        paramsCall.params.accept(self)
        print(')', end='')

    def visitNoParamsCall(self, simpleCall):
        # print("visitSimpleCall")
        print(blank(), simpleCall.id, '()', end='', sep='')

    def visitCompoundParams(self, compoundParams):
        # print("visitCompoundParams")
        compoundParams.exp.accept(self)
        print(', ', end='')
        compoundParams.params.accept(self)

    def visitSingleParam(self, singleParam):
        # print("visitSingleParam")
        singleParam.exp.accept(self)
