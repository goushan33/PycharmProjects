import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from scipy import sparse

movielist = pd.read_csv('D:/PycharmProjects/RecommendSystem/basicTaskPackage/trainingSet.csv',index_col=None)
head=movielist.head(5)
#print(movielist.describe())
row=head.userId
column=head.movieId
data=head.rating
c = sparse.csr_matrix((data, (row, column)))#construct a sparse matrix
print(c)
print (c.todense())#construct a full/dense matrix

