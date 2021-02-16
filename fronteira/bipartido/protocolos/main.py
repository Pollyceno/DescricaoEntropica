import random
import math
import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)


from newic import *
from npa import *
from multiplas import *
from oldic import *
from ic import *
from novaic import *
from rotulo import *


n=20


###########################################################################################################################
			# DISTRIBUIÇÃO DE PROBABILIDADES RELATIVAS AS DIFRENTES FUNCOES BOOLEANAS
###########################################################################################################################
#np.array([[[],[]],[[],[]]])
f1 = np.array([[[1,1],[1,1]],[[0,0],[0,0]]])
f2 = np.array([[[1,1],[1,0]],[[0,0],[0,1]]])
f3 = np.array([[[1,1],[0,1]],[[0,0],[1,0]]])
f4 = np.array([[[1,0],[1,1]],[[0,1],[0,0]]])
f5 = np.array([[[0,1],[1,1]],[[1,0],[0,0]]])
f6 = np.array([[[0,0],[1,1]],[[1,1],[0,0]]])
f7 = np.array([[[0,1],[0,1]],[[1,0],[1,0]]])
f8 = np.array([[[0,1],[1,0]],[[1,0],[0,1]]])
f9 = np.array([[[1,0],[1,0]],[[0,1],[0,1]]])
f10 = np.array([[[1,1],[0,0]],[[0,0],[1,1]]])
f11 = np.array([[[1,0],[0,1]],[[0,1],[1,0]]])
f12 = np.array([[[1,0],[0,0]],[[0,1],[1,1]]])
f13 = np.array([[[0,1],[0,0]],[[1,0],[1,1]]])
f14 = np.array([[[0,0],[1,0]],[[1,1],[0,1]]])
f15 = np.array([[[0,0],[0,1]],[[1,1],[1,0]]])
f16 = np.array([[[0,0],[0,0]],[[1,1],[1,1]]])


F = np.array([f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16])
'''
for k in range(0,len(F)):
	print('boolean',k)
	frot = rotuloBool(F[k])
	print('Depois',len(frot))
	for i in range(0,len(F)):
		f = np.array([F[i]])
		for j in frot:
			j = np.array([j])
			#print(i,j)
			I = np.concatenate((f, j), axis = 0)
	
			I = np.unique(I, axis = 0)
			if(len(I)==1):
				print(i)
'''

###########################################################################################################################
			# HIERARQUIA NPA
###########################################################################################################################

(B, A) = NPA(n)


###########################################################################################################################
			# MULTIPLAS COPIAS
###########################################################################################################################

#(EM, GM) = multiplas(n)


###########################################################################################################################
			# FRONTEIRA COM O PROTOCOLO ANTIGO
###########################################################################################################################

#(E, G) = verifica_fronteira(F[10],F[10],F[10], n,1)
#(E, G) = verifica_fronteira(F[7],F[10],F[5], n,1)
(E, G) = verifica_fronteira2(F[10],F[10],F[10], n)
#(E2, G2) = verifica_fronteira3(F[7],F[10],F[5], n)

(E0, G0) = verifica_fronteira1(F[10],F[10],F[10], n)
#(E, G) = verifica_fronteira2(F[7],F[10],F[5], n)
(E2, G2) = verifica_fronteira3(F[10],F[10],F[10], n)

plt.figure()
plt.style.use('classic') #coloca ticks "in"

b = np.arange(0., 1, 0.01)
plt.plot(b, 1-b , label='NS',linewidth=2,c = 'black',linestyle='--')
#plt.plot(E,G,label='Usual',linewidth=1.5, c='tab:blue')
plt.plot(E0,G0,label='Old IC',linewidth=1.5, c='gold')
plt.plot(E,G,label='IC',linewidth=1.5, c='tab:blue')
plt.plot(E2,G2,label='New criterion',linewidth=1.5, c='tab:red')
plt.plot(B,A, label='Q$_1$',linewidth=1.5,c='green')
#plt.plot(EM,GM, label='Multiplas',linewidth=1.5,c='gold', linestyle='--')
#plt.title('10-7-9',fontsize='20')
plt.xlabel(r'$\varepsilon$', fontsize='30')
plt.xticks(fontsize=20)
plt.ylabel(r'$\gamma$', fontsize='30')
plt.yticks(fontsize=20)
plt.legend(fontsize=20,fancybox=True, shadow=True).get_frame().set_edgecolor('lightgray')
plt.ylim(-0.01,1.01)
plt.xlim(-0.01,(((n-1)/n)+0.01))

ax=plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(0.2))
		
			
#plt.show()

fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.tight_layout()
nome = ('fraca.png')
plt.savefig(nome, dots=100)
plt.close(fig)


'''
###########################################################################################################################
			# FRONTEIRAS COM NOVOS PROTOCOLOS
###########################################################################################################################
#l=len(F)
l=1
for i in range(0,l):
	for j in range(0,l):
		for k in range(0,l):

			i=7
			j=7
			k=7
			(E2, G2) = verifica_fronteira2(F[i],F[j],F[k], n)
			#(E2, G2) = verifica_fronteira(F[10],F[10],F[10], n)
			#(E2, G2) = verifica_fronteira(F[7],F[7],F[7], n)

			#print(np.where((G2>G)==True))

			plt.figure()
			plt.style.use('classic') #coloca ticks "in"

			b = np.arange(0., 1, 0.01)
			plt.plot(b, 1-b , label='NS',linewidth=2,c = 'black')
			plt.plot(E,G,label='Usual',linewidth=2.8, c='tab:blue')
			plt.plot(B,A, label='Q$_1$',linewidth=1.5,c='green')
			#plt.plot(EM,GM, label='Multiplas',linewidth=1.5,c='gold', linestyle='--')
			novo = (str(i)+' '+str(j)+' '+str(k))

			#E2=b
			#G2=1-b
			plt.plot(E2,G2,label=novo,linewidth=1.2,c='tab:orange')

			plt.xlabel(r'$\varepsilon$', fontsize='30')
			plt.xticks(fontsize=20)
			plt.ylabel(r'$\gamma$', fontsize='30')
			plt.yticks(fontsize=20)
			plt.legend(fontsize=20,fancybox=True, shadow=True).get_frame().set_edgecolor('lightgray')
			plt.ylim(-0.01,1.01)
			plt.xlim(-0.01,(((n-1)/n)+0.01))

			ax=plt.gca()
			ax.xaxis.set_major_locator(MultipleLocator(0.2))
			
			
			#plt.show()
			
			fig = plt.gcf()
			fig.set_size_inches(10, 8)
			plt.tight_layout()
			nome = (str(i)+'-'+str(j)+'-'+str(k)+'.png')
			plt.savefig(nome, dots=100)
			plt.close(fig)
			
'''
###########################################################################################################################
			# FRONTEIRAS COM NOVOS PROTOCOLOS
###########################################################################################################################
'''
for a in range(0,2):
	for z0 in range(0,2):
		for m in range(0,2):
			for b in range(0,2):
				for g in range(0,2):
					print('a:',a,' z0:', z0, ' m:', m, 'p(m) = ', F[0][m][a][z0], ' m:', m,' b:',b, ' g:',g, 'p(g) = ', F[0][g][m][b])

'''
