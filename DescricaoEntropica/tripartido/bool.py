import math
import numpy as np

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