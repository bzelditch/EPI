# Stack implementation in Python

class Stack:
	def __init__(self):
		self.contents = []

	def push(self, data):
		self.contents.insert(0, data)

	def pop(self):
		if len(self.contents) == 0:
			return
		top = self.contents[0]
		self.contents.pop(0)
		return top

	def peek(self):
		if len(self.contents) == 0:
			return
		return self.contents[0]

	def size(self):
		return len(self.contents)

	def isEmpty(self):
		return (len(self.contents) == 0)

	def toString(self):
		s = ""
		for i in range(len(self.contents)):
			s += str(self.contents[i]) + "\n"

		return s