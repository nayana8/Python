import sys

class Node:
	def __init__(self,value = None,next = None):
		self.value = value
		self.next = next
		
class LinkedList:
	def __init__(self):
		self.first = None
	
	def insert(self, x):
		if self.first == None:
			self.first = Node(x)
		else:
			current = self.first
			while current.next != None:
				current = current.next
			current.next = Node(x)
	
	def display(self):
		if self.first == None:
			print 'Linked list is empty'
		else:
			current = self.first
			while current != None:
				print str(current.value),
				current = current.next
		
	def length(self):
		if self.first == None:
			return 0
		else:
			current = self.first
			count = 0
			while current != None:
				count += 1
				current = current.next
			return count
			
def intersection(l1, l2):
	if l1.first == None or l2.first == None:
		return
		
	len1 = l1.length()
	len2 = l2.length()
	
	if (len1 >= len2):
		fast = l1.first
		diff = len1 - len2
		slow = l2.first
	else:
		fast = l2.first
		diff = len2 - len1
		slow = l1.first
	
	i = 0
	while i < diff:
		fast = fast.next
		i += 1
	
	while fast != None and slow != None and fast != slow:
		fast = fast.next
		slow = slow.next
		
	if fast == None or slow == None:
		print '\nNo intersection found'
	else:
		print '\nIntersection at ' + str(fast.value)
		
		
l1 = LinkedList()
l2 = LinkedList()
for i in range(5):
	l1.insert(i)
for i in range(10):
	l2.insert(i)
	
l1.display()
print '\n'
l2.display()
print '\n'
intersection(l1, l2)