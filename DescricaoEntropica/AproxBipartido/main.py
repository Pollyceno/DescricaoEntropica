#import math
import numpy as np
import sys
sys.path.append('..')
np.set_printoptions(threshold=sys.maxsize)

import itertools as itt
import os

#from src.visualize_2D import visualize_2D
from src.main import fourier_motzkin_eliminate_single
#from src.polytope import translate
from src.redundancy_reduction import elimina_redundancia, testa_redundancia
from desc_entro.desc_entro import desigualdades_basicas, cenario_marginal, cenario_marginal2, restricoes_lineares, monta_matriz
from desc_entro.traduz import traduz
from desc_entro.eliminacao import elimina
from desc_entro.rotulo import *
from bipartido import *
from desc_entro.compara import compara, compara2, dependencia


import time


tempo = time.time()

##########################################################################################################################
						# DESIGUALDADES BASICAS
##########################################################################################################################
print('Listando desigualdades basicas')
n = 6

(A,vetor_H)=desigualdades_basicas(n)
basicas = A
b=np.zeros((len(A),1))

##########################################################################################################################
						# RELACOES DE INDEPENDENCIA
##########################################################################################################################
print('Restricoes lineares')
restri=np.array([[[0],[5],[]],[[1],[5],[]],[[0,1],[5],[]],[[0,1],[3],[2,5]],[[0],[3],[2,5]],[[1],[3],[2,5]],[[0,1],[4],[2,5]],[[0],[4],[2,5]],[[1],[4],[2,5]],[[0],[3,4],[2,5]],[[1],[3,4],[2,5]],[[0,1],[3,4],[2,5]],[[2],[0,1,5]],[[3],[2,5]],[[4],[2,5]],[[3,4],[2,5]]]) #restricoes lineares a ser gerada
#restri=np.array([[[0,1],[5],[]],[[0],[5],[]],[[1],[5],[]],[[0,1],[2,3],[4,5]],[[0],[2,3],[4,5]],[[1],[2,3],[4,5]],[[0,1],[2],[4,5]],[[0,1],[3],[4,5]],[[0],[2],[4,5]],[[0],[3],[4,5]],[[1],[2],[4,5]],[[1],[3],[4,5]],[[4],[0,1,5]],[[2,3],[4,5]],[[2],[4,5]],[[3],[4,5]]]) #restricoes lineares a ser gerada
#restri=np.array([[[0,1],[5],[]],[[0],[5],[]],[[1],[5],[]],[[0,1],[2],[4,5]],[[0,1],[3],[4,5]],[[0],[2],[4,5]],[[0],[3],[4,5]],[[1],[2],[4,5]],[[1],[3],[4,5]],[[4],[0,1,5]],[[2],[4,5]],[[3],[4,5]]]) #restricoes lineares a ser gerada
#restri=np.array([[[4],[0,1,5]],[[2],[4,5]],[[3],[4,5]]]) #restricoes lineares a ser gerada

#restri=np.array([[[4],[0,1,5]],[[2,3],[4,5]]]) #restricoes lineares a ser gerada
C=restricoes_lineares(restri,n)

newrow=np.zeros(len(vetor_H), dtype='int')
C = np.vstack([C, newrow])
C[len(C)-1][vetor_H.index((0,1,5))] = 1
C[len(C)-1][vetor_H.index((0,))] = -1
C[len(C)-1][vetor_H.index((1,))] = -1
C[len(C)-1][vetor_H.index((5,))] = -1

d=np.zeros((len(C),1))

A=np.vstack((A,C,-C))
b=np.vstack((b,d,-d))

##########################################################################################################################
						# RESTRICOES DO PROTOCOLO
##########################################################################################################################
print('Gerando entopias do protocolo')

#Gerando lista com todas as marginais sem m
CM = np.array([[0,1,3],[0,1,4]]) #Cenario marginal
(M,Ind)=cenario_marginal(CM, 6)
(H, lista) = verifica_fronteira2(M)
print(H)
print(lista)

#Encontando Hm
Hm = vetor_H.index((2,))
#print(vetor_H[i])

#Montando matriz de resticoes do protocolo
newrow=np.zeros(len(vetor_H), dtype='int')
C=np.array([newrow])
d = np.zeros((len(A[0]),1))
j = 0
for k in lista:
	C[j][vetor_H.index(k)] = 1
	C = np.vstack([C, newrow])
	j = j + 1
C = np.delete(C, (len(C)-1), axis = 0)

#print(C)
#print(H)
#print(len(H))
#print(len(C))

##########################################################################################################################
						# GERANDO TODAS AS ENTROPIAS DO CENARIO MARGINAL FINAL PARA POSTERIORMENTE TESTAR AS DESIGUALDADES 
##########################################################################################################################

print('Gerando entopias do protocolo')
CM2 = np.array([[0,1,2,3],[0,1,2,4]]) #Cenario marginal
(M2, Ind2) = cenario_marginal(CM2, n)# Indics a eliminar		
#(H2, lista2) = verifica_fronteira2(M2)

pabDxy = recurso(1)
prot = rotulo2(pabDxy)
print('Depois',len(prot))

for p in prot:
	(H2, lista2) = verifica_fronteira2(M2, p)
'''
print(H2[M2.index((2,))])
print(H2[M2.index((0,1))])
print(H2[M2.index((2,3))])
print(H2[M2.index((0,2,3))])
print(H2[M2.index((0,2,4))])
print(H2[M2.index((0,1,2,4))])
'''

##########################################################################################################################
						# VERIFICANDO CLASSICALIDADE
##########################################################################################################################

aux = 0
path0 = '1/'
os.mkdir(path0)
rodada = 0
while(aux < 1):#Enquanto nao encontra desigualdade
	aux = aux + 1
	
	print('Verificando classicalidade')
	
	bound = 1
	A_red = elimina(vetor_H, Hm, A, C, H, bound)
	print(len(A_red))
	
	path = (path0+str(rodada)+'-'+str(len(A_red))+'/')
	name = ('reduzido'+str(len(A_red))+'.txt')
	os.mkdir(path)
	np.savetxt(path+name, A_red, fmt="%s")

	rodada = rodada + 1
	
	
	##########################################################################################################################
							# CENARIO MAGINAL LAMBDA
	##########################################################################################################################
	
	#Ac = np.loadtxt('ineq.txt')
	Ac = A_red
	bc=np.zeros((len(Ac),1))
	
	
	print('Cenario marginal LAMBDA')
	CM = np.array([[0,1,2,3,4]]) #Cenario marginal
	(M, Ind) = cenario_marginal(CM, n)# Indics a eliminar
	print('Variaveis a eliminar: ', len(Ind))
	
	
	##########################################################################################################################
							# FOURIER MOTZKIN LAMBDA
	##########################################################################################################################
	
	print('Fourier Motzkin LAMBDA')
	cont = 0
	restante = Ind # indices que restam a eliminar. Inicialmente ele e igual ao Ind
	for var_index in Ind:
		porc = int(cont/len(Ind)*100)
		print('Porcentagem:', porc, '%')
		cont = cont + 1
		if(len(Ac) != 0):
			np.savetxt(path+"tempAiL.txt", Ac, fmt="%s")
			#np.savetxt("tempBiCI.txt", bc, fmt="%s")
		restante = np.delete(restante, np.where(restante == var_index)) # Indices restante a eliminar
		(A_new,b_new,data)=fourier_motzkin_eliminate_single(var_index,Ac,bc,atol=10**-8)
		np.savetxt(path+'dados_relevantes_L.txt', [['Eliminando outros'],['Porcentagem:', porc, '%'],['Input FM:',len(Ac)],['Numero de verificacoes:', data[1]],['Output FM:', data[0]], ['Elementares:', len(A_new)],['Indices restantes:', restante]], fmt="%s")
		Ac=A_new
		bc=b_new
	
	np.savetxt(path+"desig_sem_Lambda.txt", Ac, fmt="%s")
	#np.savetxt("b_tripartido.txt", bc, fmt="%s")
	
	##########################################################################################################################
							# CENARIO MARGINAL FINAL
	##########################################################################################################################
	print('Cenario marginal LAMBDA')
	CM = np.array([[0,1,2,3],[0,1,2,4]]) #Cenario marginal
	(M, Ind) = cenario_marginal2(M, CM, n)# Indics a eliminar
	print('Variaveis a eliminar: ', len(Ind))
	
	
	##########################################################################################################################
							# FOURIER MOTZKIN FINAL
	##########################################################################################################################
	
	print('Fourier Motzkin final')
	cont = 0
	restante = Ind # indices que restam a eliminar. Inicialmente ele e igual ao Ind
	for var_index in Ind:
		porc = int(cont/len(Ind)*100)
		print('Porcentagem:', porc, '%')
		cont = cont + 1
		if(len(Ac) != 0):
			np.savetxt(path+"tempAiCI.txt", Ac, fmt="%s")
			#np.savetxt("tempBiCI.txt", bc, fmt="%s")
		restante = np.delete(restante, np.where(restante == var_index)) # Indices restante a eliminar
		(A_new,b_new,data)=fourier_motzkin_eliminate_single(var_index,Ac,bc,atol=10**-8)
		np.savetxt(path+'dados_relevantes_CI.txt', [['Eliminando outros'],['Porcentagem:', porc, '%'],['Input FM:',len(Ac)],['Numero de verificacoes:', data[1]],['Output FM:', data[0]], ['Elementares:', len(A_new)],['Indices restantes:', restante]], fmt="%s")
		Ac=A_new
		bc=b_new
	
	np.savetxt(path+"desig_CI.txt", Ac, fmt="%s")
	
	
	##########################################################################################################################
							# ARRUMANDO COLUNAS BASICAS GERAL
	##########################################################################################################################
	print('Comparando com as basicas')
	
	matriz_desig = np.zeros((len(Ac),len(basicas[0])), dtype='float')
	a=np.zeros((len(matriz_desig),1))
	#print(matriz_desig)
	
	for i in range(0,len(Ac)):
		for j in range(0,len(Ac[0])):
			if(Ac[i][j] != 0.0):
				matriz_desig[i][vetor_H.index(M[j])] = Ac[i][j]
	
	##########################################################################################################################
							# APLICANDO O LEMA AS DESIGUALDADES SUJEITAS AS BASICAS
	##########################################################################################################################
	matriz_desig = compara(matriz_desig, basicas)
	#print(matriz_desig)
	print('Desigualdades nao triviais: ',len(matriz_desig))
	
	#Voltando para o cenario maginal
	Ac = np.zeros((len(matriz_desig),len(M)), dtype='float')
	for i in range(0,len(matriz_desig)):
		for j in range(0,len(matriz_desig[0])):
			if(matriz_desig[i][j] != 0.0):
				Ac[i][M.index(vetor_H[j])] = matriz_desig[i][j]
	
	np.savetxt(path+"nao_triviais.txt", Ac, fmt="%s")
	
	
	##########################################################################################################################
							# TRADUCAO NAO TRIVIAIS
	##########################################################################################################################
	
	X = ['Z0','Z1','M','G0','G1','L'] #Aqui e passado o cenario completo, porque matriz_desig esta na base das desigualdades basicas
	
	T = traduz(matriz_desig, X)
	
	np.savetxt(path+"traducao_nao_triv.txt", T, fmt="%s")
	
	##########################################################################################################################
							# TESTA QUAIS DAS 54 DESIGUALDADES CONHECIDAS PODEM SER OBTIDAS DO CONJUNTO OBTIDO
	##########################################################################################################################
	conhecidas = np.loadtxt('54_nao_triv.txt')
	
	#newrow=np.zeros(len(conhecidas[0]), dtype='int')
	#presentes=np.array([newrow])
	
	#for k in conhecidas:
#		for l in conhecidas:
#			if(np.array_equal(k,l)==True):
#				print(np.array_equal(k,l))
#				presentes = A=np.vstack((presentes, k))
	
	
	presentes = compara2(conhecidas, matriz_desig)
	
	#print(presentes)
	print('Pesentes:', len(presentes))
	
	
	##########################################################################################################################
							# TRADUCAO PRESENTES
	##########################################################################################################################
	
	X = ['Z0','Z1','M','G0','G1','L'] #Aqui e passado o cenario completo, porque matriz_desig esta na base das desigualdades basicas
	
	T = traduz(presentes, X)
	
	np.savetxt(path+"presentes.txt", T, fmt="%s")
	
	##########################################################################################################################
										# TESTA VIOLACAO DAS DESIGUALDADES OBTIDAS
	##########################################################################################################################
	print('Testando desigualdades')
	values = Ac@H2
	atol=10**-8
	mat_viola = []
	violacao = []
	line = 0
	for u in range(0,len(values)):
		if(values[u]>= atol):
			violacao = np.append(violacao, values[u])
			mat_viola = np.append(mat_viola, Ac[u])
			line = line +1
	mat_viola = np.reshape(mat_viola,(line,len(Ac[0])))
	np.savetxt(path+"desig_violadas.txt", mat_viola, fmt="%s")
	np.savetxt(path+"violacao.txt", violacao, fmt="%s")
	##########################################################################################################################
							# TRADUCAO DESIGUALDADES VIOLADAS
	##########################################################################################################################
	
	X = ['Z0','Z1','M','G0','G1','L']#Aqui e passado o cenario completo, porque matriz_desig esta na base das desigualdades basicas
	
	T = traduz(mat_viola, X, Ind2)
	
	np.savetxt(path+"traducao_desig_violadas.txt", T, fmt="%s")
	
	##########################################################################################################################
							# FIM
	##########################################################################################################################

print('Finished!')
print("Total--- %s seconds ---" % (time.time() - tempo))
