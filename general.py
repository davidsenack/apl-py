''' General functions for the calculator.'''

import numpy as np
import arithmetic as ar

# General IO functions


def get_input():
    ''' Get input from the user.'''
    return input('>>> ')


def print_output(output):
    ''' Print output to the user.'''
    print(output)


def print_error(error):
    ''' Print error to the user.'''
    print(error)

# Parse functions


def parse_input(user_input):
    ''' Parse the user input.'''
    p_input = user_input.split(' ')
    arr_one = []
    arr_two = []

    # Place user entered arrays into lists
    # Need to refactor this later
    if len(p_input) == 2:
        for i in p_input[1]:
            if i.isdigit():
                arr_one.append(int(i))
    elif len(p_input) == 3:
        for i in p_input[0]:
            if i.isdigit():
                arr_one.append(int(i))
        for i in p_input[2]:
            if i.isdigit():
                arr_two.append(int(i))

    # convert lists to numpy arrays
    arr_one = np.array(arr_one)
    arr_two = np.array(arr_two)

    # Check for monadic or dyadic arithmetic function and return the appropriate function
    if p_input[0] == '+':
        return ar.monadic_add(p_input[1])
    elif p_input[0] == '-':
        return ar.monadic_sub(p_input[1])
    elif p_input[0] == '*':
        return ar.monadic_mul(p_input[1])
    elif p_input[0] == '/':
        return ar.monadic_div(p_input[1])
    elif p_input[1] == '+':
        return ar.dyadic_add(p_input[0], p_input[2])
    elif p_input[1] == '-':
        return ar.dyadic_sub(p_input[0], p_input[2])
    elif p_input[1] == '*':
        return ar.dyadic_mul(p_input[0], p_input[2])
    elif p_input[1] == '/':
        return ar.dyadic_div(p_input[0], p_input[2])
    else:
        return 'Error: Invalid input'
