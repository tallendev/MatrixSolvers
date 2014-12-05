__author__ = 'tyler'

from math import sqrt

# Author: Tyler Allen
# Created: 12/04/2014
# Last Modified: 12/05/2014
# This is an implementation of Jacobi's Method.


# Function for calculating the vector norm of a given vector.
# param - vector - the vector to find the norm of.
def vector_norm(vector):
    sum = 0
    for i in range(len(vector)):
        sum += pow(vector[i], 2)
    return sqrt(sum)