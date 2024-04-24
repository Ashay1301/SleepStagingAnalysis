# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 17:01:34 2022

@author: ashay
"""

a = [1,2,3,4,5,6]
b = len(a)
print(b)
    
#textfile = open("file.txt", "w")

with open("Vis_data/file.txt", "w") as f:
    for s in a:
        f.write(str(s) +"\n")
def send_a():
    a_send = a
    return a_send