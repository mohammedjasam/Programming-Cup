tc = int(input())
for i in range(tc):
    n = int(input())
    d=[]
    for j in range(n):
        s=input()
        if s not in d:
            d.append(s)
    print(len(d))
