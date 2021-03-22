import numpy as np
import gurobipy as gp
#import time
import random


def elimina(vetor_H, i, A, C, d, bound):
    print('Inicial:', len(A))

    B =np.zeros((len(A))) 

    print('Encontrando i:')

    c = np.zeros(len(A[0]))
    c[i] = 1 # negativo porque os sinais estao trocados e ser um problema equivamente a minimizacao  

    cont=0
    n=len(A)

    matriz_desig = []

    l=0
    print('Rodando otimizacao', len(A))
    aux=0

    while (aux <= len(A)-1):
        if(type(n)==type(1)):
            por = int((cont/n)*100)
            cont=cont+1
            print('Porcentagem:', por, '%')

        row = random.randint(0,(len(A)-1)) 

        a_row = A[row][:]
        b_row = B[row]
        A_row = np.delete(A, (row), axis = 0)
        B_row = np.delete(B, (row), axis = 0)

        #A_row = A
        #B_row = B

        #t1 = time.time()
        prob = gp.Model()
        h = prob.addMVar(len(A[0]), lb=-gp.GRB.INFINITY,ub=gp.GRB.INFINITY )
        prob.setObjective(c@h, gp.GRB.MINIMIZE)
        prob.addConstr((-A_row) @ h >= B_row)
        
        prob.addConstr((C@h) == d)
        j=0
        '''
        for k in C:
            prob.addConstr(h[vetor_H.index(k)] == d[j])
            j = j +1
        '''
        prob.update()
        prob.setParam('OutputFlag',False)
        
        prob.optimize()
        
        #print(prob.Status)
        atol=10**-8
        if((prob.Status == 2)):
            print(prob.ObjVal)
            if(prob.ObjVal-bound>=atol):
                A = A_row
                B = B_row
                '''
                if(len(matriz_desig)==0):
                    matriz_desig = np.array([a_row])
                else:
                    matriz_desig = np.vstack([matriz_desig, a_row])
                aux = aux + 1
                '''
            else:
                aux = aux + 1
        else:
            #print(prob.ObjVal)
            aux = aux + 1  
    print('Apos reducao:', len(A))
    #Normalizando
    '''
    B = np.reshape(B, (np.size(B),1)) #Transpondo o vetor para poder entrar na funcaoourier Motzkin
    
    H_max=np.amax(abs(A),axis=1)
    A=np.dot(np.diag(1/H_max),A)
    B=np.dot(np.diag(1/H_max),B)
    '''
    return A