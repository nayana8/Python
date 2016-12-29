import sys

str1 = raw_input("Enter the string1: ")
str2 = raw_input("Enter the string2: ")
str1 += str1

found = str1.find(str2)
if found > 0:
	print "Yes, rotation"
else:
	print "Not a rotation"

