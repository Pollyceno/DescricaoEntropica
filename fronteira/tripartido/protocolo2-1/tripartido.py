import random
import math
import numpy as np

from marginalizacao import marginalizacao
from bool import distribuicao
from recurso import *


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




def verifica_fronteira3(n, p44, pd,  pw, t=None):
	#Declarando vetores
	E=np.arange(0., (1 + (1/n)), 1/n)
	G=1 - E	

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


	#-----------PARAMETROS BISECCAO----------------------------------------------------------
	iterac = 0
	gammaU = 1 
	gammaB = 0
	gamma = (gammaU - gammaB)/2
	atol=0.01
	bound = 0.0
	#deltaU = 0.01
	#deltaB = 0.15

#-----------VARIANDO PARAMETROS------------------------------------------------------------

	for i in range(0,n+1):
		epsilon=(1/n)*i
		E[i]=epsilon
		max_it = n
		aux = 0
		gammaU = 1-epsilon
		gamma = gammaB
		#print(gamma, gammaU, epsilon)
		while(aux < max_it ):
			iterac = iterac +1

	#-----------RECURSO --------------------------------------------------------------------

			#pabcDxyz = gamma*p44 + (1-gamma)*pw
			pabcDxyz = gamma*p44 + epsilon*pd + (1-gamma-epsilon)*pw
			
		#-----------PROBABILIDADE CONJUNTA---------------------------------------------------------
			
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
		
			
			IX0 = H(marginalizacao(Px0x1y0y1MxMyZ0, (0,))) + H(marginalizacao(Px0x1y0y1MxMyZ0, (1,2,6))) - H(marginalizacao(Px0x1y0y1MxMyZ0, (0,1,2,6)))
	
			IX1 = H(marginalizacao(Px0x1y0y1MxMyZ1, (1,))) + H(marginalizacao(Px0x1y0y1MxMyZ1, (3,4,6))) - H(marginalizacao(Px0x1y0y1MxMyZ1, (1,3,4,6)))
	
			IY0 = H(marginalizacao(Px0x1y0y1MxMyZ0, (2,))) + H(marginalizacao(Px0x1y0y1MxMyZ0, (0,3,6))) - H(marginalizacao(Px0x1y0y1MxMyZ0, (0,2,3,6)))
	
			IY1 = H(marginalizacao(Px0x1y0y1MxMyZ1, (3,))) + H(marginalizacao(Px0x1y0y1MxMyZ1, (1,5,6))) - H(marginalizacao(Px0x1y0y1MxMyZ1, (1,3,5,6)))
	
			HMxMy = H(marginalizacao(Px0x1y0y1MxMyZ1, (4,5)))
	
			Ix0x1 = H(marginalizacao(Px0x1y0y1MxMyZ0, (0,))) + H(marginalizacao(Px0x1y0y1MxMyZ0, (1,))) - H(marginalizacao(Px0x1y0y1MxMyZ0, (0,1)))
	
			Iy0y1 = H(marginalizacao(Px0x1y0y1MxMyZ0, (2,))) + H(marginalizacao(Px0x1y0y1MxMyZ0, (3,))) - H(marginalizacao(Px0x1y0y1MxMyZ0, (2,3)))
	
	#-------------VERIFICANDO DESIGUALDADE-------------------------------------------------------
	
			desig = IX0 + IX1 + IY0 + IY1 - HMxMy + Ix0x1 + Iy0y1
	
			#print(desig)
	
			if(desig>bound):
				print('U',epsilon, gamma, desig)
				gammaU = gamma
				if(abs(desig - bound) > atol):
					gamma = gammaU - (gammaU - gammaB)/2
				else:
					break
			else:
				print('B',epsilon, gamma, desig)
				gammaB = gamma
				if(abs(desig - bound) > atol):
					gamma = gammaB + (gammaU - gammaB)/2
				else:
					break
			aux = aux +1
	
		aux = 0
	
		gammaB = 0.0 #gamma - deltaB
		G[i] = gamma

	print(iterac)
	return (E, G)
		
	
	