import re
#rejex

a = "12345 6789"
b = a
# substitution- sub(pattern,replace pattern, string  )
print(a+" changes to "+re.sub(r'([0-9])',r'(\1)',b))

print(a+" changes to "+re.sub(r'([0-9])([0-9])',r'\2\1',b))

n = re.findall(r'([0-9])([0-9])',b)
#print(n)

for i in n:
    s = str(int(i[0])+int(i[1]))
    b = re.sub(i[0]+i[1],s,b)
print(a+" changes to "+b)

