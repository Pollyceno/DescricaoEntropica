#import math
import numpy as np
import sys
sys.path.append('..')
np.set_printoptions(threshold=sys.maxsize)

import itertools as itt

#from src.visualize_2D import visualize_2D
from src.main import fourier_motzkin_eliminate_single
#from src.polytope import translate
from src.redundancy_reduction import elimina_redundancia
from desc_entro.desc_entro import desigualdades_basicas, cenario_marginal, cenario_marginal2, restricoes_lineares, monta_matriz

import time


tempo = time.time()
######### DESIGUALDADES BASICAS #######################################
print('Listando desigualdades basicas')
n = 6
A=desigualdades_basicas(n)
b=np.zeros((len(A),1))

######### RESTRICOES LINEARES #########################################
print('Restricoes lineares')
restri=np.array([[[0,1],[5],[]],[[0],[5],[]],[[1],[5],[]],[[0,1],[2,3],[4,5]],[[0],[2,3],[4,5]],[[1],[2,3],[4,5]],[[0,1],[2],[4,5]],[[0,1],[3],[4,5]],[[0],[2],[4,5]],[[0],[3],[4,5]],[[1],[2],[4,5]],[[1],[3],[4,5]],[[4],[0,1,5]],[[2,3],[4,5]],[[2],[4,5]],[[3],[4,5]]]) #restricoes lineares a ser gerada
C=restricoes_lineares(restri,n)
d=np.zeros((len(C),1))

#################################################################################################################################
						# CENARIO MARGINAL PARA ELIMINAR LAMBDA
#################################################################################################################################

print('Cenario marginal LAMBDA')
CM = np.array([[0,1,2,3,4]]) #Cenario marginal
(M, Ind) = cenario_marginal(CM, n)# Indics a eliminar
#print(Ind)

######### ELIMINACAO DE REDUNDANCIAS ##################################
print('Eliminacao de redundancias')
canonico = elimina_redundancia(A,b)
Ac = canonico[0]
bc = canonico[1]

print('Basicas:', len(A), 'Elementares:', len(Ac))
#np.savetxt("desigualdades_elementares_CI.txt", Ac, fmt="%s")
#np.savetxt("dados_relevantes_CI.txt", [['Basicas:',len(A)],['Elementares:', len(Ac)]], fmt="%s")

######## FOURIER MOTZKIN ##############################################
print('Fourier Motzkin para LAMBDA')
cont = 0
restante = Ind # indices que restam a eliminar. Inicialmente ele e igual ao Ind
for var_index in Ind:
	porc = int(cont/len(Ind)*100)
	print('Porcentagem:', porc, '%')
	cont = cont + 1
	np.savetxt("tempAiL.txt", Ac, fmt="%s")
	np.savetxt("tempBiL.txt", bc, fmt="%s")
	restante = np.delete(restante, np.where(restante == var_index)) # Indices restante a eliminar
	if(var_index != Ind[0]):
		(A_new,b_new,data)=fourier_motzkin_eliminate_single(var_index,Ac,bc,atol=10**-8)
		np.savetxt("dados_relevantes_L.txt", [['Eliminando lambda'],['Porcentagem:', porc, '%'],['Input FM:',len(Ac)],['Numero de verificacoes:', data[1]],['Output FM:', data[0]], ['Elementares:', len(A_new)],['Indices restantes:', restante]], fmt="%s")
		Ac=A_new
		bc=b_new
	else:
		(A_new,b_new,data)=fourier_motzkin_eliminate_single(var_index,Ac,bc,C,d,atol=10**-8)
		np.savetxt("dados_relevantes_L.txt", [['Eliminando lambda'],['Porcentagem:', porc, '%'],['Input FM:',len(Ac)],['Numero de verificacoes:', data[1]],['Output FM:', data[0]], ['Elementares:', len(A_new)],['Indices restantes:', restante]], fmt="%s")
		Ac=A_new
		bc=b_new
	#print(len(Ac))

#np.savetxt("desigualdades_SEM_LAMBDA.txt", Ac, fmt="%s")
#np.savetxt("valores_b__SEM_LAMBDA.txt", bc, fmt="%s")

#################################################################################################################################
						# CENARIO MARGINAL IC
#################################################################################################################################

print('Cenario marginal IC')
CM = np.array([[0,1,2,4],[0,1,3,4]]) #Cenario marginal
(M, Ind) = cenario_marginal2(M, CM, n)# Indics a eliminar
#print(Ind)

######### ELIMINACAO DE REDUNDANCIAS ##################################
print('Eliminacao de redundancias')
canonico = elimina_redundancia(Ac,bc)
Ac = canonico[0]
bc = canonico[1]

#print('Basicas:', len(A), 'Elementares:', len(Ac))
#np.savetxt("desigualdades_elementares_CI.txt", Ac, fmt="%s")
#np.savetxt("dados_relevantes_CI.txt", [['Basicas:',len(A)],['Elementares:', len(Ac)]], fmt="%s")

######## FOURIER MOTZKIN ##############################################
print('Fourier Motzkin IC')
cont = 0
restante = Ind # indices que restam a eliminar. Inicialmente ele e igual ao Ind
for var_index in Ind:
	porc = int(cont/len(Ind)*100)
	print('Porcentagem:', porc, '%')
	cont = cont + 1
	np.savetxt("tempAiCI.txt", Ac, fmt="%s")
	np.savetxt("tempBiCI.txt", bc, fmt="%s")
	restante = np.delete(restante, np.where(restante == var_index)) # Indices restante a eliminar

	(A_new,b_new,data)=fourier_motzkin_eliminate_single(var_index,Ac,bc,atol=10**-8)
	np.savetxt("dados_relevantes_CI.txt", [['Eliminando outros'],['Porcentagem:', porc, '%'],['Input FM:',len(Ac)],['Numero de verificacoes:', data[1]],['Output FM:', data[0]], ['Elementares:', len(A_new)],['Indices restantes:', restante]], fmt="%s")
	Ac=A_new
	bc=b_new

#################################################################################################################################
						#CENARIO MARGINAL IC ANTIGO 
#################################################################################################################################
print('Cenario marginal IC antigo')
CM = np.array([[0,2],[1,3],[4],[0,1]]) #Cenario marginal
(M, Ind) = cenario_marginal2(M, CM, n)# Indics a eliminar
#print(Ind)

######### ELIMINACAO DE REDUNDANCIAS ##################################
print('Eliminacao de redundancias')
canonico = elimina_redundancia(Ac,bc)
Ac = canonico[0]
bc = canonico[1]

#print('Basicas:', len(A), 'Elementares:', len(Ac))
#np.savetxt("desigualdades_elementares_CI.txt", Ac, fmt="%s")
#np.savetxt("dados_relevantes_CI.txt", [['Basicas:',len(A)],['Elementares:', len(Ac)]], fmt="%s")

######## FOURIER MOTZKIN ##############################################
print('Fourier Motzkin IC')
cont = 0
restante = Ind # indices que restam a eliminar. Inicialmente ele e igual ao Ind
for var_index in Ind:
	porc = int(cont/len(Ind)*100)
	print('Porcentagem:', porc, '%')
	cont = cont + 1
	np.savetxt("tempAiCI.txt", Ac, fmt="%s")
	np.savetxt("tempBiCI.txt", bc, fmt="%s")
	restante = np.delete(restante, np.where(restante == var_index)) # Indices restante a eliminar

	(A_new,b_new,data)=fourier_motzkin_eliminate_single(var_index,Ac,bc,atol=10**-8)
	np.savetxt("dados_relevantes_CI_antigo.txt", [['Eliminando outros'],['Porcentagem:', porc, '%'],['Input FM:',len(Ac)],['Numero de verificacoes:', data[1]],['Output FM:', data[0]], ['Elementares:', len(A_new)],['Indices restantes:', restante]], fmt="%s")
	Ac=A_new
	bc=b_new
	#print(len(Ac))

np.savetxt("desig_CI_antigo.txt", Ac, fmt="%s")
np.savetxt("b_CI_antigo.txt", bc, fmt="%s")
print('Finished!')
print("Total--- %s seconds ---" % (time.time() - tempo))
