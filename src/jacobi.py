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
        num_rows = len(matrix)

        old_solution = [0 for x in range(num_rows)]
        solution = [0 for x in range(num_rows)]
        print("old sol len = " + str(len(old_solution)))
        while k < iterations:
            for i in range(num_rows):
                solution[i] = 0
                for j in range(num_rows - 1):
                    if j != i:
                        solution[i] += matrix[i][j] * old_solution[j]
                solution[i] = (1 / matrix[i][i]) * (matrix[i][num_rows] - solution[i])

            print("Temp solution: " + str(solution))
            print("Temp old solution: " + str(old_solution))
            print(str(self.__vector_norm(solution)) + " - " + str(self.__vector_norm(old_solution)) + " < " + str(tolerance))
            temp_solution = []
            for row in range(num_rows):
                temp_solution.append(solution[row] - old_solution[row])
            if self.__vector_norm(temp_solution) < tolerance:
                break
            k += 1
            old_solution = solution
            solution = [0 for x in range(num_rows)]

        self.matrix = matrix
        self.solution = solution

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