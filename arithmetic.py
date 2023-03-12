# Copyright 2023 David Senack

import numpy as np

# Addition functions

def dyadic_add(a, b):
    ''' Add two arrays together.'''
    return np.add(a, b)

def monadic_add(a):
    ''' Convert every value in an array to its postive value.'''
    return np.positive(a)

# Subtraction functions

def dyadic_sub(a, b):
    ''' Subtract two arrays together.'''
    return np.subtract(a, b)

def monadic_sub(a):
    ''' Convert every value in an array to its negative value.'''
    return np.negative(a)

# Multiplication functions

def dyadic_mul(a, b):
    ''' Multiply two arrays together.'''
    return np.multiply(a, b)

def monadic_mul(a):
    ''' Return a one for every value in an array.'''
    return np.ones_like(a)

# Division functions

def dyadic_div(a, b):
    ''' Divide two arrays together.'''
    return np.divide(a, b)

def monadic_div(a):
    ''' Return the inverse of every value in an array.'''
    a.astype(np.float64)
    return np.reciprocal(a)