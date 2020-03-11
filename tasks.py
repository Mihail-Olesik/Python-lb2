import numpy as np

def get_matrix(path):
	matrix = []
	f = open(path, 'r')
	for line in f:
	    matrix.append(line.split())
	f.close()
	matrix = np.array(matrix)
	return matrix

def delete_repeats(matrix, property):
	a = []
	if property == 'letters':
		for i in matrix:
			for j in i:
				if j not in a or j.isdigit():
					a.append(j)
	if property == 'numbers':
		for i in matrix:
			for j in i:
				if j not in a or j.isalpha():
					a.append(j)
	return ''.join(a)

def first_column_without_lower_letters(matrix):
	size_of_elems = 0
	for i in range(len(matrix[0])):
		for elem in matrix[:, i]:
			if elem.islower() and ord(elem) >= ord('a') and ord(elem) <= ord('z'):
				break
			size_of_elems += 1
		if size_of_elems == len(matrix):
			return matrix[:, i]
		size_of_elems = 0
	return False