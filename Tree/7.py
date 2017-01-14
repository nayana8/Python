import sys

# Using topological sort

class Graph:
	def __init__(self, num = 0, projects = None):
		self.num = num
		self.visited = {}
		self.adjList = {}
		for i in projects:
			self.visited[i] = 0
			self.adjList.setdefault(i, []).append(None)
	
	def addDependency(self, key, value):
		self.adjList[key].append(value)
		
	def display(self):
		for keys,values in self.adjList.items():
			print keys
			print values
			
	def getOrder(self, key, stack):
		self.visited[key] = 1
		
		values = self.adjList.get(key, None)
		if values != None:
			for value in values:
				if value != None and self.visited[value] == 0:
					self.getOrder(value, stack)
				
		stack.append(key)
		
	def buildOrder(self, projects):
		stack = []
		
		for i in projects:
			if self.visited[i] == 0:
				self.getOrder(i, stack)
		
		print "Build Order is: "
		for k in reversed(stack):
			print k,


projects = ['a', 'b', 'c', 'd', 'e', 'f']				
g = Graph(6, projects)
g.addDependency('a', 'd')
g.addDependency('f', 'b')
g.addDependency('b', 'd')
g.addDependency('f', 'a')
g.addDependency('d', 'c')

g.buildOrder(projects)

