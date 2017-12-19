from linkedlist import Node

# Remove duplicates from a doubly-linked LinkedList

# We can do this in two (more?) ways: 
# 1) maintain a buffer of values we've already seen and check it
# 2) for each value in the linkedlist, search further to find any duplicates


def remove_dups1(start_node):

	seen = []
	current = start_node
	if current == None:
		return current

	previous = None
	while current != None:
		val = current.getData()
		if val in seen:
			# Remove this node from the list
			next_node = current.getNext()
			previous.setNext(next_node)
		
		else:
			seen.append(val)
			previous = current

		current = current.getNext()

	return start_node # We can't return "current".....


root = Node(14)
root.addNext(Node(1))
root.addNext(Node(13))
root.addNext(Node(14))
root.addNext(Node(2))
root.addNext(Node(3))
root.addNext(Node(5))
root.addNext(Node(11))
root.addNext(Node(25))

print(root.toStr())

mod = remove_dups1(root)
print(mod.toStr())
