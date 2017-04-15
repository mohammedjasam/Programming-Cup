n = int(input())

import sys
l={}
for i in range(n):
    s=input()
    l[s[-1]]=(list(reversed(s)))
l=dict(sorted(l.items()))
for k,v in l.items():
    ans=""
    for x in v:
        ans+=x
    print(ans)
