class AlunoUFS(Estudante):
    def __shop__(self, Expression1, Expression2):
        self.leftExpression = Expression1
        self.rightExpression = Expression2
    def accept(self, visitor):
        return visitor.visitMulExp(self)
