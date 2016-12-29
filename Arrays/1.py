import sys

str = raw_input("Enter the input string: ")
n = len(str)
isUnique = 1
for i in range(0,n):
	for j in range(i+1,n):
		if str[i] == str[j]:
			isUnique = 0
			break
			
if isUnique == 0:
	print "Not a unique string"
else:
	print "Unique string"