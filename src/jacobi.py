from math import sqrt

__author__ = 'tyler'

# Author: Tyler Allen
# Created: 10/14/2014
# Last Modified: 10/15/2014
# This is an implementation of Jacobi's Method.


class Jacobi:

    # Initialization function that runs through gaussian elimination in order to produce the solutions for the provided
    # matrix.
    # param - matrix - the matrix to simplify. Matrix WILL BE MUTATED, clone matrix beforehand if you want to preserve
    #                  it.
    # TODO: We need to check, for this function, that the input is correct.
    def __init__(self, matrix, iterations, tolerance):
        k = 0
        num_rows = len(matrix[0])

        x = [0 for i in range(num_rows - 1)]
        while k < iterations:
            xo = [i for i in x]
            for i in range(num_rows - 1):
                pi = 0
                for j in range(num_rows - 1):
                    if j != i:
                        pi += matrix[i][j] * matrix[i][num_rows - 1]
                x[i] = (xo[i] - pi)/matrix[i][i]

            print("\nTemp solution: " + str(x))
            print("Temp old solution: " + str(xo))

            temp_solution = []
            for row in range(num_rows - 1):
                temp_solution.append(x[row] - xo[row])
            print(str(self.__vector_norm(temp_solution)) + " < " + str(tolerance))
            if self.__vector_norm(temp_solution) < tolerance:
                break
            k += 1
            #solution = [0 for x in range(num_rows)]

        print("Finished in " + str(k) + " iterations")
        self.matrix = matrix
        self.solution = x

    def __vector_norm(self, vector):
        sum = 0
        for i in range(len(vector)):
            sum += pow(vector[i], 2)
        return sqrt(sum)

    # Returns true if solution is not None.
    def has_unique_solution(self):
        return True


    # Formatted string containing the RREF form of the matrix and the solution vector.
    def __str__(self):
        return "Matrix:\n\n" + str(self.matrix)+ "\n\nSolution Vector:\n\n" + str(self.solution)