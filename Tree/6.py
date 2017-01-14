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
	
	def findParent(self, child):
		if self.root == None:
			return None
		else:
			current = self.root
			while current != None:
				if child.value < current.value:
					prev = current
					current = current.left
				elif child.value > current.value:
					prev = current
					current = current.right
				else:
					return prev
			return None
					
	def inorder_succ(self, x):
		if self.root == None:
			return -1
			
		current = self.root
		while current != None:
			if x < current.value:
				prev = current
				current = current.left
			elif x > current.value:
				prev = current
				current = current.right
			else:
				if current.right != None:
					temp = current.right.left
					if temp == None:
						return current.right.value
					else:
						while temp.left != None:
							temp = temp.left
						return temp.value
					
				if prev.left == current:
					return prev.value
					
				parent = self.findParent(prev)
				if parent != None and parent.left == prev:
					return parent.value
				
				return -1	
		return -1
		
t = Tree()
t.insert(5)
t.insert(3)
t.insert(1)
t.insert(4)
t.insert(8)
t.insert(6)
t.insert(10)
t.insert(7)
t.insert(11)

t.display(t.root)

inorder_su = t.inorder_succ(11)
if inorder_su != -1:
	print '\nInorder successor ' + str(inorder_su)
else:
	print '\nNo inorder successor'
				
					