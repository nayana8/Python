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
		
	def printPath(self, root, arr, sum, idx):
		if root != None:
			arr[idx] = root.value
		else:
			return
			
		i = idx
		temp = sum
		while i >= 0:
			temp -= arr[i]
			i -= 1
			if temp == 0:
				j = idx
				while j > i:
					print arr[j],
					j -= 1
				print '\n'
	
		self.printPath(root.left, arr, sum, idx+1)
		self.printPath(root.right, arr, sum, idx+1)
		
t = Tree()
t.insert(5)
t.insert(3)
t.insert(2)
t.insert(4)
t.insert(7)

t.display(t.root)

print '\n'

arr = [0] * 1000
sum = 7
print 'Paths sum to ' + str(sum) + ' are: '
t.printPath(t.root, arr, sum, 0)