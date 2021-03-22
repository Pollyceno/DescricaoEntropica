from desc_entro.desc_entro import *

def traduz(A, x, Ind=None, Ind_e=None):

	#####################################################################
	####### GERANDO VETOR ENTROPICO COM LETRAS ##########################

	#x=['Z0','Z1','G0','G1','M','L']
	#x=['Z0','Z1','M', 'L','G0','G1']
	n=len(x)
	comb=[list(itt.combinations(x,i)) for i in range (1,n+1)]
	comb = list(itt.chain(*comb))

	if(type(Ind) == type(np.array([1]))):
		for i in Ind:
			del comb[i]

	'''
	for i in Ind_e:
		del comb[i]
	'''
	#######################################################################
	####### TRADUZINDO DESIGUALDADES ######################################
	H=[[]]
	h=[]
	
	for a in range(0,len(A)):
		H[a] = [(A[a][i],comb[i]) for i in range(0,len(comb)) if A[a][i]!= 0.0]
		H.append(h)

	return H


