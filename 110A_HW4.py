#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 16:46:03 2024

@author: iwatashun
"""

import numpy as np
import sympy as sp

x = {'x0': [4, 2, -1]}
x1, x2, x3 = sp.symbols('x1 x2 x3')

def g(x):
    return (x[0]-4)**4 + (x[1]-3)**2 + 4*((x[2]+5)**4)

f = (x1-4)**4 + (x2-3)**2 + 4*(x3+5)**4

#gradient function
gradient = [sp.diff(f, var) for var in (x1, x2, x3)]

f_0 = sp.lambdify(x1, gradient[0])
f_1 = sp.lambdify(x2, gradient[1])
f_2 = sp.lambdify(x3, gradient[2])

def gradient_f(x):
    y1 = f_0(x[0])
    y2 = f_1(x[1])
    y3 = f_2(x[2])
    return [y1, y2, y3]

def Secant(x_0,x_1,g):
    while abs(x_0-x_1)>=1e-6:
        x_1_2 = x_1
        x_1=(g(x_1)* x_0 - g(x_0)* x_1)/(g(x_1)-g(x_0))
        x_0 = x_1_2 
    return x_1


a = sp.symbols('a')
A = {'a-1': 1, 'a0': 2}
i = 0

while True:
    y0 = [a * j for j in gradient_f(x[f'x{i}'])]
    arr1 = np.array([y0,x[f'x{i}']])
    x0 = np.diff(arr1, axis = 0)
    x0 = x0.tolist()
    x0 = x0[0]
    
    
    i += 1
    
    f_for_secant = sp.diff(g(x0), a)
    f_for_secant = sp.lambdify(a, f_for_secant)
    A[f'a{i}'] = Secant(A[f'a{i-2}'], A[f'a{i-1}'], f_for_secant)
    y1 = [A[f'a{i}'] * j for j in gradient_f(x[f'x{i-1}'])]
    arr2 = np.array([y1,x[f'x{i-1}']])
    x[f'x{i}']  = np.diff(arr2, axis = 0)
    x[f'x{i}'] = x[f'x{i}'].tolist()
    x[f'x{i}'] = x[f'x{i}'][0]
    if (abs(g(x[f'x{i}'])-g(x[f'x{i-1}']))) <= 1e-6:
        print('minimizer at', x[f'x{i}'])
        break


