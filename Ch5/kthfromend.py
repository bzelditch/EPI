from linkedlist import Node
# We want to return the kth to last element from a linked list

def kth_from_end(start_node, k):
	if start_node == None:
		return None

	num_elements = 0
	current = start_node
	while current != None:
		num_elements += 1
		current = current.getNext()

	diff = num_elements - k
	if diff < 0:
		return None

	i = 0
	current = start_node
	while i < diff:
		current = current.getNext()
		i += 1

	return current.getData()

root = Node(14)
root.addNext(Node(1))
root.addNext(Node(13))
root.addNext(Node(14))
root.addNext(Node(2))
root.addNext(Node(3))
root.addNext(Node(5))
root.addNext(Node(11))
root.addNext(Node(25))

k = 5
print(kth_from_end(root, k))