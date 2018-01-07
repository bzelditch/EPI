# Implementation of an undirected graph
# Uses an adjacency list

class Node:
	def __init__(self, data):
		self.data = data
		self.neighbors = []
		self.visited = False

	def visit(self):
		self.visited = True

	def isVisited(self):
		return self.visited

	def getData(self):
		return self.data

	def getNeighbors(self):
		return self.neighbors

	def addNeighbor(self, node):
		self.neighbors.append(node) # What about adding self to node's neighbor list?