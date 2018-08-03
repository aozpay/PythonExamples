# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 01:00:42 2018

@author: alican
"""

liste = list(range(1,100))       

liste3 = [i for i in liste if i%2 == 0]
print(liste3)