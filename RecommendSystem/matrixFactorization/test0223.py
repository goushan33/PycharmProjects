import csv
from numpy import *




def compute_global_rmse(predict_data):
    test=[]
    with open("D:\\PycharmProjects\\RecommendSystem\\matrixFactorization\\mytestingSet.csv", 'r') as f:
        reader = csv.reader(f)#readline
        for line in reader:
            test.append(line)
        print(test)
    test = test[1:]
    squaredError_list=[]
    for i in test:
        error=predict_data[i[0]][i[1]]-float(i[2])
        squaredError = error * error
        squaredError_list.append(squaredError)
    return sum(squaredError_list)/len(squaredError_list)

predict_data=mat(random.random((4, 5)))
rmse=compute_global_rmse(predict_data)
print(rmse)