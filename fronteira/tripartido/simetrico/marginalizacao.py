import random
import math
import numpy as np
import itertools as itt


def marg(P, marg):
	n =P.ndim
	x=np.arange(n)
	
	elim = np.delete(x, marg)
	elim = np.sort(elim)[::-1].astype(int)
	#print(elim)
	
	for i in elim:
		P = P.sum(axis=i,dtype='float')
	
	return P

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