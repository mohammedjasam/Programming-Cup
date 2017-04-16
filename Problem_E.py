s = input()
d={}
s=list(s)
for x in range(len(s)):
    if s[x] not in d.keys():
        d[s[x]]=1
    else:
        d[s[x]]+=1
l=[]
for x in sorted(d.values()):
    l.append(x)
l=list(reversed(l))
if len(l)>2:
    del l[0]
    del l[0]

    print(sum(l))
else:
    print(0)
