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
    p[0] = sa.ClassBodyConcrete(p[1])

def p_decls(p):
    ''' decls : decl decls 
               | decl '''

    if (len(p) == 2):
        p[0] = sa.SingleDecl(p[1])
    else:
        p[0] = sa.CompoundDecl(p[1], p[2])

def p_decl(p):
    ''' decl : funcdecl 
             | ID IGUAL exp PV '''

    if (len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = sa.AttributeDef(p[1], p[3])

def p_funcdecl(p):
    '''funcdecl : signature body'''
    p[0] = sa.FuncDeclConcrete(p[1], p[2])

def p_signature(p):
    '''signature : DEF ID LPAREN sigparams RPAREN DP
                 | DEF ID LPAREN RPAREN DP '''
    if (isinstance(p[4], sa.SigParams)):
        p[0] = sa.SignatureConcrete(p[1], p[2], p[4])
    else:
        p[0] = sa.SignatureConcrete(p[1], p[2], None)

def p_sigparams(p):
    '''sigparams : ID
                  | SELF
                  | ID COMMA sigparams
                  | SELF COMMA sigparams
    '''
    if (len(p) == 2):
        p[0] = sa.SingleSigParams(p[1])
    else:
        p[0] = sa.CompoundSigParams(p[1], p[3])

def p_body(p):
    ''' body : stms '''
    p[0] = sa.BodyConcrete(p[1])

def p_stms(p):
    ''' stms : stm
            | stm stms'''
    if (len(p) == 2):
        p[0] = sa.SingleStm(p[1])
    else:
        p[0] = sa.CompoundStm(p[1], p[2])

def p_stm(p):
    ''' stm :  exp
             | WHILE exp DP body
             | RETURN exp 
             | PASS '''
    if (len(p) == 3):
        p[0] = sa.StmExp(p[1])
    elif (p[1] == 'while'):
        p[0] = sa.StmWhile(p[3], p[5])
    elif (p[1] == 'return'):
        p[0] = sa.StmReturn(p[2])
    else:
        print('Gerei None', p[1])

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
    '''exp4 : call
            | NUMBER
            | ID
            | TRUE
            | FALSE
            | SELF 
            | SELF P exp4'''
    if isinstance(p[1], sa.Call):
        p[0] = sa.CallExp(p[1])
    elif isinstance(p[1], int):
        p[0] = sa.NumExp(p[1])
    elif (p[1] == 'true' or p[1] == 'false'):
        p[0] = sa.BooleanExp(p[1])
    else:
        p[0] = sa.IdExp(p[1])


def p_call_id_params(p):
    '''call : ID LPAREN params RPAREN
            | ID LPAREN RPAREN'''
    if len(p) == 5:
        p[0] = sa.ParamsCall(p[1], p[3])
    else:
        p[0] = sa.NoParamsCall(p[1])


def p_params_ids(p):
    '''params : exp COMMA params
            | exp '''
    if len(p) == 2:
        p[0] = sa.SingleParam(p[1])
    elif len(p) == 4:
        p[0] = sa.CompoundParams(p[1], p[3])

def p_error(p):
    print("Syntax error in input!")