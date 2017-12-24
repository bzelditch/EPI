from linkedlist import Node

# Detect the *first* node in a cycle in a circular linkedlist.

# BFS is an obvious approach, but we can try something else

def detect_cycle(start):

	# Idea: 1) We can maintain a list of nodes that we've seen and return the first node seen twice
	#       2) We can have two pointers run through the list, one twice the rate of the other.
	#          If, at any point, the two pointers point to the same node, that's the one

	pointer1 = start
	pointer2 = start
	check = 0
	while pointer1 != pointer2 or check == 0: # They both start at the same node
		check = 1
		pointer1 = pointer1.getNext()
		pointer2 = pointer2.getNext().getNext() # Moves twice as fast

	return pointer1.getData()


root = Node(1)
root.addNext(Node(2))
root.addNext(Node(3))
begin = Node(4) # Where the cycle starts
root.addNext(begin)
root.addNext(Node(5))
root.addNext(Node(6))
root.addNext(begin)

print(detect_cycle(root))