import pandas as pd
import numpy as np
testing= pd.read_csv('D:/PycharmProjects/RecommendSystem/basicTaskPackage/mytestingSet.csv', index_col=None)
userToTest=np.unique(testing.userId)
