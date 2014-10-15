__author__ = 'tyler'

# Author: Tyler Allen
# Created: 10/13/2014
# Last Modified: 10/14/2014
# This is an implementation of the Gaussian Elimination with Partial Pivoting algorithm. Creating one of these
# objects with a provided matrix will reduce the matrix to RREF form and create the solution vector.


class GaussianPivot:

    # Initialization function that runs through gaussian elimination in order to produce the solutions for the provided
    # matrix.
    # param - matrix - the matrix to simplify. Matrix WILL BE MUTATED, clone matrix beforehand if you want to preserve
    #                  it.
    # TODO: We need to check, for this function, that the input is correct.
    def __init__(self, matrix):


    # Returns true if solution is not None.
    def has_unique_solution(self):
        return self.solution is not None

    # Formatted string containing the RREF form of the matrix and the solution vector. Not guaranteed to be correct
    # if has_unique_solution() returns false.
    def __str__(self):
        return "Matrix:\n\n" + str(self.matrix)+ "\n\nSolution Vector:\n\n" + str(self.solution)