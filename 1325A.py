for _ in range(input()):
    n=input()
    l=map(int,raw_input().split())
    l=list(set(l))
    print len(l)
