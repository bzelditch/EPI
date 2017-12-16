# Rotate an nxn matrix by 90 degrees

# Idea: Work one layer at a time and rotate each layer by sequentially swapping values.
#       We'll need to rotate a total of n-1 layers

# A is an nxn matrix
def rotate(A):

	n = len(A)
	for i in range(n-1):

		# Rotate the ith layer. Begin in the top left corner and swap each element counter-clockwise
		# n - 1 times
		for j in range(n-1):

			


