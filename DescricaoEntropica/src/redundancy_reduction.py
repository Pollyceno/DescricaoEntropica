
import numpy as np
import gurobipy as gp
#mport time



def elimina_redundancia(A, B):
    print('Inicial:', len(A))

    # RETIRA DESIGUALDADES REPETIDAS
    A = np.unique(A, axis = 0)
    B = np.zeros((len(A)))
    #B = np.reshape(B, (len(B))) #Transpondo para o gurobi

    #print('Após eliminar red triviais:', len(A))
    cont=0
    c=0
    n=len(A)
    l=0
    print('Aplicando o lema', len(A))
    row=0
    while (row <= len(A)-1):
        if(type(n)==type(1)):
            por = int((cont/n)*100)
            cont=cont+1
            #print('Porcentagem:', por, '%')

        # SEPARANDO DESIGUALDADE A SER TESTADA
        a_row = A[row][:]
        b_row = B[row]
        A_row = np.delete(A, (row), axis = 0)
        B_row = np.delete(B, (row), axis = 0)

        # MONTANDO MODELO
        prob = gp.Model()
        h = prob.addMVar(len(A[0]), lb=-gp.GRB.INFINITY,ub=gp.GRB.INFINITY )
        prob.setObjective(a_row @ h, gp.GRB.MAXIMIZE)
        prob.addConstr(A_row @ h <= B_row)
        prob.update()
        prob.setParam('OutputFlag',False)

        prob.optimize()

        atol=10**-8
        # E FACTIVEL?
        if((prob.Status == 2)): 
            #print(prob.ObjVal)
            # Se cumpre o lema, ELIMINA
            if(prob.ObjVal<atol):
                A = A_row
                B = B_row
            # Se NAO cumpre o lema, NAO elimina
            else:
                row = row + 1
        #Se NAO e factivel, NAO cumpre o lema, NAO elimina
        else: 
            #print(prob.ObjVal)
            row = row + 1  
        c=c+1
    #print('Apos reducao:', len(A))
    #Normalizando
    B = np.reshape(B, (np.size(B),1)) #Transpondo o vetor para poder entrar na funcao Fourier Motzkin
    
    #RENORMALIZANDO
    H_max=np.amax(abs(A),axis=1)
    A=np.dot(np.diag(1/H_max),A)
    B=np.dot(np.diag(1/H_max),B)

    return (A, B)

def testa_redundancia(ineq, b, A, B):
    
    if(len(A)!=0):
        #print("Atual:", len(A))
        B = np.reshape(B, (len(B))) #Transpondo para o gurobi
        b = np.reshape(b, (len(b))) #Transpondo para o gurobi
    
        #t1 = time.time()
        prob = gp.Model()
        h = prob.addMVar(len(A[0]), lb=-gp.GRB.INFINITY,ub=gp.GRB.INFINITY )
        prob.setObjective(ineq @ h, gp.GRB.MAXIMIZE)
        prob.addConstr(A @ h <= B)
        prob.update()
        prob.setParam('OutputFlag',False)
        prob.optimize()
        #print("Linear Prog----%s segundos----" %(time.time()-t1))
    
        atol=10**-8
        B = np.reshape(B, (np.size(B),1)) #Transpondo o vetor para poder entrar na funcaoourier Motzkin
        b = np.reshape(b, (np.size(b),1)) #Transpondo o vetor para poder entrar na funcaoourier Motzkin
        if((prob.Status == 2)): #Se e factivel
            #print(prob.ObjVal)
            if(prob.ObjVal>=atol): # Se NAO cumpre o lema, NAO elimina
                #print("Não")
                A=np.vstack((A,ineq))
                B=np.vstack((B,b))
            #else:
                #print("Sim")
        else:# Se NAO e factivel, NAO cumpre o lema, NAO elimina 
            #print("Não2")
            A=np.vstack((A,ineq))
            B=np.vstack((B,b))
    
    #Nesse caso nao tem core pra rodar o lema, apenas resta concatenar a matriz
    else:
        A=np.vstack((A,ineq))
        B=np.vstack((B,b))
        
    return (A, B)
