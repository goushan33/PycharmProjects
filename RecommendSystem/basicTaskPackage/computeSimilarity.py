from scipy import sparse
import numpy as np
import pandas as pd
np.seterr(divide='ignore', invalid='ignore')

def compute_similarity(data):
    # construct user-item metrix
    row = data.userId
    column = data.movieId
    data = data.rating
    user_item_metrixs = sparse.csr_matrix((data, (row, column)))# construct a sparse matrix
    user_item_metrixs_full=user_item_metrixs.todense()
    #user_item_array = user_item_metrixs.toarray()
    # p = 2，则所得的 2-范数是向量的模或欧几里德长度。
    norm_x=np.linalg.norm(user_item_metrixs_full,ord=2,axis=0,keepdims=True)#计算每一列的范数。
    norm_y=(np.linalg.norm(user_item_metrixs_full,ord=2,axis=1,keepdims=True)).T#计算每一行的范数。
    user_simi=(user_item_metrixs_full*user_item_metrixs_full.T)/(norm_y.T*norm_y)
    item_simi=(user_item_metrixs_full.T*user_item_metrixs_full)/(norm_x.T*norm_x)
    print(user_simi)
    print(item_simi)



# main function:
data= pd.read_csv('D:/PycharmProjects/RecommendSystem/basicTaskPackage/mytestingSet.csv', index_col=None)
d = compute_similarity(data)
