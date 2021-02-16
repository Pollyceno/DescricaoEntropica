import random
import math
import numpy as np

from desc_entro.marginalizacao import marginalizacao
from desc_entro.desc_entro import cenario_marginal
from rotulo import rotulo
from recurso import *
from bool import distribuicao



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


def verifica_fronteira3(M, pabcDxyz):
	#Declarando vetores
	#E=np.arange(0., 0.5, 0.5/n)
	#G=1 - E	

	Px0x1y0y1MxMyabcxyZ0=np.zeros((2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), dtype='float')

	Px0x1y0y1MxMyabcxyZ1=np.zeros((2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), dtype='float')

	#Probabilidades constantes
	#p(x0,x1,y0,y1)
	px0x1y0y1=(1/16)*np.ones((2,2,2,2), dtype='float')
	#print(px0x1y0y1, px0x1y0y1.sum())

	pz = (1/2)*np.ones((2), dtype='float')#------------PROBABILIDAES-CONDICIONAIS QUE NÃO DEPENDEM DO RECURSO-----------------
	
	p2 = distribuicao(2)

	p3 = distribuicao(3)

	#p(Mx|a,x0)
	pMxDax0=p2

	#p(My|b,y0)
	pMyDby0=p2

	#p(x|x0,x1)
	pxDx0x1=p2

	#p(y|y0,y1)
	pyDy0y1=p2

	#p(Zj0|c,Mx,My)
	pZ0DcMxMy = p3

	#p(Z1|c,Mx,My)
	pZ1DcMxMy = p3

#-----------RECURSO --------------------------------------------------------------------
	'''
	if(e==0):
		pabcDxyz = recurso(3)
	if(e==1):
		pabcDxyz = recurso(4)

	rotulo(pabcDxyz)
	'''
	#pabcDxyz = recurso(4)
	#pabcDxyz = recurso(0)
	#pabcDxyz = recurso(1)
	#pabcDxyz = recurso(2)
	#print(pabcDxyz)
	#print(pabcDxyz.sum())
	#pabcDxyz = (1/8)*np.ones((2,2,2,2,2,2))

	'''
	pm = marginalizacao(pabcDxyz, (3,4,5))

	N = 3
	for k in range(0,(2**N)):
		k = np.binary_repr(k)
		I = np.zeros((N-len(k)), dtype = 'int')
		for l in range(0,len(k)):
			I = np.hstack((I,int(k[l])))
		#print(I)
		x=I[0]
		y=I[1]
		z=I[2]
		print(pm[x][y][z])
	'''
#-----------PROBABILIDADE CONJUNTA---------------------------------------------------------
	
	#print('x0+y0', 'Z0', '&', 'x1+y1', 'Z1')
	N = 12
	for k in range(0,(2**N)):
		k = np.binary_repr(k)
		I = np.zeros((N-len(k)), dtype = 'int')
		for l in range(0,len(k)):
			I = np.hstack((I,int(k[l])))
		#print(I)
		x0=I[0]
		x1=I[1]
		y0=I[2]
		y1=I[3]
		Mx=I[4]
		My=I[5]
		a=I[6]
		b=I[7]
		c=I[8]
		x=I[9]
		y=I[10]
		#z=I[10]
		Z0=I[11]
		Z1=I[11]
		
		#pabcDxyz[ind322(a,b,c,x,y,0)]
		#pabcDxyz[ind322(a,b,c,x,y,1)]
		#Px0x1y0y1MxMyabcxyZ0[x0][x1][y0][y1][Mx][My][a][b][c][x][y][Z0] = px0x1y0y1[x0][x1][y0][y1]*pMxDax0[Mx][a][x0]*pMyDby0[My][b][y0]*pabcDxyz[a][b][c][x][y][0]*pxDx0x1[x][x0][x1]*pyDy0y1[y][y0][y1]*pz[0]*pZ0DcMxMy[Z0][c][Mx][My]/pz[0]
		#Px0x1y0y1MxMyabcxyZ1[x0][x1][y0][y1][Mx][My][a][b][c][x][y][Z1] = px0x1y0y1[x0][x1][y0][y1]*pMxDax0[Mx][a][x0]*pMyDby0[My][b][y0]*pabcDxyz[a][b][c][x][y][1]*pxDx0x1[x][x0][x1]*pyDy0y1[y][y0][y1]*pz[1]*pZ1DcMxMy[Z1][c][Mx][My]/pz[1]
		Px0x1y0y1MxMyabcxyZ0[x0][x1][y0][y1][Mx][My][a][b][c][x][y][Z0] = px0x1y0y1[x0][x1][y0][y1]*pMxDax0[Mx][a][x0]*pMyDby0[My][b][y0]*pabcDxyz[ind322(a,b,c,x,y,0)]*pxDx0x1[x][x0][x1]*pyDy0y1[y][y0][y1]*pz[0]*pZ0DcMxMy[Z0][c][Mx][My]/pz[0]
		Px0x1y0y1MxMyabcxyZ1[x0][x1][y0][y1][Mx][My][a][b][c][x][y][Z1] = px0x1y0y1[x0][x1][y0][y1]*pMxDax0[Mx][a][x0]*pMyDby0[My][b][y0]*pabcDxyz[ind322(a,b,c,x,y,1)]*pxDx0x1[x][x0][x1]*pyDy0y1[y][y0][y1]*pz[1]*pZ1DcMxMy[Z1][c][Mx][My]/pz[1]

		#if(Px0x1y0y1MxMyabcxyZ0[x0][x1][y0][y1][Mx][My][a][b][c][x][y][Z0] != 0 and Px0x1y0y1MxMyabcxyZ1[x0][x1][y0][y1][Mx][My][a][b][c][x][y][Z1] != 0):
			#print((x0+y0)%2, Z0, '&', (x1+y1)%2, Z1)
	
	#----------MARGINALIZANDO-------------------------------------------------------------------
	
	#Maginalizando o que nao faz parte do protocolo	
	Px0x1y0y1MxMyZ0 = marginalizacao(Px0x1y0y1MxMyabcxyZ0, (0,1,2,3,4,5,11))
	Px0x1y0y1MxMyZ1 = marginalizacao(Px0x1y0y1MxMyabcxyZ1, (0,1,2,3,4,5,11))

	#Gerando lista com todas as marginais sem m
	#CM = np.array([[0,1,2,3,6],[0,1,2,3,7]]) #Cenario marginal
	#(M,Ind)=cenario_marginal(CM, 9)

	h = np.array([len(M)+1])# Condicao para primeiro elemento. Por algum motivo e boa 

	for k in M:
		#print(k.count(4))
		if (k.count(7)== 0): #Se tiver g1 usa uma distibuicao, se tiver g0 usa outra
			#print('if',k)
			p = marginalizacao(Px0x1y0y1MxMyZ0, k)
			#print(p)
			if(h[0]==len(M)+1): #Apenas condicao paa ser primeiro
				h[0] = H(p)
				#print(k,H(p))
			else:
				h = np.concatenate((h, np.array([H(p)])))
				#print(k,H(p))
		else:
			#Alterando 7 por 6 para ajustar o indice da distribuicao
			j = list(k)
			j[j.index(7)] = 6
			j = tuple(j)
			#print(j)
			p = marginalizacao(Px0x1y0y1MxMyZ1, j)
			#print(p)
			if(h[0]==len(M)+1):#Apenas condicao paa ser primeiro
				h[0] = H(p)
				#print(k,H(p))	
			else:
				h = np.concatenate((h, np.array([H(p)])))
				#print(k,H(p),p)
	
	

	return h