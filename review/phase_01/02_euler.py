#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 22:14:39 2026

@author: brice-nelson
"""

import sympy as sp

num = 0.1
x = sp.Symbol('x')
f = (sp.exp(-0.2*x) - 1) / (-0.2 * x)

result = f.subs(x, num)

print(f'\nEvaluate expression {f}, \nwhich yields: {result}')

