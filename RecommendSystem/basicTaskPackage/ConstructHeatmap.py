import pandas as pd
from matplotlib import pyplot as plt
from scipy import sparse

'''
use heatmap to print out the rating for first 20 users over first 30 movies
GOUSHAN 20190309

'''
def draw(data):
    #construct the first 20 user list and first 30 movie list
    user20 = list(data.head(20).userId)
    movie30=list(data.head(30).movieId)
    user20.sort()
    movie30.sort()

    # construct user-item metrix
    row = data.userId
    column = data.movieId
    data = data.rating
    user_item_metrixs = sparse.csr_matrix((data, (row, column)))  # construct a sparse matrix
    user_item_array = user_item_metrixs.toarray()

    # define the axis for heatmap
    xLabel = user20
    yLabel = movie30

    #find the axis range
    max_x=max(user20)
    min_x=min(user20)
    max_y=max(movie30)
    min_y=min(movie30)
    #print(min_x,max_x,min_y,max_y)

    #find the correlated rating in user-item metrix and construct array
    result_arr=[]
    for m in movie30:
        res = []
        for u in user20:
            res.append(user_item_array[u][m])
        result_arr.append(res)

    # draw process
    fig = plt.figure()
    # Define the canvas as 1*1 division and plot it in the first position
    ax = fig.add_subplot(111)
    # seting the axis
    ax.set_yticks(range(len(yLabel)))
    ax.set_yticklabels(yLabel)
    ax.set_xticks(range(len(xLabel)))
    ax.set_xticklabels(xLabel)

    # Draw and select the color fill style of the heat map, select the hot one here
    im = ax.imshow(result_arr, cmap=plt.cm.hot_r)
    #add coordinates description
    plt.xlabel("User-Id")
    plt.ylabel("Movie-Id")
    # add the color scale bar on the right
    plt.colorbar(im)
    # add title for the map
    plt.title("user-movie heatmap")
    # show
    plt.show()


# main function:
data= pd.read_csv('D:/PycharmProjects/RecommendSystem/basicTaskPackage/trainingSet.csv', index_col=None)
d = draw(data)