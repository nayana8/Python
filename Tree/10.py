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
		
	def subTree(self, root1, root2):
		if root1 == None and root2 == None:
			return 1
			
		if root1 != None and root2 == None:
			return 1
			
		if root1 == None and root2 != None:
			return 0
			
		if root1.value == root2.value:
			return self.subTree(root1.left, root2.left) and self.subTree(root1.right, root2.right)
			
		return self.subTree(root1.left, root2) or self.subTree(root1.right, root2)

t = Tree()
t.insert(5)
t.insert(3)
t.insert(8)
t.insert(4)
t.insert(1)
t.insert(7)
t.insert(6)

t.display(t.root)

t1 = Tree()
t1.insert(3)
t1.insert(4)
t1.insert(1)

print '\n'
t1.display(t1.root)

subtree = t.subTree(t.root, t1.root)
if subtree == 1:
	print '\nYes, subtree'
else:
	print '\nNot subtree'
	