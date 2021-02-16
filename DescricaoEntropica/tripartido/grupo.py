from sympy.combinatorics import Permutation
from sympy.combinatorics.perm_groups import PermutationGroup
from sympy.combinatorics.named_groups import SymmetricGroup

import numpy as np
import copy

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
def permuta(p):
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    l5=[]
    l6=[]
    l7=[]
    l8=[]
    l9=[]
    l10=[]
    l11=[]
    for z in range(2):
        for c in range(2):
            for y in range(2):
                for b in range(2):
                    for x in range(2):
                        for a in range(2):
                            l1.append(ind322(b,a,c,y,x,z))
                            l2.append(ind322(a,c,b,x,z,y))
                            l3.append(ind322(a,b,c,(x+1)%2,y,z))
                            l4.append(ind322(a,b,c,x,(y+1)%2,z))
                            l5.append(ind322(a,b,c,x,y,(z+1)%2))
                            if x==0 :
                                l6.append(ind322((a+1)%2,b,c,0,y,z))
                                l7.append(ind322(a,b,c,x,y,z))
                            if x==1 :
                                l6.append(ind322(a,b,c,x,y,z))
                                l7.append(ind322((a+1)%2,b,c,1,y,z))
                            if y==1:
                                l8.append(ind322(a,b,c,x,y,z))
                                l9.append(ind322(a,(b+1)%2,c,x,1,z))
                            if z==1:
                                l10.append(ind322(a,b,c,x,y,z))
                                l11.append(ind322(a,b,(c+1)%2,x,y,1))
                            if y==0:
                                l8.append(ind322(a,(b+1)%2,c,x,0,z))
                                l9.append(ind322(a,b,c,x,y,z))
                            if z==0:
                                l10.append(ind322(a,b,(c+1)%2,x,y,0))
                                l11.append(ind322(a,b,c,x,y,z))
    p1=Permutation(l1)
    p2=Permutation(l2)
    p3=Permutation(l3)
    p4=Permutation(l4)
    p5=Permutation(l5)
    p6=Permutation(l6)
    p7=Permutation(l7)
    p8=Permutation(l8)
    p9=Permutation(l9)
    p10=Permutation(l10)
    p11=Permutation(l11)
    
    G=PermutationGroup(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)
    #G = SymmetricGroup(4)
    
    
    aux = copy.deepcopy(p)
    
    #print(G._elements)
    P = []
    t = True
    for g in G._elements:
        perm = [i^g for i in range(g.size)]
        
        pe = []
        for i in range(len(p)):
            pe.append(aux[perm[i]])
        
        #print(pe)
    
        if(t==True):
            P = np.array([pe])
            #print('a')
            t=False
        else:
            pq = np.array([pe])
            P = np.concatenate((P, pq), axis = 0)
            #rint('b')
        
        
        P = np.unique(P, axis = 0)
        #print(pe)
        
    
    #print(P)
    #print(len(P))
    #print(G.order())

    return P