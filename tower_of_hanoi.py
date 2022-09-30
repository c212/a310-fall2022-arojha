def toh(n,rod_a,rod_b,rod_c):
    if n==0:
        return
    toh(n-1,rod_a,rod_c,rod_b)
    print("moving rod "+ str(n)+" from "+rod_a+" to "+rod_c)
    toh(n-1,rod_b,rod_a,rod_c)

toh(3,'A','B','C')
