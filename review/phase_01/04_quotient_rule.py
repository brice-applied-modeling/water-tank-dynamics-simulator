#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 01:37:50 2026

@author: brice-nelson
"""

import sympy as sp

def calculate_power_derivative(function: str, variable: str, arg: int | float) -> dict:
    """
    Calculates the derivative of a single function using the power rule.

    Parameters
    ----------
    function : str
        Single simplified function that is eligible for evaluation using the
        power rule.
    variable : str
        The independent variable used in the provided function.
    arg : int | float
        Argument to evaluate the derivative.

    Returns
    -------
    dict
        expression: str
            The returned expression of the derivative using the power
            rule with regards to the independent variable.
        result: int | float
            The numeric value of the calculated derivative using the
            power rule with regards to the provided argument to evaluate
            the function.
            
    Raises
    ------
    ValueError
        If the provided mathematical expression is invalid.
    """
    pass


def calculate_quotient_rule(numerator: str, denominator: str, variable:str, arg: int | float) -> dict:
    """
    Calculates the derivative of a function using the quotient rule.

    Parameters
    ----------
    numerator : str
        Numerator of the expression, v(x).
    denominator : str
        Denominator of the expression, u(x).
    variable : str
        Independent variable.
    arg : int | float
        Argument to evaluate the derivative.

    Returns
    -------
    dict:
        expression: str
            The returned expression of the derivative using the quotient
            rule with regards to the independent variable.
        result: int | float
            The numeric value of the calculated derivative using the
            quotient rule with regards to the provided argument to evaluate
            the expression.
            
    Raises
    ------
    ZeroDivisionError
        If the original denominator evaluates to zero at
        the provided argument.
    ValueError
        If the provided mathematical expression is invalid.
    """
    pass
