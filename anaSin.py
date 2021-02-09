import ply.yacc as yacc
import os
import codecs
import re
from anaLex import tokens
from sys import stdin

precedence = (
	('right','ASSIGN'),
	('right','UPDATE'),
	('left','NE'),
	('left','LT','LTE','GT','GTE'),
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('right','ODD'),
	('left','LPARENT','RPARENT'),
	)

def p_program(p):
	'''program = block '''
	#p[0] = program(p[1],'program')
	print('program')

def p_contsDecl(p):
	'''constDecl = CONST constAsssigmentlist ; '''
	#p[0] = constDecl(p[2])
	print('constDecl')

def p_constDeclEmpty(p):
	'''constDecl = empty'''
	#p[0] = Null()
	print('nulo')

def p_constAssigmenntList1(p):
	'''constAssigmenntList: ID = NUMBER'''
	print('constAssigmenntList 1')

def p_constAssigmenntList2(p):
	'''constAssigmenntList : constAssigmenntList, ID = NUMBER'''
	print('constAssigmenntList 2')

def p_varDecl1(p):
	'''varDecl: VAR ID ;'''
	print('varDecl 1')

def p_varDecl2(p):
	'''varDecl : empty'''
	print('nulo')

def p_idenList1(p):
	''' identList: ID'''
	print('idenList 1')

def p_idenList2(p):
	'''idenList : idenList, ID'''
	print('idenList 2')

def p_procDecl1(p):
	'''procDecl : idenList , ID'''
	print('procDecl 1')

def p_procDeclEmpty(p):
	'''procDecl : empty'''
	print('nulo')

def p_statement1(p):
	'''statement : ID UPDATE expression'''
	print('statement 1')

def p_statement2(p):
	'''statement : CALL ID'''
	print('statement 2')

def p_statement3(p):
	'''statement : BEGIN statementList END'''
	print('statement 3')

def p_statement4(p):
	'''statement : IF condition THEN statement'''
	print('statement 4')

def p_statement5(p):
	'''statement : WHILE condition DO satetement'''
	print('statement 5')

def p_statementEmpty(p):
	'''statement : empty '''
	print('nulo')

def p_statemenList1(p):
	'''statemenList: statement'''
	print('statemenList 1')

def p_statemenList2(p):
	'''statemenList: statementList ; statement'''
	print('statemenList 2')

def p_condition1(p):
	'''condition : ODD expresssion'''
	print('condition 1')

def p_condition2(p):
	'''condition : expression relation expression'''
	print('condition 2')

def p_realtion1(p):
	'''relation : ASSIGN'''
	print('relation 1')

def p_realtion2(p):
	'''relation : NE'''
	print('relation 2')

def p_realtion3(p):
	'''relation : LT'''
	print('relation 3')

def p_realtion4(p):
	'''relation : GT'''
	print('relation 4')

def p_realtion5(p):
	'''relation : LTE'''
	print('relation 5')

def p_realtion6(p):
	'''relation : GTE'''
	print('relation 6')

def p_expression1(p):
	'''expression : term'''
	print('expression 1')

def p_expression2(p):
	'''expression : addingOperator term'''
	print('expression 2')

def p_expression3(p):
	'''expression : expression addingOperator term'''
	print('expression 3')

def p_term1(p):
	'''term : factor'''
	print('term 1')

def p_term2(p):
	'''term : term multiplyingOperator factor'''
	print('term 2')

def p_multiplyingOperator1(p):
	'''multiplyingOperator : TIMES'''
	print('multiplyingOperator 1')

def p_multiplyingOperator2(p):
	'''multiplyingOperator : DIVIDE'''
	print('multiplyingOperator 2')

def p_factor1(p):
	'''factor : ID'''
	print('factor 1')

def p_factor2(p):
	'''factor : NUMBER'''
	print('factor 2')

def p_factor3(p):
	'''factor : LPARENT expression RPARENT'''
	print('factor 3')

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print('error de sintaxis', p)
	print('error en la linea ' + str(p.lineno))

def buscarFicheros(directorio):
	ficheros =[]
	numArchivo = ''
	respuesta = False
	cont = 1

	for base,dirs,files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print ('Has seleccionado',files[int(numArchivo)-1])

	return files[int(numArchivo)-1]

directorio = '/home/brandon/Escritorio/Compilador/testlex/'
archivo = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print(result)