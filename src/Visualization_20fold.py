# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 09:50:02 2022

@author: ashay
"""

train_time_list = []


with open("Vis_data/fold_data_20/train_data/train_time_data.txt", "r") as f:
  for line in f:
    train_time_list.append(float(line.strip()))
f.close()



train_1 = train_time_list

for i in range(19):
   
    train_time_list = train_1
    start = i*150
    stop = (i+1)*150
    print("Start: ", start)
    print("Stop: ", stop)
    train_time_list = train_time_list[start:stop]
    print("List of ",i," : ",train_time_list)
    acc_epoch =[]
    for j in range(len(train_time_list)):
        acc_epoch.append(j)
    import matplotlib.pyplot as time_plt
    plt_title = "Time fold " + str(i)
    time_plt.title(plt_title)
    time_plt.ylabel('Time(sec)')
    time_plt.xlabel('Epoch')
    time_plt.plot(acc_epoch,train_time_list,color = 'r', label="Train Time")
    
    time_plt.legend(loc='lower right')
    time_plt.show()
        


    

    


