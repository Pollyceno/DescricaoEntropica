import math
import numpy as np

def ind322(a,b,c,x,y,z):
    # Behavior indices for 322 Bell scenario
    i=0
    for K1 in range(2):
        for K0 in range(2):
            for J1 in range(2):
                for J0 in range(2):
                    for I1 in range(2):
                        for I0 in range(2):
                            if K1==z and K0==c and J1==y and J0==b and I1==x and I0==a :
                                return i
                            else :
                                i=i+1

def recurso2(N):
	
	if(N==2):
		
		Ax = np.array([0,0])
		By = np.array([0,0])
		Cz = np.array([0,0])
		AxBy = np.array([[1,0],[0,0]])
		AxCz = np.array([[0,0],[1,0]])
		ByCz = np.array([[0,0],[0,1]])
		AxByCz = np.array([[[0,0],[1,0]],[[0,-1],[0,0]]])
		
		'''
		Ax = np.array([0,0])
		By = np.array([0,0])
		Cz = np.array([0,0])
		AxBy = np.array([[0,0],[0,0]])
		AxCz = np.array([[0,0],[0,0]])
		ByCz = np.array([[0,0],[0,0]])
		AxByCz = np.array([[[1,1],[1,1]],[[1,-1],[-1,1]]])
		'''
		'''
		Ax = np.array([1,1])
		By = np.array([1,1])
		Cz = np.array([1,1])
		AxBy = np.array([[1,1],[1,1]])
		AxCz = np.array([[1,1],[1,1]])
		ByCz = np.array([[1,1],[1,1]])
		AxByCz = np.array([[[1,1],[1,1]],[[1,1],[1,1]]])
		'''
		p = np.zeros((2**6), dtype='float')
		for k in range(0,(2**6)):
		    k = np.binary_repr(k)
		    I = np.zeros((6-len(k)), dtype = 'int')
		    for l in range(0,len(k)):
		        I = np.hstack((I,int(k[l])))
		    a = (-1)**I[0]
		    b = (-1)**I[1]
		    c = (-1)**I[2]
		    x = I[3]
		    y = I[4]
		    z = I[5]
		    
		    p[ind322(I[0],I[1],I[2],x,y,z)] = (1/8)*(1 + a*Ax[x] + b*By[y] + c*Cz[z] +a*b*AxBy[x][y] + a*c*AxCz[x][z] +b*c*ByCz[y][z] + a*b*c*AxByCz[x][y][z])
	
	if(N==3):
		p = np.zeros(2**6, dtype='float')
		for k in range(0,(2**6)):
			k = np.binary_repr(k)
			I = np.zeros((6-len(k)), dtype = 'int')
			for l in range(0,len(k)):
				I = np.hstack((I,int(k[l])))
			a = I[0]
			b = I[1]
			c = I[2]
			x = I[3]
			y = I[4]
			z = I[5]

			if((a+b+c)%2 == ((x*z)+(y*z))%2):
				p[ind322(a,b,c,x,y,z)] = 1/4
			else:
				p[ind322(a,b,c,x,y,z)] = 0


	return p

def recurso(N):
	if(N==10):
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

	if(N==0):
		p = np.zeros((2,2,2,2,2,2), dtype='float')
		for k in range(0,(2**6)):
			k = np.binary_repr(k)
			I = np.zeros((6-len(k)), dtype = 'int')
			for l in range(0,len(k)):
				I = np.hstack((I,int(k[l])))
			a = I[0]
			b = I[1]
			c = I[2]
			x = I[3]
			y = I[4]
			z = I[5]

			if((a ==0 ) and (b==0) and (c ==0)):
				p[a][b][c][x][y][z] = 1
			else:
				p[a][b][c][x][y][z] = 0

		return p

	if(N==1):
		p = np.zeros((2,2,2,2,2,2), dtype='float')
		for k in range(0,(2**6)):
			k = np.binary_repr(k)
			I = np.zeros((6-len(k)), dtype = 'int')
			for l in range(0,len(k)):
				I = np.hstack((I,int(k[l])))
			a = I[0]
			b = I[1]
			c = I[2]
			x = I[3]
			y = I[4]
			z = I[5]

			if((a ==1 ) and (b==0) and (c ==1)):
				p[a][b][c][x][y][z] = 1
			else:
				p[a][b][c][x][y][z] = 0

		return p

	if(N==2):
		p = np.zeros((2,2,2,2,2,2), dtype='float')
		for k in range(0,(2**6)):
			k = np.binary_repr(k)
			I = np.zeros((6-len(k)), dtype = 'int')
			for l in range(0,len(k)):
				I = np.hstack((I,int(k[l])))
			a = I[0]
			b = I[1]
			c = I[2]
			x = I[3]
			y = I[4]
			z = I[5]

			if((a ==0 ) and ((b+c)%2==y*z)):
				p[a][b][c][x][y][z] = 1/2
			else:
				p[a][b][c][x][y][z] = 0

		return p

	if(N==3):
		p = np.zeros((2,2,2,2,2,2), dtype='float')
		for k in range(0,(2**6)):
			k = np.binary_repr(k)
			I = np.zeros((6-len(k)), dtype = 'int')
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
		for k in range(0,(2**6)):
			k = np.binary_repr(k)
			I = np.zeros((6-len(k)), dtype = 'int')
			for l in range(0,len(k)):
				I = np.hstack((I,int(k[l])))
			a = (-1)**I[0]
			b = (-1)**I[1]
			c = (-1)**I[2]
			x = I[3]
			y = I[4]
			z = I[5]
			'''
			Ax = np.array([0,0])
			By = np.array([0,0])
			Cz = np.array([0,0])
			AxBy = np.array([[0,1],[0,0]])
			AxCz = np.array([[0,0],[1,0]])
			ByCz = np.array([[0,1],[0,0]])
			AxByCz = np.array([[[1,0],[0,0]],[[0,0],[0,-1]]])
			'''
			
			Ax = np.array([0,0])
			By = np.array([0,0])
			Cz = np.array([0,0])
			AxBy = np.array([[1,0],[0,0]])
			AxCz = np.array([[0,0],[1,0]])
			ByCz = np.array([[0,0],[0,1]])
			AxByCz = np.array([[[0,0],[1,0]],[[0,-1],[0,0]]])
			
			'''
			Ax = np.array([0,0])
			By = np.array([0,0])
			Cz = np.array([0,0])
			AxBy = np.array([[1,1],[0,0]])
			AxCz = np.array([[0,0],[1,0]])
			ByCz = np.array([[0,0],[0,0]])
			AxByCz = np.array([[[0,0],[0,0]],[[0,1],[0,-1]]])
			'''
			'''

			Ax = np.array([1,1])
			By = np.array([1,1])
			Cz = np.array([1,1])
			AxBy = np.array([[1,1],[1,1]])
			AxCz = np.array([[1,1],[1,1]])
			ByCz = np.array([[1,1],[1,1]])
			AxByCz = np.array([[[1,1],[1,1]],[[1,1],[1,1]]])
			'''

			p[I[0]][I[1]][I[2]][x][y][z] = (1/8)*(1 + a*Ax[x] + b*By[y] + c*Cz[z] +a*b*AxBy[x][y] + a*c*AxCz[x][z] +b*c*ByCz[y][z] + a*b*c*AxByCz[x][y][z])
			#print(p[a][b][c][x][y][z])
			#p[a][b][c][x][y][z] = (1/8)*(1 + a*(1-2*Ax) + b*(1-2*By) + c*(1-2*Cz) +a*b*(1-2*AxBy) + a*c*(1-2*AxCz) +b*c*(1-2*ByCz) + a*b*c*(1-2*AxByCz))
			'''
			if(((a+b)%2 == 0 and x==0 and y==1) or ((b+c)%2 == 0 and y==0 and z==1) or ((c+a)%2 == 0 and z==0 and x==1) or ((a+b+c)%2 == 0 and x==0 and y==0 and z==0) or ((a+b+c)%2 == 0 and x==1 and y==1 and z==1) ):
			#if(((a+b)%2 == (x+y-(x*y))) and ((a+c)%2 == (1-x+(x*z))) and ((b+c)%2 == (1-(y*z)))  and ((a+b+c)%2 == ((1-y+(x*y)+(x*z)+(y*z))-(x*y*z))) ):
				p[a][b][c][x][y][z] = 1/4
			else:
				p[a][b][c][x][y][z] = 0
			'''

		return p