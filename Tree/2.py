import sys

class Node:
	def __init__(self, value = None, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right
		
def insertMin(root, arr, low, high):
	if low > high:
		return None
	
	mid = (low+high)/2
	root = Node(arr[mid])
	root.left = insertMin(root.left, arr, low, mid-1)
	root.right = insertMin(root.right, arr, mid+1, high)
	return root
		
def display(root):
	if root == None:
		return
		
	display(root.left)
	print root.value,
	display(root.right)


arr = []
for i in range(1,10):
	arr.append(i)

root = None
root = insertMin(root, arr, 0, len(arr)-1)
display(root)
						