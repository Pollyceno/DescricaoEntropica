import random
import math
import numpy as np
from desc_entro.marginalizacao import marginalizacao
from desc_entro.desc_entro import cenario_marginal



#------------FUNÇÃO QUE CALCULA A ENTROPIA------------------------------------------
def H(prob):
	S=np.size(prob)# Numero de elementos
	Pro=np.reshape(prob, S) #concatenando todos os elementos num vetor
	h=np.zeros(S, dtype='float')
	for i in range(0,S): #Calcuando entropia para as probabilidades não nulas
		if Pro[i]!=0:
			h[i]=-Pro[i]*math.log(Pro[i],2)
	Ent=h.sum() # Entropia de Shannon
	return Ent

def IM(p1, p2, p3, p4=None):
	if(np.size(p4)==1): #sem condicional
		I = H(p1)+H(p2)-H(p3)
	else: # com condiconal
		I = H(p1)+H(p2)-H(p3)-H(p4)

	return I

def distribuicao(N):

	if(N==2):
		p = np.zeros((2,2,2), dtype='float')
		for k in range(0,(2**3)):
			k = np.binary_repr(k)
			I = np.zeros((3-len(k)), dtype = 'int')
			for l in range(0,len(k)):
				I = np.hstack((I,int(k[l])))
			a = I[0]
			b = I[1]
			c = I[2]

			if((b+c)%2 == a):
				p[a][b][c] = 1
			else:
				p[a][b][c] = 0

		return p
	if(N==3):
		p = np.zeros((2,2,2,2), dtype='float')
		for k in range(0,(2**4)):
			k = np.binary_repr(k)
			I = np.zeros((4-len(k)), dtype = 'int')
			for l in range(0,len(k)):
				I = np.hstack((I,int(k[l])))
			a = I[0]
			b = I[1]
			c = I[2]
			d = I[3]

			if((b+c+d)%2 == a):
				p[a][b][c][d] = 1
			else:
				p[a][b][c][d] = 0

		return p
	if(N==4):
		p = np.zeros((2,2,2,2,2), dtype='float')
		for k in range(0,(2**5)):
			k = np.binary_repr(k)
			I = np.zeros((5-len(k)), dtype = 'int')
			for l in range(0,len(k)):
				I = np.hstack((I,int(k[l])))
			a = I[0]
			b = I[1]
			c = I[2]
			d = I[3]
			e = I[4]

			if((b+c+d+e)%2 == a):
				p[a][b][c][d][e] = 1
			else:
				p[a][b][c][d][e] = 0
		return p

def recurso(N):

	if(N==0):
		p = np.zeros((2,2,2,2), dtype='float')
		N = 4
		for k in range(0,(2**N)):
			k = np.binary_repr(k)
			I = np.zeros((N-len(k)), dtype = 'int')
			for l in range(0,len(k)):
				I = np.hstack((I,int(k[l])))
			a = I[0]
			b = I[1]
			x = I[2]
			y = I[3]

			if(a==0 and b ==0):
				p[a][b][x][y] = 1
			else:
				p[a][b][x][y] = 0

		return p


	if(N==1):
		p = np.zeros((2,2,2,2), dtype='float')
		N = 4
		for k in range(0,(2**N)):
			k = np.binary_repr(k)
			I = np.zeros((N-len(k)), dtype = 'int')
			for l in range(0,len(k)):
				I = np.hstack((I,int(k[l])))
			a = I[0]
			b = I[1]
			x = I[2]
			y = I[3]

			if((a+b)%2 == x*y):
				p[a][b][x][y] = 1/2
			else:
				p[a][b][x][y] = 0

		return p

	if(N==2):
		p = np.zeros((2,2,2,2), dtype='float')
		N = 4
		for k in range(0,(2**N)):
			k = np.binary_repr(k)
			I = np.zeros((N-len(k)), dtype = 'int')
			for l in range(0,len(k)):
				I = np.hstack((I,int(k[l])))
			a = I[0]
			b = I[1]
			x = I[2]
			y = I[3]

			if((a+b)%2 == (x*y+x+y)%2):
				p[a][b][x][y] = 1/2
			else:
				p[a][b][x][y] = 0

		return p

	if(N==3):
		p = np.zeros((2,2,2,2,2,2), dtype='float')
		N = 6
		for k in range(0,(2**N)):
			k = np.binary_repr(k)
			I = np.zeros((N-len(k)), dtype = 'int')
			for l in range(0,len(k)):
				I = np.hstack((I,int(k[l])))
			a = I[0]
			b = I[1]
			c = I[2]
			x = I[3]
			y = I[4]
			z = I[5]

			if((a+b+c)%2 == ((x*z)+(y*z))%2):
				p[a][b][c][x][y][z] = 1/4
			else:
				p[a][b][c][x][y][z] = 0

		return p

def verifica_fronteira2(M, pabDxy):
	#Declarando vetores
	Pz0z1abxmg0=np.zeros((2, 2, 2, 2, 2, 2, 2), dtype='float')

	Pz0z1abxmg1=np.zeros((2, 2, 2, 2, 2, 2, 2), dtype='float')

	#Probabilidades constantes
	pz0=np.array([0.5,0.5])
	pz1=np.array([0.5,0.5])
	pz0z1=np.outer(pz0,pz1)
	py=np.array([0.5,0.5])

	#------------PROBABILIDAES-CONDICIONAIS QUE NÃO DEPENDEM DO RECURSO-----------------
	
	p2= distribuicao(2)

	#p(x|z0,z1)
	pxDz0z1=p2
	
	#p(m|z0,a)
	pmDz0a=p2
	
	#p(g0|b,m)
	pg0Dbm=p2

	#p(g1|b,m)
	pg1Dbm=p2


#-----------RECURSO --------------------------------------------------------------------

	#pabDxy = recurso(1)
	#pabDxy = (1/4)*np.ones((2,2,2,2))
	#print(np.flip(np.flip(pabDxy, 0), 3))
	'''
	pm = marginalizacao(pabDxy, (2,3))

	N = 2
	for k in range(0,(2**N)):
		k = np.binary_repr(k)
		I = np.zeros((N-len(k)), dtype = 'int')
		for l in range(0,len(k)):
			I = np.hstack((I,int(k[l])))
		#print(I)
		x=I[0]
		y=I[1]
		print(pm[x][y])
	'''
#-----------PROBABILIDADE CONJUNTA---------------------------------------------------------
	
	N = 7
	for k in range(0,(2**N)):
		k = np.binary_repr(k)
		I = np.zeros((N-len(k)), dtype = 'int')
		for l in range(0,len(k)):
			I = np.hstack((I,int(k[l])))
		#print(I)

		z0=I[0]
		z1=I[1]
		a=I[2]
		b=I[3]
		x=I[4]
		m=I[5]
		g0=I[6]
		g1=I[6]
		
		Pz0z1abxmg0[z0][z1][a][b][x][m][g0] = pz0[z0]*pz1[z1]*pxDz0z1[x][z0][z1]*pmDz0a[m][z0][a]*pabDxy[a][b][x][0]*pg0Dbm[g0][b][m]
		Pz0z1abxmg1[z0][z1][a][b][x][m][g1] = pz0[z0]*pz1[z1]*pxDz0z1[x][z0][z1]*pmDz0a[m][z0][a]*pabDxy[a][b][x][1]*pg1Dbm[g1][b][m]

	#print(marginalizacao(Pz0z1mabxg0, (2)),H(marginalizacao(Pz0z1mabxg0, (2))))
	#print(marginalizacao(Pz0z1mabxg1, (2)),H(marginalizacao(Pz0z1mabxg0, (2))))	
	#----------MARGINALIZANDO-------------------------------------------------------------------
	
	#Maginalizando o que nao faz parte do protocolo	
	Pz0z1mg0 = marginalizacao(Pz0z1abxmg0, (0,1,5,6))
	Pz0z1mg1 = marginalizacao(Pz0z1abxmg1, (0,1,5,6))

	#Gerando lista com todas as marginais sem m
	#CM = np.array([[0,1,2],[0,1,3]]) #Cenario marginal
	#(M,Ind)=cenario_marginal(CM, 6)

	h = np.array([len(M)+1])# Condicao para primeiro elemento. Por algum motivo e boa 

	for k in M:
		#print(k.count(4))
		if (k.count(4)== 0): #Se tiver g1 usa uma distibuicao, se tiver g0 usa outra
			#print('if',k)
			p = marginalizacao(Pz0z1mg0, k)
			#print(p)
			if(h[0]==len(M)+1): #Apenas condicao paa ser primeiro
				h[0] = H(p)
				#print(k,H(p))
			else:
				h = np.concatenate((h, np.array([H(p)])))
				#print(k,H(p))
		else:
			#Alterando 3 por 2 para ajustar o indice da distribuicao
			j = list(k)
			j[j.index(4)] = 3
			j = tuple(j)
			#print(j)
			p = marginalizacao(Pz0z1mg1, j)
			#print(p)
			if(h[0]==len(M)+1):#Apenas condicao paa ser primeiro
				h[0] = H(p)
				#print(k,H(p))	
			else:
				h = np.concatenate((h, np.array([H(p)])))
				#print(k,H(p),p)

	#desig = (-h[M.index((2,))]+h[M.index((0,1))]+h[M.index((2,3))]-h[M.index((0,2,3))]+h[M.index((0,2,4))]-h[M.index((0,1,2,4))])
	desig = (-h[M.index((2,))]+h[M.index((3,))]+h[M.index((0,1))]-h[M.index((0,3))]+h[M.index((0,4))]-h[M.index((0,1,4))])
	print(desig)

	return h, M
