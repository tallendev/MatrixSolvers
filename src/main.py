#!usr/bin/python

__author__ = 'tyler'

# Author: Tyler Allen
# Date Created: 10/13/2014
# Last Modified: 12/05/2014
# A program for coordinating the use of the 5 solver methods being implemented for the Math 362 honors project.
# This program accepts a solution method (from the ones provided), and a file.
# For more specific instructions, please see the usage message.

import sys
import os
import copy
from src.matrix_parser import parse_matrix
from src.gaussian import Gaussian
from src.gaussian_pivot import GaussianPivot
from src.jacobi import Jacobi
from src.gauss_seidel import GaussSeidel
from src.sor import Sor

# Exit due to invalid number of arguments.
INVALID_ARG_COUNT = 1
# Exit due to file without proper permissions, or file does not exist.
INVALID_FILE = 2
# Exit due to bad matrix input.
INVALID_INPUT = 3
# Bad solution method.
INVALID_METHOD = 4

# Index in args array of program name
PROGRAM_NAME = 0
# Index in args array of method to use in solving the matrix.
SOLVE_METHOD = 1
# Index in args array of optional file name
FILE_NAME = 2
# Index in args array of the number of iterations.
ITERATIONS = 3
# Index in args array of the tolerance for iterative methods.
TOLERANCE = 4
# Index in args array of the omega for the SOR method.
OMEGA = 5

# python [program_name] solve_method
NUM_PROMPT_ARGS = 2
# python [program_name] solve_method [file_input]
NUM_FILE_ARGS = 3

# Number of args for a solve method.
SOLVE_ARGS = 3
# Number of args for iterative method.
ITERATIVE_ARGS = 5
# Number of args for SOR method.
SOR_ARGS = 6

# available solve method dictionary
DIRECT_METHODS = {'gaussian': Gaussian,
                  'gaussian_pivot': GaussianPivot}

ITERATIVE_METHODS = {'jacobi': Jacobi,
                     'gauss_seidel': GaussSeidel}

RELAXATION_METHODS = {'sor': Sor}


def main():
    num_args = len(sys.argv)
    file = None
    # Prompt user for input
    if num_args == NUM_PROMPT_ARGS:
        print("Input a matrix:\n")
        file = sys.stdin
    # Open specified file
    elif num_args >= NUM_FILE_ARGS:
        if not os.access(sys.argv[FILE_NAME], os.F_OK):
            usage(INVALID_FILE, "File not found: " + sys.argv[FILE_NAME])
        elif not os.access(sys.argv[FILE_NAME], os.R_OK):
            usage(INVALID_FILE, "File could not be read: " + sys.argv[FILE_NAME])
        file = open(sys.argv[FILE_NAME], "r", encoding="utf-8")
    # Usage
    else:
        usage(INVALID_ARG_COUNT, "Invalid number of arguments.")

    # Validate solve method
    if not (sys.argv[SOLVE_METHOD] in DIRECT_METHODS or sys.argv[SOLVE_METHOD] in ITERATIVE_METHODS
            or sys.argv[SOLVE_METHOD] in RELAXATION_METHODS):
        usage(INVALID_METHOD, "Solve method provided on command line does not exist: " + sys.argv[SOLVE_METHOD])

    input = file.read()
    matrix = parse_matrix(input)
    solution = [[]]
    if matrix is None:
        usage(INVALID_INPUT, "There was an error in the input.")
    else:
        print("Original Matrix:\n" + str(matrix) + "\n")
        if len(matrix) == 0:
            print("The matrix was empty.")
        else:
            if sys.argv[SOLVE_METHOD] in DIRECT_METHODS:
                if len(sys.argv) != SOLVE_ARGS:
                    usage(INVALID_INPUT, "Invalid number of arguments for solve method.")
                solution = DIRECT_METHODS[sys.argv[SOLVE_METHOD]](copy.deepcopy(matrix))
            elif sys.argv[SOLVE_METHOD] in ITERATIVE_METHODS:
                if len(sys.argv) != ITERATIVE_ARGS:
                    usage(INVALID_INPUT, "Invalid number of arguments for solve method.")
                solution = ITERATIVE_METHODS[sys.argv[SOLVE_METHOD]](copy.deepcopy(matrix), float(sys.argv[ITERATIONS]),
                                                                     float(sys.argv[TOLERANCE]))
            elif sys.argv[SOLVE_METHOD] in RELAXATION_METHODS:
                if len(sys.argv) != SOR_ARGS:
                    usage(INVALID_INPUT, "Invalid number of arguments for solve method.")
                solution = RELAXATION_METHODS[sys.argv[SOLVE_METHOD]](copy.deepcopy(matrix), float(sys.argv[ITERATIONS]),
                                                                      float(sys.argv[TOLERANCE]), float(sys.argv[OMEGA]))
    if solution.has_unique_solution():
        print(solution)
    else:
        print("Matrix has no unique solution.")


def usage(exit_status, message):
    print(message + "\nUsage: python " + sys.argv[PROGRAM_NAME] + " solve_method ["
          "file_input] [max_iterations] [tolerance] [sor_w]\n max_iterations, tolerance required for iterative methods."
          "sor_w value required for SOR methods. "
          "\n\nValid Solve Methods:\ngaussian: Basic Gaussian Elimination using "
          "Backwards Substitution\ngaussian_pivot: Gaussian Elimination using Partial "
          "Pivots\njacobi: Jacobi approximation method\ngauss_seidel: Gause-Seidel approximation, improvement "
          "on Jacobi\nsor: Successive Over-Relaxtion approximation method\n\n"
          "Valid File Format: {{a11, a12, ...}, {a21, a22, ...}, ...}\nAny "
          "whitespace is accepted.")
    sys.exit(exit_status)

main()
