# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:36:24 2022

@author: ashay
"""

test = [0,1,2,3,4,5,6,7,8,9,10,11]

test = test[:5]
print(test)

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

predict_acc_list = []
predict_f1_list = []

with open("Vis_data/predict_acc_data.txt", "r") as f:
  for line in f:
    predict_acc_list.append(float(line.strip()))
f.close()

with open("Vis_data/predict_f1_data.txt", "r") as f:
  for line in f:
    predict_f1_list.append(float(line.strip()))
f.close()

barWidth = 0.25
ax,fig = plt.subplots(figsize =(12,8))

br1 = np.arange(len(predict_acc_list))
br2 = [x + barWidth for x in br1]

plt.bar(br1, predict_acc_list, color='r', width = barWidth, edgecolor = 'grey', label= 'Accuracy')
plt.bar(br2, predict_f1_list, color='b', width = barWidth, edgecolor = 'grey', label= 'F1 Score')

ax.bar_label(ax.containers[0])

plt.xlabel('Subjects', fontweight = 'bold')
plt.ylabel('Performance (Percentage)', fontweight = 'bold')

plt.xticks([r + barWidth for r in range(len(predict_acc_list))],['Subject 1','Subject 2','Subject 3','Subject 4','Subject 5'])
plt.legend()
plt.show()