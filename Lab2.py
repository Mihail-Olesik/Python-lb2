import math, sys
from tasks import *

if __name__ == '__main__':
    matrix = get_matrix(sys.argv[1])
    print("\nGiven matrix: ", str(matrix), sep="\n")

    print("Delete repeats: ")
    first_half, second_half = matrix[0: len(matrix) // 2], matrix[len(matrix) // 2: len(matrix)]
    first_half = delete_repeats(first_half, "letters")	#Delete dublicates of letters
    second_half = delete_repeats(second_half, "numbers")	#Delete dublicates of numbers
    print(first_half + second_half)
    del first_half
    del second_half

