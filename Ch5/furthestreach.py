# furthest reach is an array of non-negative integers
# A[i] is the max. number of hops we can take from position i
# Q: Can we move from point 0 to point len(A) - 1? Returns True if yes, False if no
# Also want the min. number of steps to get to the end

def furthestreach(A):
	n = len(A) - 1
	i, furthest = 0, 0
	count = 1
	steps = []  # an array containing the min. # of steps to get to i
				# i.e., steps[i] is the min. # of steps needed to get to position i

	while i <= furthest and furthest < n:
		if i == 0:
			steps.append(0)
		else:
			if furthest > i:
				steps.append(count)
			else:
				count += 1
				steps.append(count)
		furthest = max(furthest, i + A[i])
		i += 1

	return (furthest >= n, steps)


A = [3, 3, 1, 2, 1, 1]

print(furthestreach(A))



