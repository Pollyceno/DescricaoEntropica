import random
import math
import numpy as np
import itertools as itt


def marginalizacao(P, marg):
	n =P.ndim
	x=np.arange(n)
	
	elim = np.delete(x, marg)
	elim = np.sort(elim)[::-1].astype(int)
	#print(elim)
	
	for i in elim:
		P = P.sum(axis=i,dtype='float')
	
	return P