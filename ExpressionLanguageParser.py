# Rascunho da gramatica
# program → funcdecl | funcdecl program
# funcdecl → signature body
# signature → id id ( sigParams)
# sigparams → ID ID | ID ID COMMA sigparams
# body → { stms }
# stms → stm  | stm  stms
# stm → exp ;  | while ( exp ) body | return exp ;
# call → id ( params )
# exp → exp + exp | exp * exp | exp ^ exp | call | assign | num | id
# call → id (params) | id ( )
# params → exp, params | exp
# assign → id = exp

import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa

def p_program1(p):
    ''' program : CLASS ID LPAREN ID IGUAL ID RPAREN DP classbody '''
    p[0]= sa.SingleClass(p[2], p[4] + p[5] + p[6], p[9])
 
def p_program2(p):
    '''program :  CLASS ID LPAREN ID RPAREN DP classbody'''
    p[0]= sa.SingleClass(p[2], p[4], p[7])
 
def p_program3(p):
    '''program :   CLASS ID DP classbody''' 
    p[0]= sa.SingleClass(p[2], None, p[4])

def p_program4(p):
    '''program :   CLASS ID LPAREN ID IGUAL ID RPAREN DP classbody program''' 
    p[0]= sa.CompoundClass(p[2], p[4] + p[5] + p[6], p[9], p[10])

def p_program5(p):
    '''program :   CLASS ID LPAREN ID RPAREN DP classbody program'''
    p[0]= sa.CompoundClass(p[2], p[4], p[7], p[8])

def p_program6(p):
    '''program :   CLASS ID DP classbody program'''
    p[0]= sa.CompoundClass(p[2], None, p[4], p[5])



def p_classbody(p):
    '''  classbody : decls '''
    p[0] = sa.ClassBody(p[1])

def p_decls(p):
    ''' decls : decl decls 
               | decl '''

    if (len(p) == 2):
        p[0] = sa.SingleDeclaration(p[1])
    else:
        p[0] = sa.CompoundDeclaration(p[1], p[2])

def p_decl1(p):
    ''' decl : funcdecl  '''
    p[0] = p[1]


def p_decl2(p):
    ''' decl : ID IGUAL exp  '''
    p[0] = sa.AttributeDeclaration(p[1], p[3])

def p_funcdecl(p):
    '''funcdecl : signature body'''
    p[0] = sa.FunctionDeclaration(p[1], p[2])

def p_signature1(p):
    '''signature : DEF ID LPAREN sigparams RPAREN DP'''
    p[0] = sa.Signature(p[2], p[4])

def p_signature2(p):
    '''signature : DEF ID LPAREN RPAREN DP '''
    p[0] = sa.Signature(p[2], None)



def p_sigparams(p):
    '''sigparams : ID
                  | SELF
                  | ID COMMA sigparams
                  | SELF COMMA sigparams
    '''
    if (len(p) == 2):
        p[0] = sa.SingleSigParameter(p[1])
    else:
        p[0] = sa.CompoundSigParameter(p[1], p[3])

def p_body(p):
    ''' body : stms '''
    p[0] = sa.Body(p[1])

def p_stms(p):
    ''' stms : stm
            | stm stms'''
    if (len(p) == 2):
        p[0] = sa.SingleStatement(p[1])
    else:
        p[0] = sa.CompoundStatement(p[1], p[2])

def p_stm1(p):
    ''' stm :  exp '''
    p[0] = sa.ExpressionStm(p[1])

def p_stm2(p):
    ''' stm :  WHILE exp DP body '''
    p[0] = sa.StmWhileStmWhile(p[2], p[4])

def p_stm3(p):
    ''' stm :  RETURN exp '''
    p[0] = sa.ReturnStm(p[2])

def p_stm4(p):
    ''' stm : PASS '''
    p[0] = sa.PassStm()

def p_exp_assign(p):
    ''' exp :    exp IGUAL exp1
              | exp1'''
    if (len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = sa.AssignExp(p[1], p[3])

def p_exp1_soma(p):
    '''exp1 : exp1 SOMA exp2
         | exp2'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = sa.SomaExp(p[1], p[3])


def p_exp2_vezes(p):
   '''exp2 : exp2 VEZES exp3
           | exp3'''
   if len(p) == 2:
       p[0] = p[1]
   else:
       p[0] = sa.MulExp(p[1], p[3])


def p_exp3_pot(p):
    '''exp3 : exp4 POT exp3
            | exp4'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = sa.PotExp(p[1], p[3])

def p_exp4_call(p):
    '''exp4 : call'''
    p[0] = sa.CallExp(p[1])

def p_exp4_number(p):
    '''exp4 : NUMBER'''
    p[0] = sa.NumExp(p[1])

def p_exp4_id(p):
    '''exp4 : ID'''
    p[0] = sa.IdExp(p[1])

def p_exp4_boolean(p):
    '''exp4 : TRUE
            | FALSE'''
    p[0] = sa.BooleanExp(p[1])

def p_exp4_singleSelf(p):
    '''exp4 : SELF '''
    p[0] = sa.SelfExp(p[1])

def p_exp4_compID(p):
    '''exp4 : ID P exp4 '''
    p[0] = sa.AccessExp(sa.IdExp(p[1]), p[3])

def p_exp4_compSelf(p):
    '''exp4 : SELF P exp4'''
    p[0] = sa.AccessExp(sa.SelfExp([1]), p[3])

def p_call_id_params(p):
    '''call : ID LPAREN params RPAREN
            | ID LPAREN RPAREN'''
    if len(p) == 5:
        p[0] = sa.CallWithParameters(p[1], p[3])
    else:
        p[0] = sa.CallWithoutParameters(p[1])


def p_params_ids(p):
    '''params : exp COMMA params
            | exp '''
    if len(p) == 2:
        p[0] = sa.SingleParameter(p[1])
    elif len(p) == 4:
        p[0] = sa.CompoundParameter(p[1], p[3])

def p_error(p):
    print("Syntax error in input!")