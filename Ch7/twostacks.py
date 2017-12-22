from stack import Stack

# Implement a queue using two stacks

# Idea: One stack is reserved for pushing items into the queue and the other is reserved for popping off
#       When the pop stack is empty and someone wants to pop, transfer contents of push stack to it

class MyQueue():

	def __init__(self):
		self.pop_stack = Stack()
		self.push_stack = Stack()

	def enqueue(self, data):
		self.push_stack.push(data)

	def dequeue(self):
		if self.pop_stack.isEmpty(): # Transfer items from push_stack to pop_stack
			while not self.push_stack.isEmpty():
				top = self.push_stack.pop()
				self.pop_stack.push(top)
		self.pop_stack.pop()

	def isEmpty(self):
		return (self.pop_stack.isEmpty() and self.push_stack.isEmpty())

	def toString(self):
		s = "Push: \n"
		s += self.push_stack.toString()
		s += "Pop: \n"
		s += self.pop_stack.toString()

		return s


hi = MyQueue()
hi.enqueue(3)
hi.enqueue(4)
hi.enqueue(5)
hi.enqueue(6)
hi.enqueue(5)
hi.enqueue(4)
hi.dequeue()
hi.dequeue()
print(hi.toString())