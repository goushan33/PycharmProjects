import random
from numpy import *
import numpy as np
import pandas as pd
from scipy import sparse
import csv

def LearningBiasLFM(train, F, maxCycles, alpha, beta, mu):
    '''

    :param train: train data
    :param F: latent pattern
    :param maxCycles:max times of iteration
    :param alpha:learning rate
    :param beta:
    :param mu:global mean
    :return:
    '''
    [bu, bi, p,q] = InitBiasLFM(train, F)
    m, n = shape(train)

    for step in range(maxCycles):
        for i in range(m):
            for j in range(n):
                if train[i,j]>0:
                    pui = Predict(i, j, p, q, bu, bi, mu)
                    eui = train[i, j] - pui
                    bu[i] += alpha * (eui - beta * bu[i])
                    bi[j] += alpha * (eui - beta * bi[j])
                    for k in range(0, F):
                        p[i, k] += alpha * (q[k, j] * eui - beta * p[i, k])
                        q[k, j] += alpha * (p[i, k] * eui - beta * q[k, j])
    return [bu, bi, p, q]



def InitBiasLFM(train, F):
    '''
    init p,q and bu,bi
    '''
    m, n = shape(train)
    p = mat(random.random((m, F)))  # randomly produce matrix p(m*K)
    q = mat(random.random((F, n)))  # randomly produce matrix q(K*n)
    bu=[0]*m
    bi=[0]*n
    return [bu,bi,p,q]

def Predict(u, i, p, q, bu, bi, mu):
    ret = mu + bu[u] + bi[i]
    ret += sum([p[u,f] * q[f,i] for f in range(0, len(p[u]))])
    return ret

def load_data(path):
    data = pd.read_csv(path, index_col=None)
    np.seterr(divide='ignore', invalid='ignore')
    return data

#create user-item matrix===========================
def create_ui_matrix(data):
    row = data.userId
    column = data.movieId
    rating = data.rating
    ui_sparse_matrix= sparse.csr_matrix((rating, (row, column)))  # construct a sparse matrix
    r1=ui_sparse_matrix.todense()
    r2=delete(r1,0,axis=0)#删除第一行
    ui_matrix=delete(r2,0,axis=1)#删除第一列
    return ui_matrix


def compute_global_rmse(test_data_path,predict_data):
    test=[]
    with open(test_data_path, 'r') as f:
        reader = csv.reader(f)#readline
        for line in reader:
            test.append(line)
        test = test[1:]
        squaredError_list=[]
        for i in test:
            error=predict_data[int(i[0]),int(i[1])]-float(i[2])
            squaredError = error * error
            squaredError_list.append(squaredError)
        return sum(squaredError_list)/len(squaredError_list)


#MAIN FUNCTION:
if __name__ == "__main__":
    data=load_data('D:/PycharmProjects/RecommendSystem/matrixFactorization/mytraining.csv')
    train_data=create_ui_matrix(data)
    row,col=shape(train_data)
    global_mean=np.sum(train_data)/(row*col)
    print(global_mean)
    [bu, bi, p, q]=LearningBiasLFM(train_data,5,10000,0.0002,0.02,global_mean)
    term=p*q

    for i in range(row):
        for j in range(col):
            term[i,j]+=bu[i]
    for j in range(col):
        for i in range(row):
            term[i,j]+=bi[j]
    res=global_mean+term

    global_rmse=compute_global_rmse('D:/PycharmProjects/RecommendSystem/matrixFactorization/mytesting.csv',res)

    print(train_data)
    print(bu)
    print(bi)
    print(term)
    print(res)
    print(global_rmse)