from stack import Stack

# We want to sort a stack using at most one extra temporary stack

# Idea: Use the extra stack to maintain the ordering of the main stack

class SortStack():

	def __init__(self):
		self.stack = Stack() # The main stack
		self.buffer = Stack() # Only used for ordering

	def pop(self):
		self.stack.pop()

	def peek(self):
		self.stack.peek()

	def isEmpty(self):
		self.stack.isEmpty()

	def push(self, data):
		if self.stack.isEmpty() or data <= self.stack.peek():
			self.stack.push(data)
		else:
			# We need to keep popping off the main stack onto the buffer stack until data <= the top
			while data > self.stack.peek():
				top = self.stack.pop()
				self.buffer.push(top)
				print("Popping " + str(top) + " and pushing onto buffer stack...")
				if self.stack.isEmpty():
					break
			
			print("*****")
			self.stack.push(data)
			while not self.buffer.isEmpty():
				buffer_top = self.buffer.pop()
				self.stack.push(buffer_top)
				print("Pushing " + str(buffer_top) + " onto the main stack...")
				if self.buffer.isEmpty():
					break
			print("*****")
			print("The stack looks like: " + "\n" + self.stack.toString())

	def toString(self):
		self.stack.toString()


h = SortStack()
h.push(1)
h.push(3)
h.push(2)
h.push(10)



