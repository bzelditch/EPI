# LinkedList implementation in Python
# Doubly-linked

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.previous = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def getPrev(self):
		return self.previous

	def setData(self, new_data):
		self.data = new_data

	def setNext(self, new_next):
		self.next = new_next

	def setPrev(self, new_prev):
		self.prev = new_prev

	def hasNext(self):
		return self.next != None

	def addNext(self, node):
		current = self
		while current.hasNext():
			current = current.getNext()

		current.next = node
		node.setPrev(current)

	def toStr(self):
		str_rep = ""
		current = self
		while current != None:
			if current.hasNext():
				str_rep += str(current.getData()) + " <-> "
			else:
				str_rep += str(current.getData())
			current = current.getNext()
		return str_rep

