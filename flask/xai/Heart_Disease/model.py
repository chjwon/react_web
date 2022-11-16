from foldrm import *
from .getCSV import heart_disease


def hd_model(inputData):
    model, data = heart_disease()
    data_train, data_test = split_data(data, ratio=0.8)
    model.fit(data_train, ratio=0.5)
    model.print_asp(simple=True)
    tempData = [52,1,0,125,212,0,1,168,0,1,2,2,3,0]

    inputData = tempData
    
    temp = model.proof(inputData)
    tempIndex = temp.index("is")
    print("val of thal is:",temp[tempIndex+3])
    # thal is thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
    return temp[tempIndex+3]

