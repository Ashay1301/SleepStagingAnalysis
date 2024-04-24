# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:04:40 2022

@author: ashay
"""

train_acc_list = []
train_loss_list = []
train_f1_list = []
val_acc_list = []
val_loss_list = []
val_f1_list = []
test_acc_list = []
test_f1_list = []

with open("Vis_data/fold_data/train_data_fold_4/train_acc_data.txt", "r") as f:
  for line in f:
    train_acc_list.append(float(line.strip()))
f.close()

with open("Vis_data/fold_data/train_data_fold_4/test_acc_data.txt", "r") as f:
  for line in f:
    test_acc_list.append(float(line.strip()))
f.close()

with open("Vis_data/fold_data/train_data_fold_4/val_acc_data.txt", "r") as f:
  for line in f:
    val_acc_list.append(float(line.strip()))
f.close()

with open("Vis_data/fold_data/train_data_fold_4/test_f1_data.txt", "r") as f:
  for line in f:
    test_f1_list.append(float(line.strip()))
f.close()

with open("Vis_data/fold_data/train_data_fold_4/val_f1_data.txt", "r") as f:
  for line in f:
    val_f1_list.append(float(line.strip()))
f.close()

with open("Vis_data/fold_data/train_data_fold_4/train_loss_data.txt", "r") as f:
  for line in f:
    train_loss_list.append(float(line.strip()))
f.close()

with open("Vis_data/fold_data/train_data_fold_4/val_loss_data.txt", "r") as f:
  for line in f:
    val_loss_list.append(float(line.strip()))
f.close()

train_acc_list = train_acc_list[:150]
test_acc_list = test_acc_list[:150]
val_acc_list = val_acc_list[:150]
train_f1_list = train_f1_list[:150]
test_f1_list = test_f1_list[:150]
val_f1_list = val_f1_list[:150]
train_loss_list = train_loss_list[:150]
val_loss_list = val_loss_list[:150]

acc_epoch =[]
for i in range(len(train_acc_list)):
    acc_epoch.append(i)
    
f1_epoch =[]
for i in range(len(test_f1_list)):
    f1_epoch.append(i)
    
loss_epoch =[]
for i in range(len(train_loss_list)):
    loss_epoch.append(i)
    
import matplotlib.pyplot as acc_plt
acc_plt.title('Accuracy Fold 4')
acc_plt.ylabel('Accuracy')
acc_plt.xlabel('Epoch')
acc_plt.plot(acc_epoch,train_acc_list,color = 'r', label="Train Accuracy")
acc_plt.plot(acc_epoch,test_acc_list, color = 'g', label="Test Accuracy")
acc_plt.plot(acc_epoch,val_acc_list, color = 'cyan', label="Validation Accuracy")
acc_plt.legend(loc='lower right')
acc_plt.show()

import matplotlib.pyplot as f1_plt
f1_plt.title('F1 Score Fold 4')
f1_plt.ylabel('F1 Score')
f1_plt.xlabel('Epoch')
#f1_plt.plot(f1_epoch,train_f1_list,color = 'r', label="F1 Train")
f1_plt.plot(f1_epoch,test_f1_list, color = 'black', label="F1 Test")
f1_plt.plot(f1_epoch,val_f1_list, color = 'orange', label="F1 Validation")
f1_plt.legend(loc='lower right')
f1_plt.show()

import matplotlib.pyplot as loss_plt
loss_plt.title('Loss Fold 4')
loss_plt.ylabel('Loss')
loss_plt.xlabel('Epoch')
loss_plt.plot(loss_epoch,train_loss_list,color = 'r', label="Train Loss")
#loss_plt.plot(acc_epoch,test_acc_list, color = 'g', label="Test Accuracy")
loss_plt.plot(loss_epoch,val_loss_list, color = 'b', label="Validation Loss")
loss_plt.legend(loc='upper right')
loss_plt.show()

print("Highest Train Acc: ", max(train_acc_list))
print("Highest Test Acc: ", max(test_acc_list))
print("Highest Val Acc: ", max(val_acc_list))
print("Highest Test F1: ", max(test_f1_list))
print("Highest Val F1: ", max(val_f1_list))
print("Lowest Train loss: ", min(train_loss_list))
print("Lowest Val Loss: ", min(val_loss_list))