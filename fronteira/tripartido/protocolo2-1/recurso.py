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

def recurso(N):

	rep = np.loadtxt('box.txt')

	Ax = np.array([rep[N-1][0],rep[N-1][1]])
	By = np.array([rep[N-1][2],rep[N-1][3]])
	Cz = np.array([rep[N-1][4],rep[N-1][5]])
	AxBy = np.array([[rep[N-1][6],rep[N-1][7]],[rep[N-1][8],rep[N-1][9]]])
	AxCz = np.array([[rep[N-1][10],rep[N-1][11]],[rep[N-1][12],rep[N-1][13]]])
	ByCz = np.array([[rep[N-1][14],rep[N-1][15]],[rep[N-1][16],rep[N-1][17]]])
	AxByCz = np.array([[[rep[N-1][18],rep[N-1][19]],[rep[N-1][20],rep[N-1][21]]],[[rep[N-1][22],rep[N-1][23]],[rep[N-1][24],rep[N-1][25]]]])

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
		
		q = (1/8)*(1 + a*Ax[x] + b*By[y] + c*Cz[z] +a*b*AxBy[x][y] + a*c*AxCz[x][z] +b*c*ByCz[y][z] + a*b*c*AxByCz[x][y][z])
		if(q>= 10**-8):
			p[ind322(I[0],I[1],I[2],x,y,z)] = q
		else:
			p[ind322(I[0],I[1],I[2],x,y,z)] = 0
	return p

def recurso2():

	p = np.zeros((2**6), dtype='float')
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
	    
	    p[ind322(a,b,c,x,y,z)] = (1/3)*(((((1+b+x+y+(x*y))%2)*((1+c+z)%2))+(a*((1+y+(c*y)+(b*((c+z)%2)))%2)))%2)
	return p

def outros(N):
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

	if(N==4):
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

			if((a+b+c)%2 == ((x*y)+(x*z)+(y*z))%2):
				p[ind322(a,b,c,x,y,z)] = 1/4
			else:
				p[ind322(a,b,c,x,y,z)] = 0
		return p

	if(N==5):
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

			if((a+b+c)%2 == (x*y*z)):
				p[ind322(a,b,c,x,y,z)] = 1/4
			else:
				p[ind322(a,b,c,x,y,z)] = 0
		return p

	if(N==6):
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

			if((a+b)%2 == (x*y) or (b+c)%2 == (y*z) or (a+c)%2 == (x*z)):
				p[ind322(a,b,c,x,y,z)] = 1/4
			else:
				p[ind322(a,b,c,x,y,z)] = 0
		return p



