import random


# removeduplicates() removes duplicate values from a sorted array of integers
# runs in O(n) time and uses O(1) space

def removeduplicates(ints):

	if( len(ints) == 1 ):
		return ints 

	index = 0
	current = ints[index] # The current value we're considering
	keepgoing = True

	while( keepgoing ):

		if( len(ints) == 1 ): #You never know
			return ints 

		if( index == len(ints) - 1): #We've made it to the end of the list
			keepgoing = False
			break

		if( ints[index + 1] == current ): #If there's a duplicate, remove the duplicate
			ints.remove(ints[index + 1])

		else:
			index += 1
			current = ints[index]


		if( index == len(ints) ): #We've made it to the end of the list
			keepgoing = False

	return ints

def main():
	ints = [random.randint(0, 30) for _ in range(10)]
	ints.sort()
	print(ints)

	distincts = removeduplicates(ints)
	print(distincts)




