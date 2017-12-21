from linkedlist import Node
import math

# Check if a linkedlist is a palindrome

# Unfortunately, we can't iterate backwards through the list b/c it's singly linked.....

def is_palindrome(start):

	contents = []
	current = start
	while current != None:
		contents.append(current.getData())
		current = current.getNext()

	if len(contents) == 0 or len(contents) == 1:
		return True

	midpoint = int(math.floor(len(contents)/2))
	for i in range(midpoint):
		if contents[i] != contents[len(contents) - 1 - i]:
			return False

	return True


root = Node(1)
root.addNext(Node(2))
root.addNext(Node(1))
root.addNext(Node(4))
root.addNext(Node(2))
root.addNext(Node(1))

print(is_palindrome(root))