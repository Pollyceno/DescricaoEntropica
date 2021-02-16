import random
import math
import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

from tripartido import *
from recurso import *
from npa322 import NPA322
from npa import NPA
from newic_uma import *
from multiplas import *



n=10

###########################################################################################################################
			# CAIXAS
###########################################################################################################################

p45 = outros(3)
pd = recurso(1)
pw = (1/8)*np.ones(64)


###########################################################################################################################
			# FRONTEIRA TRIPARTIDO
###########################################################################################################################

#(E,G)= verifica_fronteira3(n, p45, pd,  pw,1)


###########################################################################################################################
			# PLOT
###########################################################################################################################

plt.figure()
plt.style.use('classic') #coloca ticks "in"
b = np.arange(0., 1, 0.01)
plt.plot(b, 1-b , label='NS',c = 'r',linestyle='--')
#plt.plot(E,G,label='2-1',linewidth=1.5, c='tab:orange')

plt.xlabel(r'$\varepsilon$', fontsize='30')
plt.xticks(fontsize=20)
plt.ylabel(r'$\gamma$', fontsize='30')
plt.yticks(fontsize=20)
plt.legend(fontsize=20,fancybox=True, shadow=True).get_frame().set_edgecolor('lightgray')
#plt.ylim(-0.01,1.01)
#plt.xlim(-0.01,(((n-1)/n)+0.01))
plt.ylim(0.0,1.01)
plt.xlim(-0.01,1)
ax=plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(0.2))

#plt.show()

fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.tight_layout()
nome = ('Uffink.png')
plt.savefig(nome, dots=100)
plt.close(fig)

