import sys

def printMatrix(mat, rcnt, ccnt):
	print "\nDisplay the matrix "
	for i in range(rcnt):
		for j in range(ccnt):
			print mat[i][j],
		print "\n"

def zeroMatrix(matrix, rcnt, ccnt):
	row = [0] * rcnt
	col = [0] * ccnt
	for i in range(rcnt):
		for j in range(ccnt):
			if (matrix[i][j] == 0):
				row[i] = 1
				col[j] = 1

	for i in range(0,rcnt):
		for j in range(0, ccnt):
			if row[i] == 1 or col[j] == 1:
				matrix[i][j] = 0

# Input
row_count = 3
col_count = 3
matrix = [[0 for j in range(col_count)] for i in range(row_count)]

print "Enter the matrix elements ", row_count, col_count
	for i in range(0,row_count):
		for j in range(0,col_count):
			matrix[i][j] = int(raw_input())
						
printMatrix(matrix, row_count, col_count)
zeroMatrix(matrix, row_count, col_count)
printMatrix(matrix, row_count, col_count)

	
	
