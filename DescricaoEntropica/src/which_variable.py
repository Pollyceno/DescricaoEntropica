import numpy as np 

# Given a numpy array (Ind) with all indexes to be eiminated and the inequalities matrix (A) for A*x <= b,  
# return the index that number that appears least (var_index) and the set with the remaining indexes (restante).

def w_variable(Ind, A):

	n_zeros = []
	#Contagem de termos nao nulos
	for i in Ind:
		n_zeros = np.append(n_zeros, np.count_nonzero(A[:,i]))


	np.savetxt("nao_zeros.txt", [['restante: ', Ind],['Nao zeros: ',n_zeros]], fmt="%s")
	
	#Menor valor
	min_value = np.amin(n_zeros)	
	#Indice do mnor valor
	min_index = np.where(n_zeros == min_value)[0]
	min_index = min_index[0]
	
	#Variavel a eliminar
	var_index = Ind[min_index]
	
	#Elimina o indice do menor valor
	restante = np.delete(Ind, min_index)
	
	#Indices do valores que sao meiores qu o indice a eliminar
	greater = np.where(restante > Ind[min_index])[0]
	#Atualiza indices
	for j in greater:
		restante[j] = restante[j] - 1

	return (var_index, restante)
	