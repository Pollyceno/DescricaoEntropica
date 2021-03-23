import random
import math
import numpy as np


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

def verifica_fronteira3(n, t=None):
	#Declarando vetores
	pby=np.zeros((2,2), dtype='float')
	paDx=np.zeros((2,2), dtype='float')
	pbDy=np.zeros((2,2), dtype='float')
	pmg1=np.zeros((2,2), dtype='float')
	pmg2=np.zeros((2,2), dtype='float')
	pz1mg1=np.zeros((2,2,2), dtype='float')
	pz1mg2=np.zeros((2,2,2), dtype='float')
	pz2mg2=np.zeros((2,2,2), dtype='float')
	pz2mg1=np.zeros((2,2,2), dtype='float')
	pz1z2mg2=np.zeros((2,2,2,2), dtype='float')
	pz1z2mg1=np.zeros((2,2,2,2), dtype='float')
	pgDbmy=np.zeros((2,2,2,2), dtype='float')
	pabDxy=np.zeros((2,2,2,2), dtype='float')

	pz0z1z2z3mg0 = np.zeros((2,2,2,2,2,2), dtype='float')
	pz0z1z2z3mg1 = np.zeros((2,2,2,2,2,2), dtype='float')
	pz0z1z2z3mg2 = np.zeros((2,2,2,2,2,2), dtype='float')
	pz0z1z2z3mg3 = np.zeros((2,2,2,2,2,2), dtype='float')
	
	E=np.arange(0., 1, 1/n)
	G=1 - E
	P=np.zeros((2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), dtype='float')

	Pz0z1z2z3x12x22x11a12a22a11y22b12b22b11mg0=np.zeros((2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), dtype='float')
	Pz0z1z2z3x12x22x11a12a22a11y22b12b22b11mg1=np.zeros((2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), dtype='float')
	Pz0z1z2z3x12x22x11a12a22a11y12b12b22b11mg2=np.zeros((2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), dtype='float')
	Pz0z1z2z3x12x22x11a12a22a11y12b12b22b11mg3=np.zeros((2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), dtype='float')
	#Probabilidades constantes
	pz0=np.array([0.5,0.5])
	pz1=np.array([0.5,0.5])
	pz2=np.array([0.5,0.5])
	pz3=np.array([0.5,0.5])
	pz1z2=np.outer(pz1,pz2)
	py11=np.array([0.5,0.5])
	py12=np.array([0.5,0.5])
	py22=np.array([0.5,0.5])
	#px11=np.array([0.5,0.5])
	#px12=np.array([0.5,0.5])
	#px22=np.array([0.5,0.5])

#------------PROBABILIDAES-CONDICIONAIS QUE NÃO DEPENDEM DO RECURSO-----------------
	
	p2 = distribuicao(2)
	p3 = distribuicao(3)
	p4 = distribuicao(4)

	#p(x12|z0,z1)
	px12Dz0z1=p2

	#p(x22|z2,z3)
	px22Dz2z3=p2
	
	#p(m|z0,a11,a12)
	pmDz0a11a12 = p3

	#p(g0|m,b11,b12)
	pg0Dmb11b12 = p3

	#p(g1|m,b11,b12)
	pg1Dmb11b12 = p3

	#p(g2|m,b11,b22)
	pg2Dmb11b22 = p3

	#p(g3|m,b11,b22)
	pg3Dmb11b22 = p3

	#p(x11|z0,z2,a12,a22)
	px11Dz0z2a12a22	= p4

	'''
	#p(x12|z0,z1)
	px12Dz0z1=np.array([[[1,0],[0,1]],[[0,1],[1,0]]])

	#p(x22|z2,z3)
	px22Dz2z3=np.array([[[1,0],[0,1]],[[0,1],[1,0]]])
	
	#p(m|z0,a11,a12)
	pmDz0a11a12 = np.array([[[[1,0],[0,1]],[[0,1],[1,0]]],[[[0,1],[1,0]],[[1,0],[0,1]]]])	

	#p(g0|m,b11,b12)
	pg0Dmb11b12 = np.array([[[[1,0],[0,1]],[[0,1],[1,0]]],[[[0,1],[1,0]],[[1,0],[0,1]]]])

	#p(g1|m,b11,b12)
	pg1Dmb11b12 = np.array([[[[1,0],[0,1]],[[0,1],[1,0]]],[[[0,1],[1,0]],[[1,0],[0,1]]]])

	#p(g2|m,b11,b22)
	pg2Dmb11b22 = np.array([[[[1,0],[0,1]],[[0,1],[1,0]]],[[[0,1],[1,0]],[[1,0],[0,1]]]])

	#p(g3|m,b11,b22)
	pg3Dmb11b22 = np.array([[[[1,0],[0,1]],[[0,1],[1,0]]],[[[0,1],[1,0]],[[1,0],[0,1]]]])

	#p(x11|z0,z2,a12,a22)
	px11Dz0z2a12a22	= np.array([[[[[1,0],[0,1]],[[0,1],[1,0]]],[[[0,1],[1,0]],[[1,0],[0,1]]]],[[[[0,1],[1,0]],[[1,0],[0,1]]],[[[1,0],[0,1]],[[0,1],[1,0]]]]])
	'''
#-----------VARIANDO PARAMETROS------------------------------------------------------------

	for i in range(0,(n)):
		epsilon=(1/n)*i
		#epsilon=0.6+(1/n)*i*(0.2)
		E[i]=epsilon
		for j in range(0,(n)):
			gamma=(1/n)*j*(1-epsilon)
			#gamma=1.0
	
	#-----------CONSTRUINDO RECURSO------------------------------------------------------------
	
			#Caixa PR
			pr = (0.5)*np.array([[[[1,1],[1,0]],[[0,0],[0,1]]],[[[0,0],[0,1]],[[1,1],[1,0]]]])
			#ruido branco
			pw = (0.25)*np.array([[[[1,1],[1,1]],[[1,1],[1,1]]],[[[1,1],[1,1]],[[1,1],[1,1]]]])
			#Caixa determinística
			pd = np.array([[[[1,1],[1,1]],[[0,0],[0,0]]],[[[0,0],[0,0]],[[0,0],[0,0]]]])
	
			#região do politopo não sinalizante
			pa11b11Dx11y11 = gamma*pr +epsilon*pd + (1-gamma-epsilon)*pw

			pa12b12Dx12y12 = pa11b11Dx11y11

			pa22b22Dx22y22 = pa11b11Dx11y11

	
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
			
			N = 16
			for k in range(0,(2**N)):
				k = np.binary_repr(k)
				I = np.zeros((N-len(k)), dtype = 'int')

				for l in range(0,len(k)):
					I = np.hstack((I,int(k[l])))

				#print(I)
				z0=I[0]
				z1=I[1]
				z2=I[2]
				z3=I[3]
				x12=I[4]
				x22=I[5]
				x11=I[6]
				a12=I[7]
				a22=I[8]
				a11=I[9]
				y12=I[10]
				y22=I[10]
				#y11 nao precisa porque é definido
				b12=I[11]
				b22=I[12]
				b11=I[13]
				m=I[14]
				#Iguais porque nao aparecem conjuntamente
				g0=I[15]
				g1=I[15]
				g2=I[15]
				g3=I[15]
				

				Pz0z1z2z3x12x22x11a12a22a11y22b12b22b11mg0[z0][z1][z2][z3][x12][x22][x11][a12][a22][a11][y22][b12][b22][b11][m][g0] = pz0[z0]*pz1[z1]*pz2[z2]*pz3[z3]*px12Dz0z1[x12][z0][z1]*px22Dz2z3[x22][z2][z3]*px11Dz0z2a12a22[x11][z0][z2][a12][a22]*pmDz0a11a12[m][z0][a11][a12]*pa12b12Dx12y12[a12][b12][x12][0]*pa22b22Dx22y22[a22][b22][x22][y22]*pa11b11Dx11y11[a11][b11][x11][0]*py22[y22]*pg0Dmb11b12[g0][m][b11][b12]
				#if(z0 == 0 and g0 == 1 and Pz0z1z2z3x12x22x11a12a22a11y22b12b22b11mg0[z0][z1][z2][z3][x12][x22][x11][a12][a22][a11][y22][b12][b22][b11][m][g0] != 0.0):
					#print('z0', z0,'z1', z1,'z2', z2,'z3', z3,'x1', x12,'x2', x22,'x1', x11,'a12', a12,'a22', a22,'a11', a11,'y22', y22,'b12', b12,'b22', b22,'b11', b11,'m,', m,'g0', g0, Pz0z1z2z3x12x22x11a12a22a11y22b12b22b11mg0[z0][z1][z2][z3][x12][x22][x11][a12][a22][a11][y22][b12][b22][b11][m][g0])
				
				Pz0z1z2z3x12x22x11a12a22a11y22b12b22b11mg1[z0][z1][z2][z3][x12][x22][x11][a12][a22][a11][y22][b12][b22][b11][m][g1] = pz0[z0]*pz1[z1]*pz2[z2]*pz3[z3]*px12Dz0z1[x12][z0][z1]*px22Dz2z3[x22][z2][z3]*px11Dz0z2a12a22[x11][z0][z2][a12][a22]*pmDz0a11a12[m][z0][a11][a12]*pa12b12Dx12y12[a12][b12][x12][1]*pa22b22Dx22y22[a22][b22][x22][y22]*pa11b11Dx11y11[a11][b11][x11][0]*py22[y22]*pg1Dmb11b12[g1][m][b11][b12]
				#if(z1 == 0 and g1 == 1 and Pz0z1z2z3x12x22x11a12a22a11y22b12b22b11mg1[z0][z1][z2][z3][x12][x22][x11][a12][a22][a11][y22][b12][b22][b11][m][g1] != 0.0):
					#print('z0', z0,'z1', z1,'z2', z2,'z3', z3,'x1', x12,'x2', x22,'x1', x11,'a12', a12,'a22', a22,'a11', a11,'y22', y22,'b12', b12,'b22', b22,'b11', b11,'m,', m,'g0', g0, Pz0z1z2z3x12x22x11a12a22a11y22b12b22b11mg1[z0][z1][z2][z3][x12][x22][x11][a12][a22][a11][y22][b12][b22][b11][m][g1])

				Pz0z1z2z3x12x22x11a12a22a11y12b12b22b11mg2[z0][z1][z2][z3][x12][x22][x11][a12][a22][a11][y12][b12][b22][b11][m][g2] = pz0[z0]*pz1[z1]*pz2[z2]*pz3[z3]*px12Dz0z1[x12][z0][z1]*px22Dz2z3[x22][z2][z3]*px11Dz0z2a12a22[x11][z0][z2][a12][a22]*pmDz0a11a12[m][z0][a11][a12]*pa12b12Dx12y12[a12][b12][x12][y12]*pa22b22Dx22y22[a22][b22][x22][0]*pa11b11Dx11y11[a11][b11][x11][1]*py12[y12]*pg2Dmb11b22[g2][m][b11][b22]
				#if(z2 == 0 and g2 == 1 and Pz0z1z2z3x12x22x11a12a22a11y12b12b22b11mg2[z0][z1][z2][z3][x12][x22][x11][a12][a22][a11][y12][b12][b22][b11][m][g2] != 0.0):
					#print('z0', z0,'z1', z1,'z2', z2,'z3', z3,'x1', x12,'x2', x22,'x1', x11,'a12', a12,'a22', a22,'a11', a11,'y12', y12,'b12', b12,'b22', b22,'b11', b11,'m,', m,'g2', g2, Pz0z1z2z3x12x22x11a12a22a11y12b12b22b11mg2[z0][z1][z2][z3][x12][x22][x11][a12][a22][a11][y12][b12][b22][b11][m][g2])
				
				Pz0z1z2z3x12x22x11a12a22a11y12b12b22b11mg3[z0][z1][z2][z3][x12][x22][x11][a12][a22][a11][y12][b12][b22][b11][m][g3] = pz0[z0]*pz1[z1]*pz2[z2]*pz3[z3]*px12Dz0z1[x12][z0][z1]*px22Dz2z3[x22][z2][z3]*px11Dz0z2a12a22[x11][z0][z2][a12][a22]*pmDz0a11a12[m][z0][a11][a12]*pa12b12Dx12y12[a12][b12][x12][y12]*pa22b22Dx22y22[a22][b22][x22][1]*pa11b11Dx11y11[a11][b11][x11][1]*py12[y12]*pg3Dmb11b22[g3][m][b11][b22]
				#if(z3 == 0 and g3 == 1 and Pz0z1z2z3x12x22x11a12a22a11y12b12b22b11mg3[z0][z1][z2][z3][x12][x22][x11][a12][a22][a11][y12][b12][b22][b11][m][g3] != 0.0):
					#print('z0', z0,'z1', z1,'z2', z2,'z3', z3,'x1', x12,'x2', x22,'x1', x11,'a12', a12,'a22', a22,'a11', a11,'y12', y12,'b12', b12,'b22', b22,'b11', b11,'m,', m,'g3', g3, Pz0z1z2z3x12x22x11a12a22a11y12b12b22b11mg3[z0][z1][z2][z3][x12][x22][x11][a12][a22][a11][y12][b12][b22][b11][m][g3])
				#----------MARGINALIZANDO-------------------------------------------------------------------
			
			#p(z0,z1,z2,z3,m,gi)
			#Somando em x12,x22,x11,a12,a22,a11,y22,b12,b22,b11

			pz0z1z2z3mg0 = Pz0z1z2z3x12x22x11a12a22a11y22b12b22b11mg0
			pz0z1z2z3mg1 = Pz0z1z2z3x12x22x11a12a22a11y22b12b22b11mg1
			pz0z1z2z3mg2 = Pz0z1z2z3x12x22x11a12a22a11y12b12b22b11mg2
			pz0z1z2z3mg3 = Pz0z1z2z3x12x22x11a12a22a11y12b12b22b11mg3
			for k in range(0,10):
				
				pz0z1z2z3mg0 = pz0z1z2z3mg0.sum(axis=4,dtype='float')
				pz0z1z2z3mg1 = pz0z1z2z3mg1.sum(axis=4,dtype='float')
				pz0z1z2z3mg2 = pz0z1z2z3mg2.sum(axis=4,dtype='float')
				pz0z1z2z3mg3 = pz0z1z2z3mg3.sum(axis=4,dtype='float')

			#p(z0,z1,m,g1)
			pz0z1z3mg1 =pz0z1z2z3mg1.sum(axis=2,dtype='float')
			pz0z1mg1 =pz0z1z3mg1.sum(axis=2,dtype='float')

			#p(z0,m,g1)
			pz0mg1 =pz0z1mg1.sum(axis=1,dtype='float')

			#p(z1,m,g1)
			pz1mg1 =pz0z1mg1.sum(axis=0,dtype='float')
			#print('pz0mg0',pz1mg1)

			#p(m,g1)
			pmg1 =pz0mg1.sum(axis=0,dtype='float')

			#p(z0,m,g0)
			pz0z2z3mg0 = pz0z1z2z3mg0.sum(axis=1,dtype='float')
			pz0z3mg0 = pz0z2z3mg0.sum(axis=1,dtype='float')
			pz0mg0 = pz0z3mg0.sum(axis=1,dtype='float')
			#print('pz0mg0',pz0mg0)
			#print(pz0mg0.sum())

			#p(m,g0)
			pmg0 = pz0mg0.sum(axis=0,dtype='float')

			#p(z0,z2,m,g2)
			pz0z2z3mg2 = pz0z1z2z3mg2.sum(axis=1,dtype='float')
			pz0z2mg2 = pz0z2z3mg2.sum(axis=2,dtype='float')

			#p(z0,m,g2)
			pz0mg2 = pz0z2mg2.sum(axis=1,dtype='float')

			#p(z2,m,g2)
			pz2mg2 = pz0z2mg2.sum(axis=0,dtype='float')
			#print('pz2mg2',pz2mg2)

			#p(m,g2)
			pmg2 = pz2mg2.sum(axis=0,dtype='float')

			#p(z0,z3,m,g3)
			pz0z2z3mg3 = pz0z1z2z3mg3.sum(axis=1,dtype='float')
			pz0z3mg3 = pz0z2z3mg3.sum(axis=1,dtype='float')

			#p(z0,m,g3)
			pz0mg3 = pz0z3mg3.sum(axis=1,dtype='float')

			#p(z3,m,g3)
			pz3mg3 = pz0z3mg3.sum(axis=0,dtype='float')
			#print('pz3mg3',pz3mg3)

			#p(m,g3)
			pmg3 = pz3mg3.sum(axis=0,dtype='float')

			#p(m)
			pm = pmg3.sum(axis=1,dtype='float')
	#-------------TESTE ---------------------------------------------

			#pz0g0 = pz0mg0.sum(axis=1,dtype='float')
			#pg0 = pz0g0.sum(axis=0,dtype='float')

			'''
			print('Iz0g0',IM(pz0,pg0,pz0g0))
			print('Iz0mg0',IM(pz0,pmg0,pz0mg0))
			print('Iz1mg1',IM(pz1,pmg1,pz1mg1))
			print('Iz2mg2',IM(pz2,pmg2,pz2mg2))
			print('Iz3mg3',IM(pz3,pmg3,pz3mg3))
			print('Iz0z1mg1',IM(pz0mg1, pz1mg1, pz0z1mg1,pmg1))
			print('Iz0z2mg2',IM(pz0mg2, pz2mg2, pz0z2mg2,pmg2))
			print('Iz0z3mg3',IM(pz0mg3, pz3mg3, pz0z3mg3,pmg3))
			print('Desig',(IM(pz0,pmg0,pz0mg0) + IM(pz1,pmg1,pz1mg1) + IM(pz2,pmg2,pz2mg2) + IM(pz3,pmg3,pz3mg3) + IM(pz0mg1, pz1mg1, pz0z1mg1,pmg1) + IM(pz0mg2, pz2mg2, pz0z2mg2,pmg2) + IM(pz0mg3, pz3mg3, pz0z3mg3,pmg3) - H(pm) ))
			print('left',(IM(pz0,pmg0,pz0mg0) + IM(pz1,pmg1,pz1mg1) + IM(pz2,pmg2,pz2mg2) + IM(pz3,pmg3,pz3mg3) + IM(pz0mg1, pz1mg1, pz0z1mg1,pmg1) + IM(pz0mg2, pz2mg2, pz0z2mg2,pmg2) + IM(pz0mg3, pz3mg3, pz0z3mg3,pmg3)))
			print('Hm',H(pm))
			'''
	#-------------VERIFICANDO DESIGUALDADE-------------------------------------------------------
			atol=10**-8
			if((IM(pz0,pmg0,pz0mg0) + IM(pz1,pmg1,pz1mg1) + IM(pz2,pmg2,pz2mg2) + IM(pz3,pmg3,pz3mg3) + IM(pz0mg1, pz1mg1, pz0z1mg1,pmg1) + IM(pz0mg2, pz2mg2, pz0z2mg2,pmg2) + IM(pz0mg3, pz3mg3, pz0z3mg3,pmg3) - H(pm) )> atol):
				G[i]=gamma
				if(t!=None):
					print('viola', epsilon, gamma)
				break
			else:
				if(t!=None):
					print('NAO viola', epsilon, gamma)
	return (E, G)
	