def ret(n):
    return (n*(n+1))/2
for _ in range(input()):
    n=input()
    if (n/2)%2==0:
        print "YES"
        a=0
        b=0
        for i in range(1,(n/2)+1):
            print i*2,
            a+=i*2
        for i in range((n/2)-1):
            print 2*i+1,
            b+=(2*i+1)
        print a-b
    else:
        print "NO"
