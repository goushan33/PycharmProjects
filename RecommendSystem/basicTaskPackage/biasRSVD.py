'''
@2019/3/21
@gou shan
@hkust
'''

from numpy import *
import numpy as np
import pandas as pd
from scipy import sparse

'''
加入正则项的奇异值分解:RSVD
'''
#load data==========================================
def load_data(path):
    data = pd.read_csv(path, index_col=None)
    np.seterr(divide='ignore', invalid='ignore')
    return data

#create user-item matrix===========================
def create_ui_matrix(data):
    row = data.userId
    column = data.movieId
    rating = data.rating
    ui_sparse_metrix= sparse.csr_matrix((rating, (row, column)))  # construct a sparse matrix
    ui_metrix=ui_sparse_metrix.todense()
    return ui_metrix

#iterate matrix p,q=================================
def ratingPredict(data, K):
    print(data)
    m, n = shape(data)
    p = mat(random.random((m, K)))#randomly produce matrix p(m*K)
    q = mat(random.random((K, n)))#randomly produce matrix q(K*n)

    alpha = 0.0002
    beta = 0.02
    maxCycles = 10000

    for step in range(maxCycles):
        for i in range(m):
            for j in range(n):
                if data[i,j] > 0:#non-zero values
                    error = data[i,j]
                    for k in range(K):
                        error = error - p[i,k]*q[k,j]
                    for k in range(K):
                        p[i,k] = p[i,k] + alpha * (2 * error * q[k,j] - beta * p[i,k])
                        q[k,j] = q[k,j] + alpha * (2 * error * p[i,k] - beta * q[k,j])

        loss = 0.0
        for i in range(m):
            for j in range(n):
                if data[i,j] > 0:
                    error = 0.0
                    for k in range(K):
                        error = error + p[i,k]*q[k,j]
                    loss = (data[i,j] - error) * (data[i,j] - error)
                    for k in range(K):
                        loss = loss + beta * (p[i,k] * p[i,k] + q[k,j] * q[k,j]) / 2

        if loss < 0.001:#if the loss between two adjacent iterations is smaller than 0.001:
            break
        if step % 1000 == 0:
            print(loss)

    return p, q

#compute rmse================================
def compute_rmse(soure_data,res_data):
    m,n=shape(soure_data)
    rmse=[]
    for i in range(m):
        for j in range(n):
            error=res_data[i,j]-soure_data[i,j]
            squaredError=error*error
            squaredError+=squaredError
        r=sqrt(squaredError/n)
        rmse.append(r)
    print(rmse)

#main function=============================
if __name__ == "__main__":
    data= load_data('D:/PycharmProjects/RecommendSystem/matrixFactorization/mytestingSet.csv')
    dataMatrix=create_ui_matrix(data)
    p, q = ratingPredict(dataMatrix, 5)
    result = p * q
    print(result)
    compute_rmse(dataMatrix,result)
