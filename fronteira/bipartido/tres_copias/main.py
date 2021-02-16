import random
import math
import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)


from newic_uma import *
from newic_tres import *
from npa import *



n=50

###########################################################################################################################
			# HIERARQUIA NPA
###########################################################################################################################

(B, A) = NPA(n)

###########################################################################################################################
			# FRONTEIRA UMA COPIA
###########################################################################################################################

(E1, G1) = verifica_fronteira1(n)

###########################################################################################################################
			# FRONTEIRA COM TRES COPIAS
###########################################################################################################################

(E3, G3) = verifica_fronteira3(n,1)


###########################################################################################################################
			# PLOT
###########################################################################################################################

plt.figure()
plt.style.use('classic') #coloca ticks "in"
plt.plot(E1,G1,label='Uma copia',linewidth=2.0, c='tab:blue')
plt.plot(E3,G3,label='Tres copias',linewidth=1.5, c='tab:orange')
plt.plot(B,A, label='Q$_1$',linewidth=1.5,c='green')

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
nome = ('tres_copias50.png')
plt.savefig(nome, dots=100)
plt.close(fig)

