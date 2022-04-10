from abc import abstractmethod
from abc import ABCMeta

class AbstractVisitor(metaclass=ABCMeta):

    @abstractmethod
    def visitSingleClass(self, singleClass):
        pass

    @abstractmethod
    def visitCompoundClass(self, compoundClass):
        pass

    @abstractmethod
    def visitClassBody(self, bodyConcrete):
        pass

    @abstractmethod
    def visitSingleDeclaration(self, singleDecl):
        pass

    @abstractmethod
    def visitCompoundDeclaration(self, compoundDecl):
        pass

    @abstractmethod
    def visitAttributeDeclaration(self, attributeDecl):
        pass

    @abstractmethod
    def visitFunctionDeclaration(self, funcDecl):
        pass

    @abstractmethod
    def visitSignature(self, signature):
        pass

    @abstractmethod
    def visitSingleSigParameter(self, singleSigParams):
        pass

    @abstractmethod
    def visitCompoundSigParameter(self, compoundSigParams):
        pass

    @abstractmethod
    def visitBody(self, body):
        pass

    @abstractmethod
    def visitSingleStatement(self, singlestm):
        pass

    @abstractmethod
    def visitCompoundStatement(self, compoundStm):
        pass

    @abstractmethod
    def visitExpressionStm(self, stmExp):
        pass

    @abstractmethod
    def visitWhileStm(self, stmWhile):
        pass

    @abstractmethod
    def visitReturnStm(self, stmReturn):
        pass


    @abstractmethod
    def visitPassStm(self, passStm):
        pass

    @abstractmethod
    def visitAssignExp(self, assignExp):
        pass

    @abstractmethod
    def visitSomaExp(self, somaExp):
        pass

    @abstractmethod
    def visitMulExp(self, mulExp):
        pass

    @abstractmethod
    def visitPotExp(self, potExp):
        pass

    @abstractmethod
    def visitCallExp(self, callExp):
        pass

    @abstractmethod
    def visitNumExp(self, numExp):
        pass

    @abstractmethod
    def visitIdExp(self, idExp):
        pass

    @abstractmethod
    def visitSelfExp(self, selfExp):
        pass


    @abstractmethod
    def visitBooleanExp(self, booleanExp):
        pass

    @abstractmethod
    def visitAccessExp(self, accessExp):
        pass

    @abstractmethod
    def visitCallWithParameters(self, paramsCall):
        pass

    @abstractmethod
    def visitCallWithoutParameters(self, simpleCall):
        pass

    @abstractmethod
    def visitCompoundParameter(self, compoundParams):
        pass

    @abstractmethod
    def visitSingleParameter(self, singleParam):
        pass
