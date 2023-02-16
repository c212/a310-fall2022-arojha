# a = set of values to be permutated
# i = position to look forward from
# l = length of set a
# op = output

# hat -- "h" "a" t"
# h -- a; h -- t


def perms(a,i,l,op=[]):
    if l==i:
        op.append("".join(a))
    for j in range(i,l):
        w = [r for r in a]  #["a","h","t"]
        w[i],w[j] = w[j],w[i]
        # w[i],w[i] = w[i],w[i]
        perms(w,i+1,l,op)
    return op
a = "hat"
l = len(a)
#print(perms(a,0,l))
#print(sorted(['hat', 'aht', 'ath', 'hta', 'tha', 'tah']))
assert sorted(perms("hat",0,l)) == sorted(['hat', 'aht', 'ath', 'hta', 'tha', 'tah']), "First assert fails."
assert len(perms("whatever",0,8,[])) == 40320, "Third assert failed."
