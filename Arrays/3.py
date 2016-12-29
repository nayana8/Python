import sys

str = raw_input("Enter the string: ")
spaces = 0
for i in range(0,len(str)):
	if str[i] == ' ':
		spaces += 1

newlen = len(str) + (spaces*2)
newstr = str
newstr += ' ' * (spaces * 2)

j = newlen - 1
for i in range(len(str)-1,-1,-1):
	if newstr[i] != ' ':
		newstr = newstr[0:j] + newstr[i] + newstr[j+1:]
		j -= 1
	else:
		newstr = newstr[0:j-2] + '02%' + newstr[j+1:]
		j -= 3
		
print newstr
