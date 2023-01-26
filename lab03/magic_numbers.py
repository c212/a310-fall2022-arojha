
def pretty_print(m):
    for i in m:
        print(i)

##magic_squares = []
##for i in range(16):
##    k = int(input())
##    if k in magic_squares:
##        print("exists!")
##        break
##    magic_squares.append(k)
##print(magic_squares)
##
##
##k=0
##final_matrix = []
##for i in range(4):
##    n_row= []
##    for j in range(4):
##        n_row.append(magic_squares[k*i+j])
##    final_matrix.append(n_row)
##    k+=1
##pretty_print(final_matrix)

matrix = [[0 for i in range(4)] for j in range(4)]
#step 1
n=4
row = n-1
column = n//2
#step 2
for k in range(1,n*n+1):
    #step 3
    matrix[row][column]=k
    prev_row = row
    prev_column = column
    # step 4
    row+=1
    column+=1
    #step 5
    if row==n:
        row=0
    if column ==n:
        column=0
    # step 6
    if matrix[row][column]!=0:
        row = prev_row
        column = prev_column
        row-=1
pretty_print(matrix)










    
