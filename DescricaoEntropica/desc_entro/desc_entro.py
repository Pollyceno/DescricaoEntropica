import numpy as np
import sys
sys.path.append('..')
np.set_printoptions(threshold=sys.maxsize)
import gurobipy as gp
import itertools as itt
from src.main import fourier_motzkin_eliminate_single


def desigualdades_basicas(n, M = None):


	if(M == None):
		#n  e o Numero de variAveis aleatorias
		x=np.arange(n) # Array com os indices de variaveis aleatorias

		############ GERANDO COMBINACOES ####################################################################################

		comb=[list(itt.combinations(x,i)) for i in range (1,n+1)] #lista de listas para as possiveis combinacoes

		vetor_H = list(itt.chain(*comb)) # Vetor entropico
		#print(vetor_H)
	else:
		vetor_H = M
		#print(vetor_H)

	matriz_desig = np.zeros((1,len(vetor_H)), dtype='int') # Matriz de desigualdades basicas com linhas a serem incrementadas pela newrow conforme necessidade
	newrow=np.zeros(len(vetor_H), dtype='int') # array usado para incrementar matriz_desig
	linha=0

	#####################################################################################################################
	############ GERANDO H(A|B) #########################################################################################
	'''
	e utilizada a lista de combinacoes de modo que H(comb[i][k]|comb[j][l]). Quando comb[i][k]| e diferente de comb[j][l] 
	são alterados os elementos de matriz de matriz_desig, correspondente as componentes de vetor entropico que azem parte de 
	H(comb[i][k]|comb[j][l]) = H(comb[i][k],comb[j][l]) - H(comb[j][l]).
	'''
	
	for k in x: # k e o elemento da lista correspondente a variavel A
		elemento = tuple(np.sort(x)) #Ordenando crescentemente e transformando em tuple
		condicao = np.delete(x, (np.where(x==k)[0][0])) # Gerando termo condicao
		condicao = tuple(np.sort(condicao)) #Ordenando crescentemente e transformando em tuple

		coluna = vetor_H.index(elemento) #Encontrando indice da componente dentro do vetor entropico
		matriz_desig[linha][coluna] = -1 # Atribuindo coeficiente a matriz 
		coluna = vetor_H.index(condicao) #Encontrando indice da componente dentro do vetor entropico
		matriz_desig[linha][coluna] = 1 # Atribuindo coeficiente a matriz

		#Apos as alteracoes realizadas ao encontrar a desigualdade, deve-se criar mais uma linha a matriz para a proxima dessigualdade que sera encontrada
		matriz_desig = np.vstack([matriz_desig, newrow])
		linha=linha+1 # Indice da linha em que a prxima desigualdade sera salva
	
	#####################################################################################################################
	############ GERANDO I(A:B|C) #########################################################################################
	
	for k in x: # k e o elemento da lista correspondente a variavel A
		#print((np.where(x<=k)[0]))
		elim = np.delete(x, (np.where(x<=k)[0])) # Eliminando k e seus antececores
		#print(elim)
		#elemento = tuple(np.sort(x)) #Ordenando crescentemente e transformando em tuple. Termo H(A,B,C)
		for l in elim: # l e o elemento da lista correspondente a variavel B
		#------------------I(A:B|C)---------------------------------------------------------------------------------

			condicao = np.delete(x, (np.where(x==k)[0][0])) # Eliminando k
			condicao = np.delete(condicao, (np.where(condicao==l)[0][0])) # Eliminando k

			#print(np.size(condicao))
			if(np.size(condicao)!=0): #Para contornar casos n=2 que nao tem temo condicional
				
				condicao=[list(itt.combinations(condicao,i)) for i in range (1,len(condicao)+1)] #lista de listas para as possiveis combinacoes
				condicao = list(itt.chain(*condicao)) # transformando numa lista

				#print(np.concatenate(condicao,condicao).astype(int))
				for c in condicao: # c varre todas as condicionais que entram nas informacoes mutuas				
					
					kc = np.concatenate(((k,),c)).astype(int)# Gerando elemento H(k,c)
					kc = tuple(np.sort(kc))
					coluna = vetor_H.index(kc) #Encontrando indice da componente dentro do vetor entropico H(A,C)
					matriz_desig[linha][coluna] = -1 # Atribuindo coeficiente a matriz
					
					lc = np.concatenate(((l,),c)).astype(int)# Gerando elemento H(l,c)
					lc = tuple(np.sort(lc))
					coluna = vetor_H.index(lc) #Encontrando indice da componente dentro do vetor entropico H(B,C)
					matriz_desig[linha][coluna] = -1 # Atribuindo coeficiente a matriz
					
					elemento = np.concatenate(((k,),(l,),c)).astype(int)# Gerando elemento H(k,l,c)
					elemento = tuple(np.sort(elemento))
					coluna = vetor_H.index(elemento) #Encontrando indice da componente dentro do vetor entropico H(A,B,C)
					matriz_desig[linha][coluna] = 1 # Atribuindo coeficiente a matriz 
	
					coluna = vetor_H.index(c) #Encontrando indice da componente dentro do vetor entropico H(C)
					matriz_desig[linha][coluna] = 1 # Atribuindo coeficiente a matriz 
	
					#Apos as alteracoes realizadas ao encontrar a desigualdade, deve-se criar mais uma linha a matriz para a proxima dessigualdade que sera encontrada
					matriz_desig = np.vstack([matriz_desig, newrow])
					linha=linha+1 # Indice da linha em que a prxima desigualdade sera salva

		#------------------I(A:B)---------------------------------------------------------------------------------
			coluna = vetor_H.index(k) #Encontrando indice da componente dentro do vetor entropico
			matriz_desig[linha][coluna] = -1 # Atribuindo coeficiente a matriz

			coluna = vetor_H.index(l) #Encontrando indice da componente dentro do vetor entropico
			matriz_desig[linha][coluna] = -1 # Atribuindo coeficiente a matriz

			elemento = np.concatenate(((k,),(l,))).astype(int)# Gerando elemento H(k,l,c)
			elemento = tuple(np.sort(elemento))
			coluna = vetor_H.index(elemento) #Encontrando indice da componente dentro do vetor entropico
			matriz_desig[linha][coluna] = 1 # Atribuindo coeficiente a matriz 

			#Apos as alteracoes realizadas ao encontrar a desigualdade, deve-se criar mais uma linha a matriz para a proxima dessigualdade que sera encontrada
			matriz_desig = np.vstack([matriz_desig, newrow])
			linha=linha+1 # Indice da linha em que a prxima desigualdade sera salva
	

	matriz_desig = np.delete(matriz_desig, (len(matriz_desig)-1), axis = 0) #eliminando ultima linha que nao tem nada
	matriz_desig = np.unique(matriz_desig, axis = 0) # Removento desigualdades iguais
	#print(matriz_desig)
	return(matriz_desig, vetor_H)
	
def restricoes_lineares(I, n):
	x=np.arange(n) # Array com os indices de variaveis aleatorias
	############ GERANDO COMBINACOES ####################################################################################
	comb=[list(itt.combinations(x,i)) for i in range (1,n+1)] #lista de listas para as possiveis combinacoes
	vetor_H = list(itt.chain(*comb)) # Vetor entropico

	matriz_restricao = np.zeros((1,len(vetor_H)), dtype='int') # Matriz de restricoes lineares com linhas a serem incrementadas pela newrow conforme necessidade
	newrow=np.zeros(len(vetor_H), dtype='int') # array usado para incrementar matriz_desig
	linha=0
	for i in I:
		if(len(i)==3): #Testa se é restrição para informação mutua
			elemento = np.concatenate((i[0],i[2])).astype(int) #Gerando a componente do vetor entrópico respectivo a H(A,C)
			elemento = tuple(np.sort(elemento)) #Ordenando crescentemente e transformando em tuple
			coluna = vetor_H.index(elemento) #Encontrando indice da componente dentro do vetor entropico
			matriz_restricao[linha][coluna] = 1 # Atribuindo coeficiente a matriz 

			elemento = np.concatenate((i[1],i[2])).astype(int) #Gerando a componente do vetor entrópico respectivo a H(B,C)
			elemento = tuple(np.sort(elemento)) #Ordenando crescentemente e transformando em tuple
			coluna = vetor_H.index(elemento) #Encontrando indice da componente dentro do vetor entropico
			matriz_restricao[linha][coluna] = 1 # Atribuindo coeficiente a matriz 

			elemento = np.concatenate((i[0],i[1],i[2])).astype(int) #Gerando a componente do vetor entrópico respectivo a H(A,B,C)
			elemento = tuple(np.sort(elemento)) #Ordenando crescentemente e transformando em tuple
			coluna = vetor_H.index(elemento) #Encontrando indice da componente dentro do vetor entropico
			matriz_restricao[linha][coluna] = - 1 # Atribuindo coeficiente a matriz

			if(len(i[2]) > 0): #Testa se existe o termo condicional C
				elemento = tuple(np.sort(i[2])) #Ordenando crescentemente e transformando em tuple a componente H(C)
				coluna = vetor_H.index(elemento) #Encontrando indice da componente dentro do vetor entropico
				matriz_restricao[linha][coluna] = - 1 # Atribuindo coeficiente a matriz 

			#Apos as alteracoes realizadas ao encontrar a desigualdade, deve-se criar mais uma linha a matriz para a proxima desigualdade que sera encontrada
			if(linha+1 != len(I)):
				matriz_restricao = np.vstack([matriz_restricao, newrow])
			linha=linha+1 # Indice da linha em que a prxima desigualdade sera salva

		if(len(i)==2): #Testa se é restrição para entropia condicional
			elemento = np.concatenate((i[0],i[1])).astype(int) #Gerando a componente do vetor entrópico respectivo a H(A,B)
			elemento = tuple(np.sort(elemento)) #Ordenando crescentemente e transformando em tuple
			coluna = vetor_H.index(elemento) #Encontrando indice da componente dentro do vetor entropico
			matriz_restricao[linha][coluna] = 1 # Atribuindo coeficiente a matriz 

			elemento = tuple(np.sort(i[1])) #Ordenando crescentemente e transformando em tuple
			coluna = vetor_H.index(elemento) #Encontrando indice da componente dentro do vetor entropico
			matriz_restricao[linha][coluna] = -1 # Atribuindo coeficiente a matriz 

			#Apos as alteracoes realizadas ao encontrar a desigualdade, deve-se criar mais uma linha a matriz para a proxima desigualdade que sera encontrada
			if(linha+1 != len(I)):
				matriz_restricao = np.vstack([matriz_restricao, newrow])
			linha=linha+1 # Indice da linha em que a prxima desigualdade sera salva
	return  matriz_restricao

def cenario_marginal(CM, n):

	x=np.arange(n) # Array com os indices de variaveis aleatorias
	############ GERANDO COMBINACOES ####################################################################################
	comb=[list(itt.combinations(x,i)) for i in range (1,n+1)] #lista de listas para as possiveis combinacoes
	vetor_H = list(itt.chain(*comb)) # Vetor entropico
	#print(vetor_H)

	M = []
	Ind = np.array([len(vetor_H)+1])

	for i in CM:
		comb = [list(itt.combinations(i,j)) for j in range (1,len(i)+1)] #Lista de combinações para cada subconjunto 
		m = list(itt.chain(*comb))
		M = list(set(itt.chain(M, m)))
	#print(M)
	for i in vetor_H:
		if(M.count(i)==0):
			if(Ind[0]==len(vetor_H)+1):
				Ind[0]=vetor_H.index(i)
			else:
				Ind = np.concatenate((Ind,np.array([vetor_H.index(i)])))

	Ind_ordenado = np.sort(Ind)[::-1].astype(int) # ordenando de forma decrescent e transformando em inteiro
	
	M = vetor_H
	for i in Ind_ordenado:
		#M = np.delete(M, (i), axis = 0)
		del M[i]
	#print(len(M))

	return M, Ind_ordenado # ordenando de forma decrescent e transformando em inteiro

# Função de gera o cenário marginal de um cenário que já é marginal com relação a um vetor etrópico. É utilizado uando é feita uma eliminação e precisa-se realizar outra
def cenario_marginal2(vetor_M,CM, n):

	M = []
	Ind = np.array([len(vetor_M)+1])

	for i in CM:
		comb = [list(itt.combinations(i,j)) for j in range (1,len(i)+1)] #Lista de combinações para cada subconjunto 
		m = list(itt.chain(*comb))
		M = list(set(itt.chain(M, m)))
	#print(M)
	for i in vetor_M:
		if(M.count(i)==0):
			if(Ind[0]==len(vetor_M)+1):
				Ind[0]=vetor_M.index(i)
			else:
				Ind = np.concatenate((Ind,np.array([vetor_M.index(i)])))

	Ind_ordenado = np.sort(Ind)[::-1].astype(int) # ordenando de forma decrescent e transformando em inteiro
	
	M = vetor_M
	for i in Ind_ordenado:
		#M = np.delete(M, (i), axis = 0)
		del M[i]

	#print(M)

	return M, Ind_ordenado # ordenando de forma decrescent e transformando em inteiro
