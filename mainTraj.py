# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:44:56 2023

@author: student
"""
import numpy as np
import random as rng
from particleTraj import *



def makeCon():
    N = 10
    
    f = open("initial_conditions.txt", 'w')
    
    for i in range(N):
        linestr = ""
        for j in range(6):
            linestr += (str((rng.random() - 0.5) * 100) + ", ")
        
        linestr += str(1000)
        linestr += "\n"
        
        f.write(linestr)
    
    f.close()
def doData(filePath):
    raw_data = open(filePath, 'r') 
    input_str = raw_data.read()
    input_array = input_str.split('\n')
    data = [input_array[i].split(',') for i in range(len(input_array))]
    for i in range(len(data) - 1):
        print(data[i])
        for j in range(len(data[0])):
            if data[i][j] == '':
                data[i][j] = float(0)
            else:     
                data[i][j] = float(data[i][j])
    data = data[:len(data) - 1]
    return data



def putInClass(arr):
    particleData = []
    for i in range(len(arr)):
        particleData.append(Particles(arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[i][4], arr[i][5], arr[i][6]))
    return particleData

output = doData('initial_conditions.txt')
final = putInClass(output)




        