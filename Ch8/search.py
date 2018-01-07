# This module will contain implementations of DFS and BFS
from graph import Node
from queueG import Queue

def DFS(root):
	if root == None:
		return
	root.visit()
	print("Visiting: " + str(root.getData())) # Just to see it
	for n in root.getNeighbors():
		if not n.isVisited():
			DFS(n)

def BFS(root):
	q = Queue()
	root.visit()
	q.enqueue(root)

	while not q.isEmpty():
		top = q.dequeue()
		top.visit()
		print("Visiting: " + str(top.getData()))
		for n in top.getNeighbors():
			#print(n.isVisited())
			if not n.isVisited():
				q.enqueue(n)
				#print('Adding ' + str(n.getData()) + ' to the queue')
