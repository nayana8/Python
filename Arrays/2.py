import sys

str = raw_input("Enter the input string1: ")
str1 = raw_input("Enter the input string2: ")

len1 = len(str)
len2 = len(str1)
if(len1 != len2):
	print "Not permutation strings"
	exit()
		
hash = {}
for i in range(0, len1):
	if str[i] in hash:
		hash[str[i]] += 1
	else:
		hash[str[i]] = 1
		
hash1 = {}
for i in range(0, len1):
	if str1[i] in hash1:
		hash1[str1[i]] += 1
	else:
		hash1[str1[i]] = 1
		
if hash == hash1:
	print "Permutation Strings"
else:
	print "Not permutation strings"
