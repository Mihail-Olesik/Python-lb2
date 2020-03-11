import numpy as np

def get_matrix(path):
	matrix = []
	f = open(path, 'r')
	for line in f:
	    matrix.append(line.split())
	f.close()
	matrix = np.array(matrix)
	return matrix