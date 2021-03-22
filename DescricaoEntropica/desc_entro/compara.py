#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 13:52:06 2018

@author: sadra
"""
import numpy as np
import gurobipy as gp
#import cvxpy as cp
#import time



def compara(verif, const): #Verifica quais desigualdades de verif NAO DECORREM de const

    print('Inicial:', len(verif))

    B_verif = np.zeros((len(verif)))
    B_const = np.zeros((len(const)))
    #B = np.reshape(B, (len(B))) #Transpondo para o gurobi

    cont=0
    n=len(verif)
    l=0
    print('Aplicando o lema', len(verif))
    row=0
    while (row <= len(verif)-1):
        if(type(n)==type(1)):
            por = int((cont/n)*100)
            cont=cont+1
            #print('Porcentagem:', por, '%')
        a_row = verif[row][:]
        b_row = B_verif[row]
        verif_row = np.delete(verif, (row), axis = 0)
        B_verif_row = np.delete(B_verif, (row), axis = 0)

        #t1 = time.time()
        prob = gp.Model()
        h = prob.addMVar(len(verif[0]), lb=-gp.GRB.INFINITY,ub=gp.GRB.INFINITY )
        prob.setObjective(a_row @ h, gp.GRB.MAXIMIZE)
        prob.addConstr(const @ h <= B_const)
        prob.update()
        prob.setParam('OutputFlag',False)
        prob.optimize()
        atol=10**-8
        #print(prob.Status, row)
        if((prob.Status == 2)):
            #print(prob.ObjVal)
            if(prob.ObjVal<atol): #Se cumpre o lema deleta
                #print(row)
                #row = row + 1
                verif = verif_row
                B_verif = B_verif_row
            else:
                row = row + 1
        else:
            #print(prob.ObjVal)
            row = row + 1
    #print('Apos reducao:', len(verif))
    #Normalizando
    
    B_verif = np.reshape(B_verif, (np.size(B_verif),1)) #Transpondo o vetor para poder entrar na funcaoourier Motzkin
    '''
    H_max=np.amax(abs(verif),axis=1)
    verif=np.dot(np.diag(1/H_max),verif)
    B_verif=np.dot(np.diag(1/H_max),B_verif)
    '''
    return (verif)


def compara2(verif, const): #Verifica quais desigualdades de verif DECORREM de const

    print('Inicial:', len(verif))

    B_verif = np.zeros((len(verif)))
    B_const = np.zeros((len(const)))
    #B = np.reshape(B, (len(B))) #Transpondo para o gurobi

    cont=0
    n=len(verif)
    l=0
    #print('Aplicando o lema', len(verif))
    row=0
    while (row <= len(verif)-1):
        if(type(n)==type(1)):
            por = int((cont/n)*100)
            cont=cont+1
            #print('Porcentagem:', por, '%')
        a_row = verif[row][:]
        b_row = B_verif[row]
        verif_row = np.delete(verif, (row), axis = 0)
        B_verif_row = np.delete(B_verif, (row), axis = 0)

        #t1 = time.time()
        prob = gp.Model()
        h = prob.addMVar(len(verif[0]), lb=-gp.GRB.INFINITY,ub=gp.GRB.INFINITY )
        prob.setObjective(a_row @ h, gp.GRB.MAXIMIZE)
        prob.addConstr(const @ h <= B_const)
        prob.update()
        prob.setParam('OutputFlag',False)
        prob.optimize()
        atol=10**-8
        #print(prob.Status, row)
        if((prob.Status == 2)):#Se cumpre o lema mantem
            #print(prob.ObjVal)
            if(prob.ObjVal<atol): #Se cumpre o lema mantem
                #print(row)
                row = row + 1
                #verif = verif_row
                #B_verif = B_verif_row
            else:# Se nao cumpe deleta
                #row = row + 1
                verif = verif_row
                B_verif = B_verif_row
        else:# Se nao cumpe deleta
            #print(prob.ObjVal)
            #row = row + 1
            verif = verif_row
            B_verif = B_verif_row
    #print('Apos reducao:', len(verif))
    #Normalizando
    B_verif = np.reshape(B_verif, (np.size(B_verif),1)) #Transpondo o vetor para poder entrar na funcaoourier Motzkin
    '''
    H_max=np.amax(abs(verif),axis=1)
    verif=np.dot(np.diag(1/H_max),verif)
    B_verif=np.dot(np.diag(1/H_max),B_verif)
    '''
    return (verif)

def dependencia(verif, const):

    B_const = np.zeros((len(const)))
    #B = np.reshape(B, (len(B))) #Transpondo para o gurobi

    cont=1
    n=len(verif)
    l=0
    print('Aplicando o lema', len(const))
    row=0
    while (row <= len(const)-1):
        const_row = np.delete(const, (row), axis = 0)
        B_const_row = np.delete(B_const, (row), axis = 0)
        #const_row = const
        #B_const_row = B_const
        #row = row + len(const)

        #t1 = time.time()
        prob = gp.Model()
        h = prob.addMVar(len(verif), lb=-gp.GRB.INFINITY,ub=gp.GRB.INFINITY )
        prob.setObjective(verif @ h, gp.GRB.MAXIMIZE)
        prob.addConstr(const_row @ h <= B_const_row)
        prob.update()
        prob.setParam('OutputFlag',False)
        '''
        if(cont == 1):
            print("Modelo----%s segundos----" %(time.time()-t1))
        t2 = time.time()
        '''
        prob.optimize()
        '''
        if(cont == 1):
            print("Optimize----%s segundos----" %(time.time()-t2))
        '''
        atol=10**-8
        #print(prob.Status, row)
        if((prob.Status == 2)):
            #print(prob.ObjVal)
            if(prob.ObjVal<atol):
                const = const_row 
                B_const = B_const_row # Se cumpre o lema, elimina. Pois pode ser obtida a partir das restantes
            else:
                row = row + 1 # Se NAO cumpre o lema, nao elimina. Pois ela e necessaria. Apenas passa para a proxima
                print(cont)
        else:
            row = row + 1 # Se NAO e activel, nao elimina. Pois ela e necessaria. Apenas passa para a proxima
            print(cont)

        cont = cont + 1
    print('Apos reducao:', len(const))
    B_const = np.reshape(B_const, (np.size(B_const),1)) #Transpondo o vetor para poder entrar na funcaoourier Motzkin
    '''
    #Normalizando
    H_max=np.amax(abs(verif),axis=1)
    verif=np.dot(np.diag(1/H_max),verif)
    B_verif=np.dot(np.diag(1/H_max),B_verif)
    '''
    return (const, B_const)

################################################################################################
##### COMPARA DUAS MATRIZES ######################################################################

'''
for i in range(0,len(A)):
    for j in range(0, len(desig_plane)):
        #print(np.equal(A[i], desig_plane[j]).all())
        if((np.equal(A[i], desig_plane[j]).all() == True)):
            print(i, j)
    #if(np.size(np.where((desig_plane == A[i]).all(axis=1)))    > 0):
    #print(np.where((desig_plane == A[i]).all(axis=1)))
    #print(A[i])
'''