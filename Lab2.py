import math, sys
from tasks import *
import numpy as np

if __name__ == '__main__':
    matrix = get_matrix(sys.argv[1])
    print("\nGiven matrix: ", str(matrix), sep="\n", end='\n\n')
    print("Delete repeats: ")
    first_half, second_half = matrix[0: len(matrix) // 2], matrix[len(matrix) // 2: len(matrix)]
    first_half = delete_repeats(first_half, "letters")	#Delete dublicates of letters
    second_half = delete_repeats(second_half, "numbers")	#Delete dublicates of numbers
    print(first_half + second_half, end='\n\n')
    del first_half
    del second_half

    ascii_matrix = np.array([[ord(j) for j in i] for i in matrix])
    multiple = np.array([ord(i) for i in first_column_without_lower_letters(matrix)]).reshape(1, 6).dot(ascii_matrix)

    print("Vector multiple: ")
    print([i for i in multiple], end='\n\n')

    print("ASCII codes matrix:")
    print(ascii_matrix, end='\n\n')

    print("Change min and max string: ")
    ascii_matrix = change_min_and_max_string(ascii_matrix)
    print(ascii_matrix)