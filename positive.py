# -*- coding: utf-8 -*-
"""
Created on Sat May  2 08:13:13 2020

@author: Veena
"""
# Python program to print positive Numbers in a List 
list = [12, -7, 5, 64, -14]  
num = 0
# using while loop      
while(num < len(list)):  
    if list[num] >= 0: 
        print(list[num],",", end = " ") 
    num += 1