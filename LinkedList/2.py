import sys

class Node:
	def __init__(self, value = None, next = None):
		self.value = value
		self.next = next
		
class LinkedList:
	def __init__(self):
		self.first = None
		
	def insert(self, x):
		if self.first == None:
			self.first = Node(x)
		else:
			temp = Node(x)
			current = self.first
			while(current.next != None):
				current = current.next
			current.next = temp
	
	def display(self):
		if self.first == None:
			print 'Empty linked list'
		else:
			current = self.first
			while current != None:
				print current.value,
				current = current.next
				
	def findKthLast(self, k):
		if self.first == None:
			print 'Empty linked list'
		else:
			i = 0
			fast = self.first
			slow = self.first
			while i != k:
				fast = fast.next
				i += 1
			while fast != None:
				fast = fast.next
				slow = slow.next
			
			if slow != None:
				return slow.value
				
		return -1
			
l = LinkedList()
for i in range(10):
	l.insert(i)
l.display()
k = 1
val = l.findKthLast(k)
if val != -1:
	print '\n'
	print str(k) + 'th Value is: ' + str(val)
else:
	print '\nWrong k value given, k value start from 1 to length of linked list'