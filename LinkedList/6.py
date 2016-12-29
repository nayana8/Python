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
			current = self.first
			while current.next != None:
				current = current.next
			current.next = Node(x)
	
	def display(self):
		current = self.first
		while current != None:
			print current.value,
			current = current.next
	
	def reverseList(self):
		head = self.first
		cur = None
		prev = None
		while head != None:
			cur = head.next
			head.next = prev
			prev = head
			head = cur
		self.first = prev
		
	def reverseListMid(self, mid):
		head = mid
		cur = None
		prev = None
		while head != None:
			cur = head.next
			head.next = prev
			prev = head
			head = cur
		return prev
			
	def findMid(self):
		fast = self.first
		slow = self.first
		while fast != None and fast.next != None:
			fast = fast.next.next
			prev = slow
			slow = slow.next
		
		if fast == None:
			return prev
		else:
			return slow
					
	def palindrome(self):
		mid = self.findMid()		
		mid.next = self.reverseListMid(mid.next)
#		self.display()

		head = self.first
		cur = mid.next
		while(cur != None):
			if head.value != cur.value:
				print '\nNot palindrome'
				return
			else:
				head = head.next
				cur = cur.next
		print '\nPalindrome'
		
l = LinkedList()
for i in range(5):
	l.insert(i)
	
for i in range(4,-1,-1):
	l.insert(i)
	
l.display()
l.palindrome()
