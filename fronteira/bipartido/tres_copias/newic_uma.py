import random
import math
import numpy as np


#------------FUNÇÃO QUE CALCULA A ENTROPIA------------------------------------------
def H(prob):
	S=np.size(prob)# Numero de elementos
	Pro=np.reshape(prob, S) #concatenando todos os elementos num vetor
	h=np.zeros(S, dtype='float')
	for i in range(0,S): #Calcuando entropia para as probabilidades não nulas
		if Pro[i]!=0.0:
			h[i]=-Pro[i]*math.log(Pro[i],2)
	Ent=h.sum() # Entropia de Shannon
	return Ent

def verifica_fronteira1(n, t=None):
	#Declarando vetores
	pby=np.zeros((2,2), dtype='float')
	paDx=np.zeros((2,2), dtype='float')
	pbDy=np.zeros((2,2), dtype='float')
	pmg0=np.zeros((2,2), dtype='float')
	pmg1=np.zeros((2,2), dtype='float')
	pz0mg0=np.zeros((2,2,2), dtype='float')
	pz0mg1=np.zeros((2,2,2), dtype='float')
	pz1mg1=np.zeros((2,2,2), dtype='float')
	pz1mg0=np.zeros((2,2,2), dtype='float')
	pz0z1mg1=np.zeros((2,2,2,2), dtype='float')
	pz0z1mg0=np.zeros((2,2,2,2), dtype='float')
	pgDbmy=np.zeros((2,2,2,2), dtype='float')
	pabDxy=np.zeros((2,2,2,2), dtype='float')
	
	E=np.arange(0., 1, 1/n)
	G=1 - E
	P=np.zeros((2, 2, 2, 2, 2, 2, 2, 2), dtype='float')
	#Probabilidades constantes
	pz0=np.array([0.5,0.5])
	pz1=np.array([0.5,0.5])
	pz0z1=np.outer(pz0,pz1)
	py=np.array([0.5,0.5])
	px=np.array([0.5,0.5])

#------------PROBABILIDAES-CONDICIONAIS QUE NÃO DEPENDEM DO RECURSO-----------------
	
	#p(x|z0,z1)
	pxDz0z1=np.array([[[1,0],[0,1]],[[0,1],[1,0]]])
	
	#p(m|z0,a)
	pmDz0a=np.array([[[1,0],[0,1]],[[0,1],[1,0]]])
	
	#p(g|b,m)
	pgDbm=np.array([[[1,0],[0,1]],[[0,1],[1,0]]])
#-----------VARIANDO PARAMETROS------------------------------------------------------------

	for i in range(0,n):
		epsilon=(1/n)*i
		#epsilon=0.6+(1/n)*i*(0.2)
		#epsilon = 1.0
		E[i]=epsilon
		for j in range(0,n):
			gamma=(1/n)*j*(1-epsilon)
			#gamma=0.0
	
	#-----------CONSTRUINDO RECURSO------------------------------------------------------------
	
			#Caixa PR
			pr000 = (0.5)*np.array([[[[1,1],[1,0]],[[0,0],[0,1]]],[[[0,0],[0,1]],[[1,1],[1,0]]]])
			#pr010 = (0.5)*np.array([[[[1,0],[1,1]],[[0,1],[0,0]]],[[[0,1],[0,0]],[[1,0],[1,1]]]])
			#pr111 = (0.5)*np.array([[[[0,1],[1,1]],[[1,0],[0,0]]],[[[1,0],[0,0]],[[0,1],[1,1]]]])
			#ruido branco
			pw = (0.25)*np.array([[[[1,1],[1,1]],[[1,1],[1,1]]],[[[1,1],[1,1]],[[1,1],[1,1]]]])
			#Caixa determinística
			pd = np.array([[[[1,1],[1,1]],[[0,0],[0,0]]],[[[0,0],[0,0]],[[0,0],[0,0]]]])
			#pl1111 = np.array([[[[0,0],[0,1]],[[0,0],[1,0]]],[[[0,1],[0,0]],[[1,0],[0,0]]]])
	
			#região do politopo não sinalizante
			#pabDxy = gamma*pr000 +epsilon*pl1111 + (1-gamma-epsilon)*pw
			#pabDxy = gamma*pr000 +epsilon*pr010 + (1-gamma-epsilon)*pw
			#pabDxy = gamma*pr000 +epsilon*pr111 + (1-gamma-epsilon)*pw
			pabDxy = gamma*pr000 +epsilon*pd + (1-gamma-epsilon)*pw
			#print(pabDxy)
	
			#print(pabDxy)
	#-------PROBABILIDADES CONDICIONAIS QUE DEPENDEM DO RECURSO--------------------------------
	
			#p(g|y,b,m)
			'''
			pbDxy=pabDxy.sum(axis=0,dtype='float')
			for b in range(0,2):
				for y in range(0,2):
					pby[b][y]=pbDxy[b][0][y]*py[y]
					pbDy[b][y]=pbDxy[b][0][y]
			pb=pby.sum(axis=1,dtype='float')
	
			for g in range(0,2):
				for b in range(0,2):
					for m in range(0,2):
						for y in range(0,2):
							pgDbmy[g][b][m][y] = (pb[b]*pgDbm[g][b][m])/pbDy[b][y]
			'''
	#-----------PROBABILIDADE CONJUNTA---------------------------------------------------------
			
			#p(z0,z1,a,x,m,b,y,g)
			for z0 in range(0,2):
				for z1 in range(0,2):
					for a in range(0,2):
						for x in range(0,2):
							for m in range(0,2):
								for b in range(0,2): 
									for y in range(0,2):
										for g in range(0,2):
											P[z0][z1][a][x][m][b][y][g] = pz0[z0]*pz1[z1]*pxDz0z1[x][z0][z1]*pmDz0a[m][z0][a]*pabDxy[a][b][x][y]*py[y]*pgDbm[g][b][m]
											#print('z0:', z0,'z0:', z1,'a:', a, 'x:', x, 'm:', m, 'b:', b,'y:', y,'g:', g, 'P = ',P[z0][z1][a][x][m][b][y][g])
			#print(H(P))
	#----------MARGINALIZANDO-------------------------------------------------------------------
			#p(z0,z1,m,g1)
			pz0z1xmbyg = P.sum(axis=2, dtype='float')
			pz0z1mbyg = pz0z1xmbyg.sum(axis = 2, dtype='float')
			pz0z1myg = pz0z1mbyg.sum(axis = 3, dtype='float')

			for z0 in range(0,2):
				for z1 in range(0,2):
					for m in range(0,2):
						for g1 in range(0,2):
							pz0z1mg1[z0][z1][m][g1] = pz0z1myg[z0][z1][m][1][g1]/py[1]
			#print(-H(pz0z1mg1))

			#p(z0,m,g1)
			pz0mg1 = pz0z1mg1.sum(axis=1, dtype='float')
			#print(pz0mg1)
			#print(+H(pz0mg1))



			#p(z0,m,g0)
			pz0myg = pz0z1myg.sum(axis=1,dtype='float')
			for z0 in range(0,2):
				for m in range(0,2):
					for g0 in range(0,2):
						pz0mg0[z0][m][g0] = pz0myg[z0][m][0][g0]/py[0]
			#print(-H(pz0mg0))
			#print(pz0mg0)

			#p(m,g0)
			pmg0 = pz0mg0.sum(axis=0,dtype='float')
			#print(+H(pmg0))

			#p(z0,z1)
			pz0z1yg = pz0z1myg.sum(axis=2,dtype = 'float')
			pz0z1g = pz0z1yg.sum(axis=2,dtype = 'float')
			pz0z1 = pz0z1g.sum(axis=2,dtype = 'float')
			#print(+H(pz0z1))

			#p(m)
			pm = pmg0.sum(axis=1,dtype='float')
			#print(-H(pm))
	#-------------TESTES------------------------------------------------------------------------
			'''
			#p(mg1)
			pmg1 = pz1mg1.sum(axis=0,dtype='float')

			#p(z1,m,g1)
			pz1mg1 = pz0z1mg1.sum(axis=0, dtype='float')
			#print(pz1mg1)

			pz0 = pz0z1.sum(axis = 1, dtype='float')


			pz1 = pz0z1.sum(axis = 0, dtype='float')
			
			#print('Iz1g0m',H(pz1)+H(pmg0)-H(pz1mg0))

			print('Iz0g1m',H(pz0)+H(pmg1)-H(pz0mg1))

			
			pz1 = pz0z1.sum(axis = 0, dtype='float')
			pz1mg1 = pz0z1mg1.sum(axis = 0, dtype='float')
			pmg1 = pz1mg1.sum(axis = 0, dtype='float')
			print('Iz1g1m',H(pz1)+H(pmg1)-H(pz1mg1))

			print('Iz0z1',H(pz0)+H(pz1)-H(pz0z1))

			print('Iz0z1g1m',H(pz0mg1)+H(pz1mg1)-H(pmg1)-H(pz0z1mg1))
			'''
	#-------------VERIFICANDO DESIGUALDADE-------------------------------------------------------
			atol=10**-8
			if((-H(pm)+ H(pz0z1)+H(pmg0)-H(pz0mg0)+H(pz0mg1)-H(pz0z1mg1)) > atol): # 03
				#print('soma',(-H(pm)+ H(pz0z1)+H(pmg0)-H(pz0mg0)+H(pz0mg1)-H(pz0z1mg1)))
				G[i]=gamma
				if(t!=None):
					print('viola', epsilon, gamma,'\n')
				break
			else:
				if(t!=None):
					print('NAO viola', epsilon, gamma,'\n')
	return (E, G)

