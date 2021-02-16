import random
import math
import numpy as np


def multiplas(n):
	pass
	EM=np.arange(0., 1, 1/n)
	GM= 1 - EM
	C = np.zeros((2,2), dtype='float')
	
	for i in range(0,(n)):
		epsilon=(1/n)*i
		EM[i]=epsilon
		for j in range(0,(n)):
			gamma=(1/n)*j*(1-epsilon)
		
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
			pabDxy = gamma*pr000 +epsilon*pd + (1-gamma-epsilon)*pw
		
			C[0][0] = pabDxy[0][0][0][0] + pabDxy[1][1][0][0] - pabDxy[0][1][0][0] - pabDxy[1][0][0][0]
			C[0][1] = pabDxy[0][0][0][1] + pabDxy[1][1][0][1] - pabDxy[0][1][0][1] - pabDxy[1][0][0][1]
			C[1][0] = pabDxy[0][0][1][0] + pabDxy[1][1][1][0] - pabDxy[0][1][1][0] - pabDxy[1][0][1][0]
			C[1][1] = pabDxy[0][0][1][1] + pabDxy[1][1][1][1] - pabDxy[0][1][1][1] - pabDxy[1][0][1][1]
			
			if(((C[0][0]+C[1][0])**2 + (C[0][1]-C[1][1])**2) > 4):
				GM[i]=gamma
				break
	
	return (EM, GM)