import math
import numpy as np
import itertools as itt

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
	if(type(p4)!=type(np.array([0]))): #sem condicional
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

			if((a+b)%2 == x*y):
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

	if(N==4):
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

			if((a+b+c)%2 == ((x*y)+(y*z)+(x*z))%2):
				p[a][b][c][x][y][z] = 1/4
			else:
				p[a][b][c][x][y][z] = 0

		return p

	if(N==5):
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
			#print(a, b, c, x, y, z)
			if((a+b)%2 == (x*y) or (b+c)%2 == (y*z) or (a+c)%2 == (x*z)):
				#print(a, b, c, x, y, z)
				p[a][b][c][x][y][z] = 1/4
			else:
				p[a][b][c][x][y][z] = 0

		return p