import random
import math
import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)


#from newic import *
#from npa import *
#from multiplas import *
#from oldic import *
#from ic import *
from novaic import *
#from rotulo import *
from marginalizacao import *
from recurso import *
from grupo import *
import time


n=1


###########################################################################################################################
			# FRONTEIRA COM O PROTOCOLO ANTIGO
###########################################################################################################################
t=True
atol = 10**-8
per = 0
for N in range(29,30):
	
	pabcDxyz = recurso(N) #Gera representante da classe N

	recursos = permuta(pabcDxyz) # Geratodas as permutacoes da classe
	caixa = 0
	for p in recursos:
	#	print('Caixa: ', caixa)

		#tempo = time.time()
		(desig, I1, I2, I3, Ix0m0g0, Ix1m0g1, Iy0m1h0,Iy1m1h1, Iz0m2j0, Iz1m2j1) = verifica_fronteiraS(n,p) # Testa violacao da caixa p
		#print("Total--- %s seconds ---" % (time.time() - tempo))

		caixa = caixa +1

		if(I1 > atol or I1 > atol or I3 > atol):
			inf= np.array([caixa, desig, I1, I2, I3, Ix0m0g0, Ix1m0g1, Iy0m1h0,Iy1m1h1, Iz0m2j0, Iz1m2j1])
			if(t==True):
				I1I2 = np.array([inf])
				t=False
			else:
				inf2 = np.array([inf])
				I1I2 = np.concatenate((I1I2, inf2), axis = 0)
			np.savetxt('Info.txt', I1I2, fmt="%s")
			np.savetxt('porcentagem.txt', [100*per/(len(recursos)), ' %'], fmt="%s")
			per = per +1







