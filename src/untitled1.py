# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 21:37:41 2022

@author: ashay
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 10:30:38 2022

@author: ashay
"""
train_acc_list = []
val_acc_list = []
test_acc_list = []
with open("Vis_data/fold_data_20/train_data/train_acc_data.txt", "r") as f:
  for line in f:
    train_acc_list.append(float(line.strip()))
f.close()

with open("Vis_data/fold_data_20/train_data/val_acc_data.txt", "r") as f:
  for line in f:
    val_acc_list.append(float(line.strip()))
f.close()

with open("Vis_data/fold_data_20/train_data/test_acc_data.txt", "r") as f:
  for line in f:
    test_acc_list.append(float(line.strip()))
f.close()



train_1 = train_acc_list
val_1 = val_acc_list
test_1 = test_acc_list
print("Highest Train Acc: ", max(train_acc_list))
print("Highest Test Acc: ", max(test_acc_list))
print("Highest Val Acc: ", max(val_acc_list))
print("Train acc: ", train_acc_list.index(91.22234123148462))
print("Test acc: ", test_acc_list.index(93.79453681710214))
print("Val acc: ", val_acc_list.index(91.7352209680505))
for i in range(20):   
    train_acc_list = train_1
    val_acc_list = val_1
    test_acc_list = test_1
    if i <= 7:
        start = i*150
        stop = (i+1)*150        
    else:
        if i == 8:
            start = 1200
            stop = 1315
        elif i == 9:
            start = 1315
            stop = 1447
        elif i == 10:
            start = 1448
            stop = 1597
        elif i == 11:
            start = 1598
            stop = 1744
        elif i == 12:
            start = 1746
            stop = 1894
        elif i == 13:
            start = 1895
            stop = 2044
        elif i == 14:
            start = 2045
            stop = 2178
        elif i == 15:
            start = 2179
            stop = 2313
        elif i == 16:
            start = 2314
            stop = 2442
        elif i == 17:
            start = 2443
            stop = 2535
        elif i == 18:
            start = 2536
            stop = 2659
        elif i == 19:
            start = 2660
            stop = 2810
            
    
    print("Start: ", start)
    print("Stop: ", stop)
    train_acc_list = train_acc_list[start:stop]
    val_acc_list = val_acc_list[start:stop]
    test_acc_list = test_acc_list[start:stop]
    acc_epoch =[]
    for j in range(len(train_acc_list)):
        acc_epoch.append(j)
    import matplotlib.pyplot as acc_plt
    plt_title = "Accuracy Fold " + str(i)
    acc_plt.title(plt_title)
    acc_plt.ylabel('Accuracy')
    acc_plt.xlabel('Epoch')
    acc_plt.plot(acc_epoch,train_acc_list,color = 'r', label="Train Accuracy")
    acc_plt.plot(acc_epoch,test_acc_list, color = 'g', label="Test Accuracy")
    acc_plt.plot(acc_epoch,val_acc_list, color = 'cyan', label="Validation Accuracy")
    acc_plt.legend(loc='lower right')
    acc_plt.show()