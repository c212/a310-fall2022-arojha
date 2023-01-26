n  =20

for lines in range(n): # 0 1 2 3 
    for columns in range(n):
        if lines==n//2 or (columns==int(0.7*n) and lines>=(0.25*n)) or(n//2-lines== columns):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

##for lines in range(n):
##    for columns in range(n):
##        if n-4-lines == columns:
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
##        #print("("+str(lines)+","+str(columns)+") ",end=" ")
##    print()
