# Queue implementation in Python

class Queue:
	def __init__(self):
		self.contents = []

	def enqueue(self, data):
		self.contents.append(data)

	def dequeue(self):
		top = self.contents[0]
		self.contents.pop(0)
		return top

	def size(self):
		return len(self.contents)

	def isEmpty(self):
		return (len(self.contents) == 0)