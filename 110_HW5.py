#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:17:02 2024

@author: iwatashun
"""

#1
import numpy as np
import sympy as sp

x = {}
x['x0'] = np.array([[3],[-1],[0],[1]])

x1, x2, x3, x4 = sp.symbols('x1 x2 x3 x4')

def f(x):
    return (x[0] + 10* x[1])**2 + 5*(x[2]-x[3])**2 + (x[1] - 2*x[2])**4 + 10*(x[0]-x[3])**4

f_0 = (x1 + 10*x2)**2 + 5*(x3 - x4)**2 + (x2 - 2*x3)**4 + 10*(x1 - x4)**4

#gradient function
gradient = [sp.diff(f_0, var) for var in (x1, x2, x3, x4)]

f_1 = sp.lambdify(x1, gradient[0])
f_2 = sp.lambdify(x2, gradient[1])
f_3 = sp.lambdify(x3, gradient[2])
f_4 = sp.lambdify(x4, gradient[3])

def gradient_f(x):
    y1 = f_1(x[0])
    y2 = f_2(x[1])
    y3 = f_3(x[2])
    y4 = f_4(x[3])
    return np.array([[y1], [y2], [y3], [y4]])

# Hessien = {}

# for var in (x1,x2,x3,x4):
#     g = sp.diff(f_0, var)
#     for var_2 in (x1,x2,x3,x4):
#         Hessien[f'f_{var}{var_2}'] = sp.lambdify(var, sp.diff(g,var_2))
        
def hessian_f(x):
    hessian = np.zeros((len(x), len(x)))
    for i in range(len(x)):
        for j in range(len(x)):
            hessian[i][j] = np.gradient(gradient_f(x), axis = 0)[i]
    return hessian
x = np.array([1, 2, 3, 4])
H = hessian_f(x)
print("Hessian matrix:")
print(H)
    
