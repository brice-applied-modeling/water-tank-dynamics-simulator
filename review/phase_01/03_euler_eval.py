#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 22:42:38 2026

@author: brice-nelson
"""

import sympy as sp

h = sp.Symbol('h')

f1 = (sp.exp(-0.2*h) - 1) / h

f2 = (sp.exp(-0.2*h) - 1) / (-0.2*h)

print(f'function f1: {sp.limit(f1, h, 0)}')
print(f'function f2: {sp.limit(f2, h, 0)}')