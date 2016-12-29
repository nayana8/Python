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
			print 'Linked list empty'
		else:
			temp = self.first
			while temp != None:
				print temp.value,
				temp = temp.next
		
	def removeDup(self):
		if self.first == None:
			return
		else:
			cur = self.first
			while(cur != None):
				prev = cur
				temp = cur.next
				while(temp != None):
					if cur.value == temp.value:
						prev.next = temp.next
					else:
						prev = temp
					temp = temp.next
				cur = cur.next
				
l = LinkedList()
l.insert(1)
l.insert(2)
l.insert(1)
l.insert(3)
l.insert(4)
l.insert(4)

l.display()
l.removeDup()
print '\nAfter removing duplicates'
l.display()