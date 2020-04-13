import math
for _ in range(input()):
    n=input()
    l=map(int,raw_input().split())
    l.sort()
    i=0
    j=n-1
    a=[]
    while i<j:
        a.append(l[j])
        a.append(l[i])
        i+=1
        j-=1
    if n%2==1:
        a+=[l[i]]
    for i in range(n):
        print a[n-i-1],
    print
