import sys

class Node:
	def __init__(self, value = None, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right
		self.visited = False
		
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
	
	def findTree(self, root, x):
		if root == None:
			return None
			
		current = root
		while current != None:
			prev = current
			if x < current.value:
				current = current.left
			elif x > current.value:
				current = current.right
			else:
				return current
		return None

			
	def dfs(self, root, x, y):
		if root == None:
			return 0
			
		node1 = self.findTree(root, x)
		if node1 == None:
			return 0
					
		s = []
		s.append(node1)
		
		while len(s) > 0:
			temp = s.pop()
			temp.visited = True
			if temp.value == y:
				return 1
			if temp.left != None and temp.left.visited == False:
				s.append(temp.left)
			if temp.right != None and temp.right.visited == False:
				s.append(temp.right)
		return 0
				
t = Tree()
t.insert(5)
t.insert(3)
t.insert(1)
t.insert(0)
t.insert(8)
t.insert(6)
t.insert(10)
t.display(t.root)

route = t.dfs(t.root, 8, 10)	
print '\n'
if route == 1:
	print 'Route exists'
else:
	print 'Route doesn\'t exist'	