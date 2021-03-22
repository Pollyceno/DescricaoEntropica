import math
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
from desc_entro.compara import compara, compara2, dependencia
from tripartido import *
from rotulo import *
from recurso import *
from grupo import *

import time


tempo = time.time()

##########################################################################################################################
						# DESIGUALDADES BASICAS
##########################################################################################################################
print('Listando desigualdades basicas')
n = 9

(A,vetor_H)=desigualdades_basicas(n)
basicas = A
b=np.zeros((len(A),1))

##########################################################################################################################
						# RELACOES DE INDEPENDENCIA
##########################################################################################################################
print('Restricoes lineares')
#restri=np.array([[[0,1],[5],[]],[[0],[5],[]],[[1],[5],[]],[[0,1],[2,3],[4,5]],[[0],[2,3],[4,5]],[[1],[2,3],[4,5]],[[0,1],[2],[4,5]],[[0,1],[3],[4,5]],[[0],[2],[4,5]],[[0],[3],[4,5]],[[1],[2],[4,5]],[[1],[3],[4,5]],[[4],[0,1,5]],[[2,3],[4,5]],[[2],[4,5]],[[3],[4,5]]]) #restricoes lineares a ser gerada
restri=np.array([[[4],[0,1,8]],[[5],[2,3,8]],[[6,7],[4,5,8]]]) #restricoes lineares a ser gerada
RIC=restricoes_lineares(restri,n)
#d=np.zeros((len(RIC),1))

newrow=np.zeros(len(vetor_H), dtype='int')
RIC = np.vstack([RIC, newrow])
#RIC=np.array([newrow])


RIC[len(RIC)-1][vetor_H.index((0,1,2,3,8))] = 1
RIC[len(RIC)-1][vetor_H.index((0,))] = -1
RIC[len(RIC)-1][vetor_H.index((1,))] = -1
RIC[len(RIC)-1][vetor_H.index((2,))] = -1
RIC[len(RIC)-1][vetor_H.index((3,))] = -1
RIC[len(RIC)-1][vetor_H.index((8,))] = -1
#print(len(C))

RId=np.zeros((len(RIC),1))

A=np.vstack((A,RIC,-RIC))
b=np.vstack((b,RId,-RId))

##########################################################################################################################
						# RESTRICOES DO PROTOCOLO
##########################################################################################################################
print('Gerando entopias do protocolo')
#Gerando lista com todas as marginais sem m
CM = np.array([[0,1,2,3,6],[0,1,2,3,7]]) #Cenario marginal
(M,Ind)=cenario_marginal(CM, 9)
#del M[M.index((4,5))]
#print(M)

pabcDxyz = recurso2(3)

(H) = verifica_fronteira3(M, pabcDxyz)

#Encontando HMxMy
Hm = vetor_H.index((4,5))
#print(vetor_H[i])

#Montando matriz de resticoes do protocolo
newrow=np.zeros(len(vetor_H), dtype='int')
C=np.array([newrow])
d = np.zeros((len(A[0]),1))
j = 0
for k in M:
	C[j][vetor_H.index(k)] = 1
	C = np.vstack([C, newrow])
	j = j + 1
C = np.delete(C, (len(C)-1), axis = 0)

#A = np.loadtxt('reduzido339.txt')


##########################################################################################################################
		# GERANDO TODAS AS ENTROPIAS DO CENARIO MARGINAL FINAL PARA POSTERIORMENTE TESTAR AS DESIGUALDADES 
##########################################################################################################################

print('Gerando TODAS as entopias do protocolo')
CM2 = np.array([[0,1,2,3,4,5,6],[0,1,2,3,4,5,7]]) #Cenario marginal
(M2, Ind2) = cenario_marginal(CM2, n)# Indics a eliminar

pabcDxyz = recurso2(3)

(H2) = verifica_fronteira3(M2,pabcDxyz)

##########################################################################################################################
		# GERANDO TODAS AS ENTROPIAS DO CENARIO MARGINAL FINAL PARA POSTERIORMENTE TESTAR A OUTRA CAIXA 
##########################################################################################################################

print('Gerando TODAS as entopias do protocolo para caixas CLASSE 4')
CM3 = np.array([[0,1,2,3,4,5,6],[0,1,2,3,4,5,7]]) #Cenario marginal
(M3, Ind3) = cenario_marginal(CM3, n)# Indics a eliminar

pabcDxyz = recurso2(2)

prot = permuta(pabcDxyz)
#print(len(prot))

t=0
H3 = []
for p in prot:
	#print(t)
	t=t+1
	(h3) = verifica_fronteira3(M3, p)
	H3 = np.append(H3, h3)
	if(t==5):
		break

H3 = np.reshape(H3,(5,len(M3)))


##########################################################################################################################
						# VERIFICANDO CLASSICALIDADE
##########################################################################################################################
aux = False
rodada0 = 0
atol=10**-8
while(aux == False):#Enquanto nao encontra desigualdade
	
	print('Verificando classicalidade')
	rodada1=0
	bound = 3.8
	A_red0 = elimina(vetor_H, Hm, A, C, H, bound)

	path0 = ('Classe4-'+str(rodada0)+'-'+str(len(A_red0))+'/')
	name = ('reduzido'+str(len(A_red0))+'.txt')
	os.mkdir(path0)
	np.savetxt(path0+name, A_red0, fmt="%s")
	rodada0 = rodada0 + 1
	
	for r in range(0,1): #Testa 5 vezes para o primeiro nivel de eliminacao
		
		A_red = A_red0
		bound = 3.5

		#while (len(A_red)> 200): #Enquanto o número de desigualdades é maior que 200
		while (bound > 2.01):
			#if(bound>2.01):
			bound = bound - 0.3
			print('bound', bound)
			#print('C', C)
			#print('H', H)
			A_red = elimina(vetor_H, Hm, A_red, C, H, bound)
			
		print('Reduzidas:',len(A_red))
		
		path1 = (str(rodada1)+'-red'+str(len(A_red))+'b'+str(bound)+'/')
		name = ('reduzido'+str(len(A_red))+'.txt')
		path =path0+path1
		os.mkdir(path)
		np.savetxt(path+name, A_red, fmt="%s")

		rodada1 = rodada1 + 1
		

		
		#Ac = np.loadtxt('ineq.txt')
		Ac=A_red
		bc=np.zeros((len(Ac),1))

		#################################################################################################################################
								# INCLUI RIC NOVAMENTE PARA FACILITAR FM
		#################################################################################################################################
		#Ac=np.vstack((Ac,RIC,-RIC))
		#bc=np.vstack((bc,RId,-RId))
		
		#################################################################################################################################
								# CENARIO MARGINAL PARA ELIMINAR LAMBDA
		#################################################################################################################################
		
		print('Cenario marginal LAMBDA')
		CM = np.array([[0,1,2,3,4,5,6,7]]) #Cenario marginal
		(M, Ind) = cenario_marginal(CM, n)# Indics a eliminar
		#print(Ind)

		##########################################################################################################################
								# FOURIER MOTZKIN FINAL LAMBDA
		##########################################################################################################################
		
		print('Fourier Motzkin LAMBDA')
		cont = 0
		restante = Ind # indices que restam a eliminar. Inicialmente ele e igual ao Ind

		parar = 0
		for var_index in Ind:
			porc = int(cont/len(Ind)*100)
			print('Porcentagem:', porc, '%')
			cont = cont + 1
			#if(len(Ac) != 0):
				#np.savetxt(path+"tempAiCI.txt", Ac, fmt="%s")
				#np.savetxt(path+"tempBiCI.txt", bc, fmt="%s")
			phi_positive=[i for i in range(Ac.shape[0]) if Ac[i,var_index]>=atol] # list of positive var entries
			phi_negative=[i for i in range(Ac.shape[0]) if Ac[i,var_index]<=-atol]  # list of negative var entries

			verificacoes = (len(phi_positive)*len(phi_negative))

			if(verificacoes > 7000):
				parar = 1
				np.savetxt(path+'divergiu.txt', ['verificacoes:', verificacoes], fmt="%s")
				break
			restante = np.delete(restante, np.where(restante == var_index)) # Indices restante a eliminar
			(A_new,b_new,data)=fourier_motzkin_eliminate_single(var_index,Ac,bc,atol=10**-8)
			np.savetxt(path+"dados_relevantes_L.txt", [['Eliminando LAMBDA'],['Porcentagem:', porc, '%'],['Input FM:',len(Ac)],['Numero de verificacoes:', data[1]],['Output FM:', data[0]], ['Elementares:', len(A_new)],['Indices restantes:', restante]], fmt="%s")
			Ac=A_new
			bc=b_new
		if(parar == 1):
			break
		
		np.savetxt(path+"desigualdades_SEM_LAMBDA.txt", Ac, fmt="%s")
		#np.savetxt(path+"valores_b__SEM_LAMBDA.txt", bc, fmt="%s")
		
		##########################################################################################################################
								# CENARIO MAGINAL FINAL
		##########################################################################################################################
		
		print('Cenario marginal final')
		CM = np.array([[0,1,2,3,4,5,6],[0,1,2,3,4,5,7]]) #Cenario marginal
		(M, Ind) = cenario_marginal2(M, CM, n)# Indics a eliminar
		print('Variaveis a eliminar: ', len(Ind))
		
		
		##########################################################################################################################
								# FOURIER MOTZKIN FINAL
		##########################################################################################################################
		
		print('Fourier Motzkin final')
		cont = 0
		restante = Ind # indices que restam a eliminar. Inicialmente ele e igual ao Ind
		parar = 0
		for var_index in Ind:
			porc = int(cont/len(Ind)*100)
			print('Porcentagem:', porc, '%')
			cont = cont + 1
			#if(len(Ac) != 0):
				#np.savetxt(path+"tempAiCI.txt", Ac, fmt="%s")
				#np.savetxt(path+"tempBiCI.txt", bc, fmt="%s")
			phi_positive=[i for i in range(Ac.shape[0]) if Ac[i,var_index]>=atol] # list of positive var entries
			phi_negative=[i for i in range(Ac.shape[0]) if Ac[i,var_index]<=-atol]  # list of negative var entries

			verificacoes = (len(phi_positive)*len(phi_negative))

			if(verificacoes > 7000):
				parar = 1
				break
			restante = np.delete(restante, np.where(restante == var_index)) # Indices restante a eliminar
			(A_new,b_new,data)=fourier_motzkin_eliminate_single(var_index,Ac,bc,atol=10**-8)
			np.savetxt(path+"dados_relevantes_F.txt", [['Eliminando outros'],['Porcentagem:', porc, '%'],['Input FM:',len(Ac)],['Numero de verificacoes:', data[1]],['Output FM:', data[0]], ['Elementares:', len(A_new)],['Indices restantes:', restante]], fmt="%s")
			Ac=A_new
			bc=b_new

		if(parar == 1):
			break
		
		#print(Ac)
		np.savetxt(path+"desig_tripartido.txt", Ac, fmt="%s")
		#np.savetxt(path+"b_tripartido.txt", bc, fmt="%s")
		
		
		##########################################################################################################################
								# ARRUMANDO COLUNAS BASICAS GERAL
		##########################################################################################################################
		
		matriz_desig = np.zeros((len(Ac),len(basicas[0])), dtype='float')
		#print(matriz_desig)
		
		for i in range(0,len(Ac)):
			for j in range(0,len(Ac[0])):
				if(Ac[i][j] != 0.0):
					matriz_desig[i][vetor_H.index(M[j])] = Ac[i][j]
		
		##########################################################################################################################
								# APLICANDO O LEMA AS DESIGUALDADES SUJEITAS AS BASICAS
		##########################################################################################################################
		
		matriz_desig = compara(matriz_desig, basicas)
		
		Ac = np.zeros((len(matriz_desig),len(M)), dtype='float')
		
		#Voltando para o cenario maginal
		for i in range(0,len(matriz_desig)):
			for j in range(0,len(matriz_desig[0])):
				if(matriz_desig[i][j] != 0.0):
					Ac[i][M.index(vetor_H[j])] = matriz_desig[i][j]
		#print(matriz_desig)
		print('Desigualdades nao triviais: ',len(matriz_desig))
		np.savetxt(path+"nao_triviais.txt", Ac, fmt="%s")
		
		
		##########################################################################################################################
								# TRADUCAO
		##########################################################################################################################
		
		X = ['X0','X1','Y0','Y1','Mx','My','Z0','Z1','L'] #Aqui e passado o cenario completo, porque matriz_desig esta na base das desigualdades basicas
		
		T = traduz(matriz_desig, X)
		
		np.savetxt(path+"traducao_nao_triv_TRIPARTIDO.txt", T, fmt="%s")
		
		##########################################################################################################################
								# TESTA SE A DESIGUALDADE DO PDF ESTA PRESENTE
		##########################################################################################################################
		conhecida = np.zeros((1,len(vetor_H)), dtype='int')
		
		
		conhecida[len(conhecida)-1][vetor_H.index((0,))] = 1
		conhecida[len(conhecida)-1][vetor_H.index((2,6))] = 2
		conhecida[len(conhecida)-1][vetor_H.index((0,2,6))] = -1
		conhecida[len(conhecida)-1][vetor_H.index((1,))] = 1
		conhecida[len(conhecida)-1][vetor_H.index((3,7))] = 2
		conhecida[len(conhecida)-1][vetor_H.index((1,3,7))] = -1
		conhecida[len(conhecida)-1][vetor_H.index((0,1,6))] = 1
		conhecida[len(conhecida)-1][vetor_H.index((0,1,2,6))] = -1
		conhecida[len(conhecida)-1][vetor_H.index((6,))] = -1
		conhecida[len(conhecida)-1][vetor_H.index((0,1,7))] = 1
		conhecida[len(conhecida)-1][vetor_H.index((0,1,3,7))] = -1
		conhecida[len(conhecida)-1][vetor_H.index((7,))] = -1
		conhecida[len(conhecida)-1][vetor_H.index((4,))] = 1
		conhecida[len(conhecida)-1][vetor_H.index((5,))] = 1
		
		
		presentes = compara2(conhecida, matriz_desig)
		print('Pesentes:', len(presentes))
		
		
		##########################################################################################################################
								# TRADUCAO PRESENTES
		##########################################################################################################################
		
		X = ['X0','X1','Y0','Y1','Mx','My','Z0','Z1','L'] #Aqui e passado o cenario completo, porque matriz_desig esta na base das desigualdades basicas
		
		T = traduz(presentes, X)
		
		np.savetxt(path+"presentes.txt", T, fmt="%s")
		
		##########################################################################################################################
									# TESTA VIOLACAO DAS DESIGUALDADES OBTIDAS PRIMEIRA CAIXA
		##########################################################################################################################
		print('Testando desigualdades PRIMEIRA caixa')
		values = Ac@H2
		atol=10**-8
		mat_viola = []
		line = 0
		for u in range(0,len(values)):
			if(values[u]>= atol):
			#if(values[u]!= 0.0):
				mat_viola = np.append(mat_viola, ((2/values[u])*Ac[u]))
			#else:
			#	mat_viola = np.append(mat_viola, Ac[u])
				line = line +1

		mat_viola = np.reshape(mat_viola,(line,len(Ac[0])))
		#Ac = mat_viola

		np.savetxt(path+"desig_VIOLA_1ST.txt", mat_viola, fmt="%s")
		np.savetxt(path+"violacao_1ST.txt", values, fmt="%s")

		##########################################################################################################################
								# TRADUCAO DESIGUALDADES VIOLADAS
		##########################################################################################################################
		
		X = ['X0','X1','Y0','Y1','Mx','My','Z0','Z1','L'] #Aqui e passado o cenario completo, porque matriz_desig esta na base das desigualdades basicas
		
		T = traduz(mat_viola, X, Ind2)
		
		np.savetxt(path+"traducao_desig_VIOLA_1ST.txt", T, fmt="%s")

		##########################################################################################################################
									# TESTA VIOLACAO DAS DESIGUALDADES OBTIDAS SEGUNDA CAIXA
		##########################################################################################################################
		print('Testando desigualdades SEGUNDA caixa')

		values = Ac@H3[0]
		np.savetxt(path+"values_2ND.txt", values, fmt="%s")

		line = 0
		violacao = []
		caixa = []
		desig = []
		for ac in Ac:
			c = 0
			t = False
			col = 0
			for h3 in H3:
				value = ac@h3
				atol=10**-8
				if(value>=atol): #Se violar
					t = True
					violacao = value
					caixa = c
					desig = line
					np.savetxt(path+"VIOLA_2ND.txt", [['Violacao:', violacao],['Caixa:', caixa],['Desigualdade:', desig]], fmt="%s")
					break
				c = c + 1
			if(t==True):#E violado?
				break
			line = line + 1
		
		##########################################################################################################################
									# SE ENCONTRAR A DESIGUALDADE PARA O PROGRAMA
		##########################################################################################################################
		
		if(len(presentes)!=0 or t==True):
		#if(t==True):
			#np.savetxt(path+"ENCONTREI.txt", ['sim'], fmt="%s")
			aux = True
			break
print('Finished!')
print("Total--- %s seconds ---" % (time.time() - tempo))
