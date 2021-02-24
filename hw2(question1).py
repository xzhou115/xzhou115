# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 19:50:13 2020

@author: Administrator
"""

#Q1
#Use dictionary comprehension to create a dictionary where keys are alphabets upper cases and corresponding values are their ascii decimal code respectively
d1={chr(65+i):65+i for i in range(26)}
##Use dictionary comprehension to create a dictionary where keys are alphabets lower cases and corresponding values are their ascii decimal code respectively
d2={chr(97+i):97+i for i in range(26)}
#Two dictionary connection
d1.update(d2)
#Output result
print('The answer of q1 is:\n', d1)