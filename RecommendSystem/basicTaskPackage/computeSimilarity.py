from scipy import sparse
import numpy as np
import pandas as pd
import heapq

def compute_similarity(data):
    # construct user-item metrix
    row = data.userId
    column = data.movieId
    data = data.rating
    user_item_metrixs = sparse.csr_matrix((data, (row, column)))# construct a sparse matrix
    user_item_metrixs_full=user_item_metrixs.todense()
    #user_item_array = user_item_metrixs.toarray()
    # oder=2。
    norm_x=np.linalg.norm(user_item_metrixs_full,ord=2,axis=0,keepdims=True)#norm of each column
    norm_y=(np.linalg.norm(user_item_metrixs_full,ord=2,axis=1,keepdims=True)).T#norm of each row
    u=(user_item_metrixs_full*user_item_metrixs_full.T)/(norm_y.T*norm_y)#user-user similarity
    i=(user_item_metrixs_full.T*user_item_metrixs_full)/(norm_x.T*norm_x)#item-item similarity
    user_simi=np.delete(np.delete(u,0,axis=0),0,axis=1)#delete the first row and first column
    item_simi=np.delete((np.delete(i,0,axis=0)),0,axis=1)#delete the first row and first column
    return user_simi

# main function========================================================================
#load training/testing data============================================================
training= pd.read_csv('D:/PycharmProjects/RecommendSystem/basicTaskPackage/mytestingSet.csv', index_col=None)
testing= pd.read_csv('D:/PycharmProjects/RecommendSystem/basicTaskPackage/mytestingSet.csv', index_col=None)
np.seterr(divide='ignore', invalid='ignore')
user_sim=compute_similarity(training)
height=user_sim.shape
#set diagonal value =0
for i in range(height[0]):
    user_sim[i,i]=0
sim_score=np.sort(user_sim,axis=1)#don't support 'desc'!Complicated!!!!
neighbor=np.argsort(user_sim, axis=1)

'''
print(user_sim)
print(sim_score)
print(neighbor)
'''



def findneigbors(k,user,movieToRating,user_item_metrixs_full):
    predict_rating=0
    for i in range(k):
        fenzi=0
        fenmu=0
        #sim[user-1,sim_sort[user-1,-1-i]]*user_item_metrixs_full[sim_sort[user-1,-1-i]]

#print(np.argmax(sim,1) )
#print(np.max(sim,1) )
'''
userToTest=np.unique(testing.userId)
for user in userToTest:
    print(sim[user-1, :])
'''
