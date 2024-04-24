# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 03:18:20 2022

@author: ashay
"""

import numpy as np
cf_matrix = np.loadtxt("Vis_data/fold_data_20/CM_fold5.txt", dtype='i',delimiter=' ')
print(input)

import seaborn as sns
import matplotlib.pyplot as plt

ax = sns.heatmap(cf_matrix/np.sum(cf_matrix), annot=cf_matrix, cmap='Blues')
print("Hello")

ax.set_title('Confusion Matrix fold_4\n\n');
ax.set_xlabel('\nPredicted Sleep Stages')
ax.set_ylabel('Actual Sleep Stages');

## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['W','N1', 'N2', 'N3', 'REM'])
ax.yaxis.set_ticklabels(['W','N1', 'N2', 'N3', 'REM'])

## Display the visualization of the Confusion Matrix.
plt.show()