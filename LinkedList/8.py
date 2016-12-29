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
			current = Node(x)
			temp = self.first
			while temp.next != None:
				temp = temp.next
			temp.next = current

	def display(self):
		if self.first == None:
			print 'Empty linked list'
		else:
			temp = self.first
			while temp != None:
				print temp.value,
				temp = temp.next
	
	def loopDetect(self):
		loop_found = 0
		if self.first == None:
			print 'Empty linked list'
		else:
			fast = self.first
			slow = self.first
			while fast != None and fast.next != None:
				fast = fast.next.next
				slow = slow.next
				if fast == slow:
					loop_found = 1
					break
		
		if loop_found == 1:
			slow = self.first
			while fast != slow:
				fast = fast.next
				slow = slow.next
			print 'Loop starting point ' + str(fast.value)
			return 1
		
		return 0

						
l = LinkedList()
for i in range(10):
	l.insert(i)
l.display()
loop = l.loopDetect()
if loop == 1:
	print '\nLoop found'
else:
	print '\nLoop not found'