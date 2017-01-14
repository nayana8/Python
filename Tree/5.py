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
		
	def checkBst(self, root, min, max):
		if root == None:
			return 1
			
		if ((min < root.value) and (max >= root.value)):
			return self.checkBst(root.left, min, root.value) and self.checkBst(root.right, root.value, max)
			
		return 0
		
t = Tree()
t.insert(5)
t.insert(3)
t.insert(4)
t.insert(6)
t.insert(7)

t.display(t.root)
print '\n'
result = t.checkBst(t.root, 0, 1000)
if result == 1:
	print 'Yes, it is BST'
else:
	print 'Not a BST'