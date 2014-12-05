__author__ = 'tyler'


from src.matrix_functions import vector_norm


# Author: Tyler Allen
# Created: 12/05/2014
# Last Modified: 12/05/2014
# This is an implementation of an SOR method.

class Sor:

    # Initialization function that runs through gaussian elimination in order to produce the solutions for the provided
    # matrix.
    # param - matrix - the matrix to simplify. Matrix WILL BE MUTATED, clone matrix beforehand if you want to preserve
    #                  it.
    def __init__(self, matrix, iterations, tolerance, omega):
        k = 0
        num_rows = len(matrix[0])

        x = [1 for i in range(num_rows - 1)]
        while k < iterations:
            xo = [i for i in x]
            for i in range(num_rows - 1):
                pi = 0
                for j in range(num_rows - 1):
                    if j != i:
                        pi += (matrix[i][j] * x[j])
                x[i] = (1 - omega) * x[i] + (omega * (matrix[i][num_rows - 1] - pi))/matrix[i][i]

            temp_solution = []
            for row in range(num_rows - 1):
                temp_solution.append(x[row] - xo[row])
            if vector_norm(temp_solution) < tolerance:
                break
            k += 1

        print("Finished in " + str(k) + " iterations")
        self.matrix = matrix
        self.solution = x

    # Returns true if solution is not None.
    def has_unique_solution(self):
        return True


    # Formatted string containing the RREF form of the matrix and the solution vector.
    def __str__(self):
        return "Matrix:\n\n" + str(self.matrix)+ "\n\nSolution Vector:\n\n" + str(self.solution)