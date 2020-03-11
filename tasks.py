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