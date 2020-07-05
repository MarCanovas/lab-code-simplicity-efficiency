"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import random
import string
import sys


def RandomStringGenerator(stringLength=12):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def BatchStringGenerator(n, a=8, b=12):
    #Array of random strings
    r = []          

    for i in range(n):
        r.append(RandomStringGenerator(random.choice(range(a, b))))
    return r

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n), int(a), int(b)))
