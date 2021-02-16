import random
import math
import numpy as np
import cvxpy as cp

def NPA(n):
		
	B=np.zeros(n, dtype='float')
	A=np.zeros(n, dtype='float')
	
	pr = np.array([[0.5,0.5,0.5,0],[0,0,0,0.5],[0,0,0,0.5],[0.5,0.5,0.5,0]])
	#pr010 = (0.5)*np.array([[1,0,1,1],[0,1,0,0],[0,1,0,0],[1,0,1,1]])
	#pr111 = (0.5)*np.array([[0,1,1,1],[1,0,0,0],[1,0,0,0],[0,1,1,1]])
	pl = np.array([[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
	#pl1111 = np.array([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
	pi = 0.25*np.ones((4,4))

	for i in range (0,n):
	    #b=0.6+(1/n)*i*0.2
	    b=(1/n)*i
	    B[i]=b
	    a=cp.Variable()
	    x=cp.Variable()
	    y=cp.Variable()
	    F = cp.Variable((5,5), symmetric=True)
	
	    #p = a*pr + (1-a)*(b*pl + (1-b)*pi)
	    p = a*pr + b*pl + (1-a-b)*pi
	
	    constraints = [F >> 0,
	                F[0,0] == 1,
	                F[0,1] == p[0,0]+p[1,0],
	                F[0,2] == p[0,2]+p[1,2],
	                F[0,3] == p[0,0]+p[2,0],
	                F[0,4] == p[0,1]+p[2,1],
	                F[1,1] == p[0,0]+p[1,0],
	                F[1,2] == x,
	                F[1,3] == p[0,0],
	                F[1,4] == p[0,1],
	                F[2,2] == p[0,2]+p[1,2],
	                F[2,3] == p[0,2],
	                F[2,4] == p[0,3],
	                F[3,3] == p[0,0]+p[2,0],
	                F[3,4] == y,
	                F[4,4] == p[0,1]+p[2,1] ]
	    prob = cp.Problem(cp.Maximize(a),constraints)
	    prob.solve()
	    if(prob.value >= 0):
	   		A[i]=prob.value
	    #print(B[i], A[i])
	#plt.plot(B,A, label='Q$_1$')

	return (B, A)