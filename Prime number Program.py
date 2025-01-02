# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:06:15 2024

@author: Aharan
"""

def is_prime(number):
    """
    Function to determine whether a given number is a prime number.

    Parameters:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is a prime number, False otherwise.
    """
    if number <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    if number == 2:  # 2 is the only even prime number
        return True
    if number % 2 == 0:  # Other even numbers are not prime
        return False

    # Check for divisors from 3 to √number, skipping even numbers
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

# Input and Output
num = int(input("Enter any Given Number: "))
if is_prime(num):
    print("The Given Value is a Prime Number.")
else:
    print("Given Value is NOT a Prime Number.")
