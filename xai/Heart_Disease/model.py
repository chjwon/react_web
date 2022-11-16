from foldrm import *
from getCSV import heart_disease

def hd_model():
    model, data = heart_disease()
    data_train, data_test = split_data(data, ratio=0.8)
    model.fit(data_train, ratio=0.5)


    model.print_asp(simple=True)
    # Y = [d[-1] for d in data_test]
    # Y_test_hat = model.predict(data_test)
    # acc = get_scores(Y_test_hat, data_test)
    # print('% acc', round(acc, 4), '# rules', len(model.crs))
    # acc, p, r, f1 = scores(Y_test_hat, Y, weighted=True)
    # print('% acc', round(acc, 4), 'macro p r f1', round(p, 4), round(r, 4), round(f1, 4), '# rules', len(model.crs))


    tempData = [52,1,0,125,212,0,1,168,0,1,2,2,3,0]
    # print("11111")
    # print(type(model.explain(tempData)))
    # print(model.explain(tempData))

    # print(model.proof(tempData))
    temp = model.proof(tempData)
    tempIndex = temp.index("is")
    print("val of thal is:",temp[tempIndex+3])
    # thal is thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
    return temp[tempIndex+3]

hd_model()