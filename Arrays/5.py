import sys

word1 = raw_input("Enter the first word: ")
word2 = raw_input("Enter the second word: ")

len1 = len(word1)
len2 = len(word2)

diff = abs(len1 - len2)
if(diff > 1):
	print "Not one edit away"
	exit()
	
# Check for replace, delete or insert
edit = 0
if(diff == 0):
	i = 0
	for letter in word1:
		if letter != word2[i]:
			edit += 1
		i += 1
else:
	if len1 > len2:
		long = word1
		short = word2
	else:
		long = word2
		short = word1
	i = 0
	j = 0
	while i < len2:
		if short[i] != long[j]:
			j += 1
			edit += 1
		else:
			i += 1
			j += 1

if edit > 1:
	print "Not one edit away"
else:
	print "Yes, one edit away"
		

			