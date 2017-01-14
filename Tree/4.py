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
		
	def height(self, root):
		if root == None:
			return 0
			
		maxL = 1 + self.height(root.left)
		maxR = 1 + self.height(root.right)
		if maxL > maxR:
			return maxL
		else:
			return maxR

	def checkBalancedBst(self, root):
		if root == None:
			return 1
		
		maxL = self.height(root.left)
		maxR = self.height(root.right)
		if (abs(maxL-maxR) > 1):
			return 0
			
		return self.checkBalancedBst(root.left) and self.checkBalancedBst(root.right)

t = Tree()
t.insert(5)
t.insert(3)
t.insert(1)
t.insert(7)
t.insert(6)
t.insert(8)
t.insert(10)

t.display(t.root)

h = t.height(t.root)
print '\nHeight of tree: ' + str(h)

chk = t.checkBalancedBst(t.root)
if chk == 1:
	print 'Yes, it is balanced BST'
else:
	print 'Not a balanced BST'
		