for _ in range(input()):
    n=input()
    k=2
    while n%((1<<k)-1)!=0:
        k+=1
    print n/((1<<k)-1)
