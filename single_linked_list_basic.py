import sys
import os.path

class Node(object):
	
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node
		
	def get_data(self):
		return self.data
		
	def get_next(self):
		return self.next_node
		
	def set_next(self, new_next):
		self.next_node = new_next
		
class LinkedList(object):
	
	def __init__(self, head=None):
		self.head = head
		
	def insert_head(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node
		
	def insert_tail(self, data):
		new_node = Node(data)
		current = self.head
		while current.get_next():
			current = current.get_next()
		current.set_next(new_node)
			
	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count
		
	def search(self, data):
		current = self.head
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()
		return found
		
	def delete(self, data):
	    current = self.head
	    previous = None
	    found = False
	    while current and found is False:
	        if current.get_data() == data:
	            found = True
	        else:
	            previous = current
	            current = current.get_next()
	    if current is None:
	        raise ValueError("Data not in list")
	    if previous is None:
	        self.head = current.get_next()
	    else:
	        previous.set_next(current.get_next())

	def printList(self):
		current = self.head
		while current:
			print str(current.get_data()) + " ",
			current = current.get_next()
		print "\n"
		
sll = LinkedList()
sll.insert_head(5)
sll.insert_head(6)
sll.insert_head(7)
sll.insert_head(8)
sll.insert_head(9)
sll.insert_head(10)
sll.insert_tail(4)
sll.insert_tail(3)
sll.insert_tail(2)
sll.insert_tail(1)
sll.printList()

search = sll.search(7)
print search

search = sll.search(0)
print search

sll.delete(5)
sll.printList()