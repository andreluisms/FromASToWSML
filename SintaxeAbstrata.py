from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

'''
Programa
'''
class Program:
    def accept(self, visitor):
        pass


class SingleClass(Program):
    def __init__(self, ID1, ID2, ClassBody):
        self.className = ID1
        self.fatherName = ID2 
        self.classBody = ClassBody
    def accept(self, visitor):
        return visitor.visitSingleClass(self)


class CompoundClass(Program):
    def __init__(self, ID1, ID2, ClassBody, Program):
        self.className = ID1
        self.fatherName = ID2
        self.classBody = ClassBody
        self.classes = Program
    def accept(self, visitor):
        return visitor.visitCompoundClass(self)


'''
ClassBody
'''

class ClassBody:
    def __init__(self, Declarations):
        self.declarations = Declarations
    def accept(self, visitor):
        return visitor.visitClassBody(self)


'''
Declarations
'''
class Declarations:
    def accept(self, visitor):
        pass


class SingleDeclaration(Declarations):
    def __init__(self, Declaration):
        self.declaration = Declaration
    def accept(self, visitor):
        return visitor.visitSingleDeclaration(self)


class CompoundDeclaration(Declarations):
    def __init__(self, Declaration, Declarations):
        self.declaration = Declaration
        self.declarations = Declarations
    def accept(self, visitor):
        return visitor.visitCompoundDeclaration(self)


'''
Declaracao de funcao
FuncDecl
'''

class Declaration:
    def accept(self, visitor):
        pass

class AttributeDeclaration(Declaration):
    def __init__(self, ID, Expression):
         self.nameAttribute = ID
         self.expression = Expression
    def accept(self, visitor):
        return visitor.visitAttributeDeclaration(self)

class FunctionDeclaration(Declaration):
    def __init__(self, Signature, Body):
        self.signature = Signature
        self.functionBody = Body
    def accept(self, visitor):
        return visitor.visitFunctionDeclaration(self)

'''
Assinatura de funcao
Signature
'''
class Signature:
    def __init__(self, ID, Parameters):
        self.nameFunction = ID
        self.parameters = Parameters
    def accept(self, visitor):
        return visitor.visitSignature(self)
'''
Parametros de assinatura de funcao
SigParams
'''

class SigParameters:
    def accept(self, visitor):
        pass

class SingleSigParameter(SigParameters):
    def __init__(self, ID):
        self.nameParameter = ID
    def accept(self, visitor):
        return visitor.visitSingleSigParameter(self)


class CompoundSigParameter(SigParameters):
    def __init__(self, ID, SigParameters):
        self.nameParameter = ID
        self.parameters = SigParameters
    def accept(self, visitor):
        return visitor.visitCompoundSigParameter(self)

'''
Corpo de uma funcao
Body
'''

class Body:
    def __init__(self, Statements):
        self.statements = Statements
    def accept(self, visitor):
        return visitor.visitBody(self)

'''
Comandos
Stms
'''

class Statements:
    def accept(self, visitor):
        pass

class SingleStatement(Statements):
    def __init__(self, Statement):
        self.statement = Statement
    def accept(self, visitor):
        return visitor.visitSingleStatement(self)

class CompoundStatement(Statements):
    def __init__(self, Statement, Statements):
        self.statement = Statement
        self.statements = Statements
    def accept(self, visitor):
        return visitor.visitCompoundStatement(self)

'''
Comando
Stm
'''

class Statement:
    def accept(self, visitor):
        pass

class ExpressionStm(Statement):
    def __init__(self, Expression):
        self.expression = Expression
    def accept(self, visitor):
        return visitor.visitExpressionStm(self)

class WhileStm(Statement):
    def __init__(self, Expression, Body):
        self.expression = Expression
        self.block = Body
    def accept(self, visitor):
        return visitor.visitWhileStm(self)

class ReturnStm(Statement):
    def __init__(self, Expression):
        self.expression = Expression
    def accept(self, visitor):
        return visitor.visitReturnStm(self)

class PassStm(Statement):
    def accept(self, visitor):
        return visitor.visitPassStm(self)

'''
Expressoes
Exp
'''

class Expression:
    def accept(self, visitor):
        pass

class AssignExp(Expression):
    def __init__(self, Expression1, Expression2):
        self.leftExpression = Expression1
        self.rightExpression = Expression2
    def accept(self, visitor):
        return visitor.visitAssignExp(self)

class SomaExp(Expression):
    def __init__(self, Expression1, Expression2):
        self.leftExpression = Expression1
        self.rightExpression = Expression2
    def accept(self, visitor):
        return visitor.visitSomaExp(self)


class MulExp(Expression):
    def __init__(self, Expression1, Expression2):
        self.leftExpression = Expression1
        self.rightExpression = Expression2
    def accept(self, visitor):
        return visitor.visitMulExp(self)


class PotExp(Expression):
    def __init__(self, Expression1, Expression2):
        self.leftExpression = Expression1
        self.rightExpression = Expression2
    def accept(self, visitor):
        return visitor.visitPotExp(self)


class CallExp(Expression):
    def __init__(self, Call):
        self.call = Call
    def accept(self, visitor):
        return visitor.visitCallExp(self)

class NumExp(Expression):
    def __init__(self, Number):
        self.number = Number
    def accept(self, visitor):
        return visitor.visitNumExp(self)

class IdExp(Expression):
    def __init__(self, ID):
        self.id = ID
    def accept(self, visitor):
        return visitor.visitIdExp(self)

class SelfExp(Expression):
    def __init__(self, ID):
        self.id = ID
    def accept(self, visitor):
        return visitor.visitSelfExp(self)

class StarIDExp(Expression):
    def __init__(self, ID):
        self.id = ID
    def accept(self, visitor):
        return visitor.visitSelfExp(self)

class DStarIDExp(Expression):
    def __init__(self, ID):
        self.id = ID
    def accept(self, visitor):
        return visitor.visitSelfExp(self)

class BooleanExp(Expression):
    def __init__(self, BoolValue):
        self.boolValue = BoolValue
    def accept(self, visitor):
        return visitor.visitBooleanExp(self)

class AccessExp(Expression):
    def __init__(self, name, Expression):
        self.name = name
        self.expression = Expression
    def accept(self, visitor):
        return visitor.visitAccessExp(self)

'''
Chamada de funcao
Call
'''
class Call:
    def accept(self, visitor):
        pass

class CallWithParameters(Call):
    def __init__ (self, ID, Parameters):
        self.nameFunction = ID
        self.parameters = Parameters
    def accept(self, visitor):
        return visitor.visitCallWithParameters(self)

class CallWithoutParameters(Call):
    def __init__(self, ID):
        self.nameFunction = ID
    def accept(self, visitor):
        return visitor.visitCallWithoutParameters(self)


'''
Parametros de uma chamada de funcao
Params
'''
class Parameters:
    def accept(self, visitor):
        pass

class CompoundParameter(Parameters):
    def __init__(self, Expression, Parameters):
        self.expression = Expression
        self.parameters = Parameters
    def accept(self, visitor):
        return visitor.visitCompoundParameter(self)

class SingleParameter(Parameters):
    def __init__(self, Expression):
        self.expression = Expression
    def accept(self, visitor):
        return visitor.visitSingleParameter(self)
