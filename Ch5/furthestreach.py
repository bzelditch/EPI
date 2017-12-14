# furthest reach is an array of non-negative integers
# A[i] is the max. number of hops we can take from position i
# Q: Can we move from point 0 to point len(A) - 1? Returns True if yes, False if no
# Also want the min. number of steps to get to the end

def furthestreach(A):
	n = len(A) - 1
	i, furthest = 0, 0
	steps = 0

	while i <= furthest and furthest <= n:

		if (i + A[i]) > furthest:
			steps += 1

		furthest = max(furthest, i + A[i])
		i += 1

	return (furthest >= n, steps)


A = [1, 4, 1, 1, 1, 0]

print(furthestreach(A))



