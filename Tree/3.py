import sys

class Node:
	def __init__(self, value = None, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right
		
class Tree:
	def __init__(self):
		self.root = None
		
	def insert(self, x):
		if self.root == None:
			self.root = Node(x)
		else:
			current = self.root
			while current != None:
				prev = current
				if x < current.value:
					current = current.left
				else:
					current = current.right
					
			if x < prev.value:
				prev.left = Node(x)
			else:
				prev.right = Node(x)
				
	def display(self, root):
		if root == None:
			return
			
		self.display(root.left)
		print root.value,
		self.display(root.right)
	
	def formList(self, q):
		l1 = []
		
		for node in q:
			l1.append(node.value)
		return l1
			
	def swap(self, q1, q2):
		for node in q2:
			q1.append(node)
		q2[:] = []
		
	def bfs(self, root):
		if root == None:
			return
			
		q1 = []
		q2 = []
		ll = []
		
		q1.append(root)
		ll.append(self.formList(q1))
		while len(q1) > 0:
			temp = q1.pop(0)
			if temp != None:
				if temp.left != None:
					q2.append(temp.left)
				if temp.right != None:
					q2.append(temp.right)
			if len(q1) == 0:
				ll.append(self.formList(q2))
				self.swap(q1, q2)
				
		return ll
				
t = Tree()
t.insert(5)
t.insert(3)
t.insert(7)
t.insert(1)
t.insert(0)
t.insert(8)
t.display(t.root)

print '\n'
l = t.bfs(t.root)
for level in l:
	if len(level) != 0:
		print level	


