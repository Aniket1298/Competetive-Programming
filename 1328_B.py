for _ in range(input()):
    a,k=map(int,raw_input().split())
    n=k-1
    x=(-1+ pow(1+4*2*n,0.5))/2
    x=int(x)
    till= (x*(x+1))/2
    s='a'*(a-(x+2))+'b'
    c='b'+'a'*(k-till-1)
    print s+'a'*(a-len(s)-len(c))+c
