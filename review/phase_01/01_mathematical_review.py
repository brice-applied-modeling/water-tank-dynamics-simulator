#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 01:11:51 2026

@author: brice-nelson
"""

# %% Module description
# Exercises meant to help provide refresher and review math derivations.

# Phase 01: Mathematical Foundations Review
# Reference: docs/06_learning/01_phase_01_mathematical_review.md

# %% Imports
import sympy as sp
from sympy import Symbol, Derivative



# %% 1. Derivatives

# Exercise 1
# Evaluate 3x**2 + 5x - 4

x = Symbol('x')
Sx = 3*x**2 + 5*x - 4

d = Derivative(Sx, x)

# use *.doit() function to evaluate
print(f'Exercise 1 = {d.doit()}')


# Exercise 2
# Evaluate t^(1/2) + 6

t =  Symbol('t')

St = t**(1/2) + 6

der = Derivative(St, 't')
print(f'Exercise 2 = {der.doit()}')

# Exercise 3
# Evaluate (5 - 2s)^2

a = Symbol('a')
Sa = 25 - 4*a + 4*a**2

derivative = Derivative(Sa, 'a')
print(f'Exercise 3 = {derivative.doit()}')


# Exercise 4
# Evaluate e^(-0.2b)

b = Symbol('b')
Sb = sp.E**(-0.2*b)

deriv = Derivative(Sb, 'b')
print(f'Exercise 4 = {deriv.doit()}')



# %% 2. Initial-value problems

# Exercise 1


# %% 3. Separable ordinary differential equations


# %% 4. Indefinite integration


# %% 5. Definite integration


# %% 6. Engineering applications


# %% 7. Findings and observations