#not (a and b) == (not a) or (not b)
# 0= False
# 1= True
#method 1
def lhs(a,b):
    return not(a and b)
def rhs(a,b):
    return ((not a) or (not b))

#method 2
def function(a,b):
    return not (a and b) == ((not a) or (not b))

#print(lhs(0,1)==rhs(0,1))
#print(lhs(0,1)==rhs(1,0))
#print(rhs(False,True))
print(function(0,0))
print(function(0,1))
print(function(1,0))
print(function(1,1))

# not ((not a) or (not b)) == a and b
# not(not a) and not(not b)
# a and b
