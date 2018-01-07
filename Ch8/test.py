from search import DFS, BFS
from queueG import Queue
from graph import Node

root = Node(1)
b = Node(3)
c = Node(4)
d = Node(10)
e = Node(11)

root.addNeighbor(b) # There's a better way
b.addNeighbor(root)

b.addNeighbor(e)
e.addNeighbor(b)

root.addNeighbor(c)
c.addNeighbor(root)

c.addNeighbor(d)
d.addNeighbor(c)

#print("DFS: ")
#DFS(root)


print("BFS: ")
BFS(root)