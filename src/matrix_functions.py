__author__ = 'tyler'

from math import sqrt


def vector_norm(vector):
    sum = 0
    for i in range(len(vector)):
        sum += pow(vector[i], 2)
    return sqrt(sum)