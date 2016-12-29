import sys

str = raw_input("Enter the string: ")
hash = {}

for letter in str:
	if letter.isalpha():
		if letter in hash:
			hash[letter] += 1
		else:
			hash[letter] = 1

odd = 0
for key in hash:
	if (hash[key] % 2) != 0:
		odd += 1

if odd <= 1:
	print "Palindrome"
else:
	print "Not a palindrome"