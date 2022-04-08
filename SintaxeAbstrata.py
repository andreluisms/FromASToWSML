from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

'''
Programa
'''
class Program:
    @abstractmethod
    def accept(self, visitor):
        pass

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
ClassBody
'''
class ClassBody:
    @abstractmethod
    def accept(self, visitor):
        pass


class ClassBodyConcrete(ClassBody):
    def __init__(self, decls):
        self.decls = decls
    def accept(self, visitor):
        pass


'''
decls
'''
class Decls:
    @abstractmethod
    def accept(self, visitor):
        pass


class SingleDecl(Decls):
    def __init__(self, decl):
        self.decl = decl
    def accept(self, visitor):
        pass


class CompoundDecl(Decls):
    def __init__(self, decl, decls):
        self.decl = decl
        self.decls = decls
    def accept(self, visitor):
        pass


'''
Declaracao de funcao
FuncDecl
'''
class AttributeDef:
    def __init__(self, ID, exp):
         self.ID = ID
         self.exp = exp
    def accept(self, visitor):
        pass

class FuncDecl:
    @abstractmethod
    def accept(self, visitor):
        pass

class FuncDeclConcrete(FuncDecl):
    def __init__(self, signature, body):
        self.signature = signature
        self.body = body
    def accept(self, visitor):
        return visitor.visitFuncDeclConcrete(self)

'''
Assinatura de funcao
Signature
'''
class Signature:
    @abstractmethod
    def accept(self, visitor):
        pass


class SignatureConcrete(Signature):
    def __init__(self, type, id, sigParams):
        self.type = type
        self.id = id
        self.sigParams = sigParams
    def accept(self, visitor):
        return visitor.visitSignatureConcrete(self)
'''
Parametros de assinatura de funcao
SigParams
'''

class SigParams:
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleSigParams(SigParams):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitSingleSigParams(self)


class CompoundSigParams(SigParams):
    def __init__(self, id, sigParams):
        self.id = id
        self.sigParams = sigParams
    def accept(self, visitor):
        return visitor.visitCompoundSigParams(self)

'''
Corpo de uma funcao
Body
'''

class Body:
    @abstractmethod
    def accept(self, visitor):
        pass


class BodyConcrete(Body):
    def __init__(self, stms):
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitBodyConcrete(self)

'''
Comandos
Stms
'''

class Stms:
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleStm(Stms):
    def __init__(self, stm):
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitSingleStm(self)

class CompoundStm(Stms):
    def __init__(self, stm, stms):
        self.stm = stm
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitCompoundStm(self)

'''
Comando
Stm
'''

class Stm:
    @abstractmethod
    def accept(self, visitor):
        pass

class StmExp(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmExp(self)

class StmWhile(Stm):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block
    def accept(self, visitor):
        return visitor.visitStmWhile(self)

class StmReturn(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmReturn(self)

'''
Expressoes
Exp
'''

class Exp:
    @abstractmethod
    def accept(self, visitor):
        pass

class AssignExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitAssignExp(self)

class SomaExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitSomaExp(self)


class MulExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitMulExp(self)


class PotExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitPotExp(self)


class CallExp(Exp, Stm):
    def __init__(self, call):
        self.call = call

    def accept(self, visitor):
        return visitor.visitCallExp(self)

class NumExp(Exp):
    def __init__(self, num):
        self.num = num
    def accept(self, visitor):
        return visitor.visitNumExp(self)


class IdExp(Exp):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitIdExp(self)

class BooleanExp(Exp):
    def __init__(self, boolValue):
        self.boolValue = boolValue
    def accept(self, visitor):
        return visitor.visitBooleanExp(self)

'''
Chamada de funcao
Call
'''
class Call:
    @abstractmethod
    def accept(self, visitor):
        pass

class ParamsCall(Call):
    def __init__ (self, id, params):
        self.id = id
        self.params = params
    def accept(self, visitor):
        return visitor.visitParamsCall(self)

class NoParamsCall(Call):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitNoParamsCall(self)


'''
Parametros de uma chamada de funcao
Params
'''
class Params:
    @abstractmethod
    def accept(self, visitor):
        pass

class CompoundParams(Params):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params
    def accept(self, visitor):
        return visitor.visitCompoundParams(self)

class SingleParam(Params):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitSingleParam(self)