import math
for _ in range(input()):
    a,b=map(int,raw_input().split())
    if a>b:
        t=a%b
        if t==0:
            print 0
        else:
            print (a-t+b -a)
    else:
        print (b-a)
