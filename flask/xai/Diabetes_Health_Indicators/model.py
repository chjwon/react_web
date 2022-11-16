from foldrm import *
from .getCSV import diabete_binary_5050split
def dh_model(inputData):
    print("inputData is: ",inputData)
    model, data = diabete_binary_5050split()
    data_train, data_test = split_data(data, ratio=0.8)
    model.fit(data_train, ratio=0.5)
    model.print_asp(simple=True)
    tempData=[0.0,1.0,0.0,1.0,26.0,0.0,0.0,0.0,1.0,0.0,1.0,0.0,1.0,0.0,3.0,5.0,30.0,0.0,1.0,4.0,6.0,8.0]
    
    inputData = tempData

    temp = model.proof(tempData)
    tempIndex = temp.index("is")
    print(temp[tempIndex+3])
    # 0 = no diabetes 1 = prediabetes 2 = diabetes
    return temp[tempIndex+3]


