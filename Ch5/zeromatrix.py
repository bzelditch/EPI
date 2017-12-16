
# Given an mxn matrix A, if A[i][j] = 0 then zero out row i and column j

def zero(A):

	m = len(A)
	n = len(A[0])
	zeroed = [] # Columns of elements that are 0

	for i in range(m):
		for j in range(n):
			if A[i][j] == 0 and (j not in zeroed):
				for k in range(n):
					A[i][k] = 0
				for l in range(m):
					A[l][j] = 0
				zeroed.append(j)
				break

	return A

A = [[1, 1, 0], [0, 3, 5], [3, 2, 1]]
print(zero(A))