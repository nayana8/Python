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
		if (root == None):
			return
			
		self.display(root.left)
		print root.value,
		self.display(root.right)
		
	def commonAncestor(self, root, x, y):
		if root == None:
			return None
			
		if root.value == x or root.value == y:
			return root
			
		lf = self.commonAncestor(root.left, x, y)
		rh = self.commonAncestor(root.right, x, y)
			
		if lf != None and rh != None:
			return root
		if lf != None:
			return lf
		if rh != None:
			return rh
				
t = Tree()
t.insert(5)
t.insert(3)
t.insert(7)
t.insert(6)

t.display(t.root)
print '\n'

anc = t.commonAncestor(t.root, 7, 6)
if anc != None:
	print anc.value
else:
	print 'No ancestor'