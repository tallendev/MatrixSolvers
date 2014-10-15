__author__ = 'tyler'

# Author: Tyler Allen
# Created: 10/14/2014
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
        # The solution to the provided matrix.
        self.solution = None
        # The matrix to be converted into rref form.
        self.matrix = matrix

        rows = len(matrix)
        for i in range(rows - 1):
            pivot = -1
            # Check for potential pivot rows
            max = matrix[0]
            # Find max of potential pivot rows
            for p in range(i, rows - 1):
                # Max of pivot row?
                if abs(matrix[p][i]) > abs(max[i]):
                    pivot = p
                    max = matrix[p]
            # If pivot row is 0, no solution
            if pivot == 0:
                break
            # row swap!
            if pivot != i:
                temp_row = matrix[pivot]
                matrix[pivot] = matrix[i]
                matrix[i] = temp_row
            # Apply column operations...
            for j in range(i + 1, rows):
                coefficient = matrix[j][i] / matrix[i][i]
                # Adjust each row w/ E_j - m_ji * E_i -> E_j
                for column in range(rows + 1):
                    # row adjustment
                    matrix[j][column] = matrix[j][column] - coefficient * matrix[i][column]
            print("Matrix Iter:\n" + str(matrix))
        if matrix[rows - 1][rows - 1] != 0:
            # create rows number of solution spots
            self.solution = [0 for x in range(rows)]
            # BEGIN THE BACKWARDS SUBSTITUTION
            for i in range(rows - 1, -1, -1):
                # our row
                self.solution[i] = matrix[i][rows]
                # sum previous answers
                for j in range(i + 1, rows):
                    self.solution[i] -= matrix[i][j] * self.solution[j]
                self.solution[i] /= matrix[i][i]


    # Returns true if solution is not None.
    def has_unique_solution(self):
        return self.solution is not None

    # Formatted string containing the RREF form of the matrix and the solution vector. Not guaranteed to be correct
    # if has_unique_solution() returns false.
    def __str__(self):
        return "Matrix:\n\n" + str(self.matrix)+ "\n\nSolution Vector:\n\n" + str(self.solution)