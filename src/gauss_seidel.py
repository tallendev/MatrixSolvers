__author__ = 'tyler'


from src.matrix_functions import vector_norm


class GaussSeidel:

    def __init__(self, matrix, iterations, tolerance):
        k = 0
        num_rows = len(matrix[0])

        x = [0 for i in range(num_rows - 1)]
        while k <= iterations:
            xo = [i for i in x]
            for i in range(num_rows - 1):
                sum1 = 0
                for j in range(num_rows - 1):
                    if i != j:
                        sum1 += matrix[i][j] * x[j]
                x[i] = (matrix[i][num_rows - 1] - sum1)/matrix[i][i]

            temp_solution = []
            for row in range(num_rows - 1):
                temp_solution.append(x[row] - xo[row])
            print(str(vector_norm(temp_solution)) + " < " + str(tolerance))
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
