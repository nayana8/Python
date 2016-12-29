import sys

str1 = raw_input("Enter the input string: ")
len1 = len(str1)
i = 0
newstr = []
count = 1
while i < (len1-1):
	if str1[i] == str1[i+1]:
		count += 1
	else:
		newstr.append(str1[i])
		newstr.append(str(count))
		count = 1
	i += 1

newstr.append(str1[len1-1])
if str1[len1-2] != str1[len1-1]:
	newstr.append('1')
else:
	newstr.append(str(count))

str2 = ''.join(newstr)
if (len(str2) <= len1):
	print "Compressed string: ", str2
else:
	print "Not compressed, original string: ", str1
		