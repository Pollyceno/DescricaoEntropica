#import math
import numpy as np
#import itertools as itt
from marginalizacao import *
from funcoes import *
from recurso import *


def verifica_fronteiraS(n, pabcDxyz):
	#Declarando vetores
	P = np.zeros((2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), dtype='float')

	Px0x1m0g0=np.zeros((2, 2, 2, 2), dtype='float')
	Px0x1m0g1=np.zeros((2, 2, 2, 2), dtype='float')
	Py0y1m1h0=np.zeros((2, 2, 2, 2), dtype='float')
	Py0y1m1h1=np.zeros((2, 2, 2, 2), dtype='float')
	Pz0z1m2j0=np.zeros((2, 2, 2, 2), dtype='float')
	Pz0z1m2j1=np.zeros((2, 2, 2, 2), dtype='float')

	E=np.arange(0., 1.0, 1.0/n)
	G=1 - E


	#Probabilidades constantes p(x1) = 0.5
	p05=np.array([0.5,0.5])

	#------------PROBABILIDAES-CONDICIONAIS QUE NÃO DEPENDEM DO RECURSO-----------------
	
	#p(f|x1,x2) quando f = x1+x2
	pf= distribuicao(2)


	#-----------PARAMETROS BISECCAO----------------------------------------------------------
	iterac = 0
	gammaU = 1 
	gammaB = 0
	gamma = (gammaU - gammaB)/2
	atol = 10**-8
	bound = 0.0
	#deltaU = 0.01
	#deltaB = 0.15
#-----------VARIANDO PARAMETROS------------------------------------------------------------

	for i in range(0,n):
		epsilon=(1/n)*i
		#epsilon = 0
		E[i]=epsilon
		max_it = n
		aux = 0
		gammaU = 1-epsilon
		gamma = gammaB
		#gamma = 1
		#print(gamma, epsilon)
		while(aux < max_it ):
			iterac = iterac +1


#-----------RECURSO --------------------------------------------------------------------
		
			#pr000 = recurso(2)
			#pw = (0.25)*np.array([[[[1,1],[1,1]],[[1,1],[1,1]]],[[[1,1],[1,1]],[[1,1],[1,1]]]])
			#pd = np.array([[[[1,1],[1,1]],[[0,0],[0,0]]],[[[0,0],[0,0]],[[0,0],[0,0]]]])

			#pabDxy = gamma*pr000 +epsilon*pd + (1-gamma-epsilon)*pw
			#print(pabDxy)
			#pabcDxyz = recurso(4)

			
		#-----------PROBABILIDADE CONJUNTA---------------------------------------------------------
			
			N = 18
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
				z0=I[4]
				z1=I[5]
				m0=I[6]
				m1=I[7]
				m2=I[8]
				a=I[9]
				b=I[10]
				c=I[11]
				x=I[12]
				y=I[13]
				z=I[14]
				g=I[15]
				h=I[16]
				j=I[17]


				P[x0][x1][y0][y1][z0][z1][m0][m1][m2][a][b][c][x][y][z][g][h][j]= p05[x0]*p05[x1]*p05[y0]*p05[y1]*p05[z0]*p05[z1]*pf[x][x0][x1]*pf[y][y0][y1]*pf[z][z0][z1]*pf[m0][x0][a]*pf[m1][y0][b]*pf[m2][z0][c]*pabcDxyz[ind322(a,b,c,x,y,z)]*pf[g][b][m0]*pf[h][c][m1]*pf[j][a][m2]
				
			#print(P.sum())

			Px0x1m0yg = marg(P, (0,1,6,13,15))
			Py0y1m1zh = marg(P, (2,3,7,14,16))
			Pz0z1m2xj = marg(P, (4,5,8,12,17))
			
			Px0x1m0 = marg(P, (0,1,6))
			Py0y1m1 = marg(P, (2,3,7))
			Pz0z1m2 = marg(P, (4,5,8))

			#print(marg(P, (0,13,15)))


			N = 4
			for k in range(0,(2**N)):
				k = np.binary_repr(k)
				I = np.zeros((N-len(k)), dtype = 'int')
				for l in range(0,len(k)):
					I = np.hstack((I,int(k[l])))
				#print(I)
		
				x0=I[0]
				x1=I[1]
				x2=I[2]
				x3=I[3]

				Px0x1m0g0[x0][x1][x2][x3] = Px0x1m0yg[x0][x1][x2][0][x3]/p05[0]
				Px0x1m0g1[x0][x1][x2][x3] = Px0x1m0yg[x0][x1][x2][1][x3]/p05[1]

				Py0y1m1h0[x0][x1][x2][x3] = Py0y1m1zh[x0][x1][x2][0][x3]/p05[0]
				Py0y1m1h1[x0][x1][x2][x3] = Py0y1m1zh[x0][x1][x2][1][x3]/p05[1]

				Pz0z1m2j0[x0][x1][x2][x3] = Pz0z1m2xj[x0][x1][x2][0][x3]/p05[0]
				Pz0z1m2j1[x0][x1][x2][x3] = Pz0z1m2xj[x0][x1][x2][1][x3]/p05[1]


			#print(Px0x1m0g0.sum())
			#print(Px0x1m0g1.sum())
			#print(Py0y1m1h0.sum())
			#print(Py0y1m1h1.sum())
			#print(Pz0z1m2j0.sum())
			#print(Pz0z1m2j1.sum())

			#print(marg(Px0x1m0g0, (0,3)))
			#print(marg(Px0x1m0g1, (0,3)))
			#print(marg(Py0y1m1h0, (0,3)))
			#print(marg(Py0y1m1h1, (0,3)))
			#print(marg(Pz0z1m2j0, (0,3)))
			#print(marg(Pz0z1m2j1, (0,3)))
			
			I1 = - H(marg(Px0x1m0, (2,))) + H(marg(Px0x1m0, (0,1))) + H(marg(Px0x1m0g0, (2,3))) - H(marg(Px0x1m0g0, (0,2,3))) + H(marg(Px0x1m0g1, (0,2,3))) - H(Px0x1m0g1)
			#print('I1: ',I1)
			I2 = - H(marg(Py0y1m1, (2,))) + H(marg(Py0y1m1, (0,1))) + H(marg(Py0y1m1h0, (2,3))) - H(marg(Py0y1m1h0, (0,2,3))) + H(marg(Py0y1m1h1, (0,2,3))) - H(Py0y1m1h1)
			#print('I2: ',I2)
			I3 = - H(marg(Pz0z1m2, (2,))) + H(marg(Pz0z1m2, (0,1))) + H(marg(Pz0z1m2j0, (2,3))) - H(marg(Pz0z1m2j0, (0,2,3))) + H(marg(Pz0z1m2j1, (0,2,3))) - H(Pz0z1m2j1)
			#print('I3: ',I3)
			
			Ix0m0g0 = H(marg(Px0x1m0, (0,)))+H(marg(Px0x1m0g0, (2,3))) - H(marg(Px0x1m0g0, (0,2,3)))
			#print('Ix0m0g0 ',H(marg(Px0x1m0, (0,)))+H(marg(Px0x1m0g0, (2,3))) - H(marg(Px0x1m0g0, (0,2,3))))
			Ix1m0g1 = H(marg(Px0x1m0, (1,)))+H(marg(Px0x1m0g1, (2,3))) - H(marg(Px0x1m0g1, (1,2,3)))
			#print('Ix1m0g1 ',H(marg(Px0x1m0, (1,)))+H(marg(Px0x1m0g1, (2,3))) - H(marg(Px0x1m0g1, (1,2,3))))

			Iy0m1h0 = H(marg(Py0y1m1, (0,)))+H(marg(Py0y1m1h0, (2,3))) - H(marg(Py0y1m1h0, (0,2,3)))
			#print('Iy0m1h0 ',H(marg(Py0y1m1, (0,)))+H(marg(Py0y1m1h0, (2,3))) - H(marg(Py0y1m1h0, (0,2,3))))
			Iy1m1h1 = H(marg(Py0y1m1, (1,)))+H(marg(Py0y1m1h1, (2,3))) - H(marg(Py0y1m1h1, (1,2,3)))
			#print('Iy1m1h1 ',H(marg(Py0y1m1, (1,)))+H(marg(Py0y1m1h1, (2,3))) - H(marg(Py0y1m1h1, (1,2,3))))

			Iz0m2j0 = H(marg(Pz0z1m2, (0,)))+H(marg(Pz0z1m2j0, (2,3))) - H(marg(Pz0z1m2j0, (0,2,3)))
			#print('Iz0m2j0 ',H(marg(Pz0z1m2, (0,)))+H(marg(Pz0z1m2j0, (2,3))) - H(marg(Pz0z1m2j0, (0,2,3))))
			Iz1m2j1 = H(marg(Pz0z1m2, (1,)))+H(marg(Pz0z1m2j1, (2,3))) - H(marg(Pz0z1m2j1, (1,2,3)))
			#print('Iz1m2j1 ',H(marg(Pz0z1m2, (1,)))+H(marg(Pz0z1m2j1, (2,3))) - H(marg(Pz0z1m2j1, (1,2,3))))



			
			
			#-------------VERIFICANDO DESIGUALDADE-------------------------------------------------------
			
			desig = I1 + I2 + I3
			#print('desig',desig)

			#desig = 0
			'''
			if(desig>bound):
				#print('U',epsilon, gamma, desig)
				gammaU = gamma
				if(abs(desig - bound) > atol):
					gamma = gammaU - (gammaU - gammaB)/2
				else:
					break
			else:
				#print('B',epsilon, gamma, desig)
				gammaB = gamma
				if(abs(desig - bound) > atol):
					gamma = gammaB + (gammaU - gammaB)/2
				else:
					break
			'''
			aux = aux +1

		aux = 0

		gammaB = 0.0 #gamma - deltaB
		G[i] = gamma
	
	#print('int',iterac)
	return (desig, I1, I2, I3, Ix0m0g0, Ix1m0g1, Iy0m1h0,Iy1m1h1, Iz0m2j0, Iz1m2j1)
		
		#	[1. 1. 1. 0. 2. 2. 1. 1. 1. 2. 2.]		