from linkedlist import Node

# Sum two linked lists, assuming that the digits are stored in reverse order in the lists

def sum_lists(start1, start2):

	list_sum = 0
	exponent = 0 # The power of ten we're currently on
	pointer1 = start1
	pointer2 = start2

	if start1 == None or start2 == None:
		return None

	while pointer1 != None and pointer2 != None:
		power = 10**exponent
		list_sum += (pointer1.getData() + pointer2.getData())*power
		pointer1 = pointer1.getNext()
		pointer2 = pointer2.getNext()
		exponent += 1

	# At this point, either pointer1 = None or pointer2 = None or both equal None
	# If both, we can just return the sum
	if pointer1 == None and pointer2 == None:
		return list_sum

	elif pointer1 == None:
		while pointer2 != None:
			power = 10**exponent
			list_sum += pointer2.getData()*power
			pointer2 = pointer2.getNext()
			exponent += 1

	else:
		while pointer1 != None:
			power = 10**exponent
			list_sum += pointer1.getData()*power
			pointer1 = pointer1.getNext()
			exponent += 1

	return list_sum

root1 = Node(14)
root1.addNext(Node(1))
root2 = Node(15)


print(sum_lists(root1, root2))