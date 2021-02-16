import numpy as np

from desc_entro.marginalizacao import marginalizacao

def rotulo(P):

	N = 9
	p = []
	for k in range(0,(2**N)):
		k = np.binary_repr(k)
		I = np.zeros((N-len(k)), dtype = 'int')
		for l in range(0,len(k)):
			I = np.hstack((I,int(k[l])))
		#print(I)
		AB = I[0] 
		BC = I[1]
		AC = I[2] 
		a=I[3]
		b=I[4]
		c=I[5]
		x=I[6]
		y=I[7]
		z=I[8]

		pabcDxyz = P

		#if(AB == 1 and BC ==0 and AC ==0):
		if(AB == 1):
			pabcDxyz = np.swapaxes(pabcDxyz,0,1)
			pabcDxyz = np.swapaxes(pabcDxyz,3,4)
		#if(BC == 1 and AB ==0 and AC ==0):
		if(BC == 1):
			pabcDxyz = np.swapaxes(pabcDxyz,1,2)
			pabcDxyz = np.swapaxes(pabcDxyz,4,5)
		#if(AC == 1 and AB ==0 and BC ==0):
		if(AC == 1):
			pabcDxyz = np.swapaxes(pabcDxyz,0,2)
			pabcDxyz = np.swapaxes(pabcDxyz,3,5)	
		if(a==1):
			pabcDxyz = np.flip(pabcDxyz,0)
		if(b==1):
			pabcDxyz = np.flip(pabcDxyz,1)
		if(c==1):
			pabcDxyz = np.flip(pabcDxyz,2)
		if(x==1):
			pabcDxyz = np.flip(pabcDxyz,3)
		if(y==1):
			pabcDxyz = np.flip(pabcDxyz,4)
		if(z==1):
			pabcDxyz = np.flip(pabcDxyz,5)

		#print(k)
		if(k==np.binary_repr(0)):
			p = np.array([pabcDxyz])
			#print(p)
		else:
			pe = np.array([pabcDxyz])
			p = np.concatenate((p, pe), axis = 0)

		


	#print('Antes',len(p))
	p = np.unique(p, axis = 0)

	return p

def rotulo2(P):

	N = 5
	p = []
	for k in range(0,(2**N)):
		k = np.binary_repr(k)
		I = np.zeros((N-len(k)), dtype = 'int')
		for l in range(0,len(k)):
			I = np.hstack((I,int(k[l])))
		#print(I)
		AB = I[0]
		a=I[1]
		b=I[2]
		x=I[3]
		y=I[4]

		pabDxy = P

		if(AB == 1):
			pabDxy = np.swapaxes(pabDxy,0,1)
			pabDxy = np.swapaxes(pabDxy,2,3)
		if(a==1):
			pabDxy = np.flip(pabDxy,0)
		if(b==1):
			pabDxy = np.flip(pabDxy,1)
		if(x==1):
			pabDxy = np.flip(pabDxy,2)
		if(y==1):
			pabDxy = np.flip(pabDxy,3)

		#print(k)
		if(k==np.binary_repr(0)):
			p = np.array([pabDxy])
			#print(p)
		else:
			pe = np.array([pabDxy])
			p = np.concatenate((p, pe), axis = 0)

		


	print('Antes',len(p))
	p = np.unique(p, axis = 0)

	return p
	'''
	for pabcDxyz in p:

		pm = marginalizacao(pabcDxyz, (3,4,5))
		#print('Depois',len(p))
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
	#print(p[0])