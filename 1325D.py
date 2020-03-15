def compute(S, X): 
    A = (S - X)//2
    a = 0
    b = 0
  
    # Traverse through all bits 
    for i in range(64): 
        Xi = (X & (1 << i)) 
        Ai = (A & (1 << i)) 
        if (Xi == 0 and Ai == 0): 
            # Let us leave bits as 0. 
            pass
              
        elif (Xi == 0 and Ai > 0): 
            a = ((1 << i) | a)  
            b = ((1 << i) | b)  
          
        elif (Xi > 0 and Ai == 0): 
            a = ((1 << i) | a)  
            # We leave i-th bit of b as 0. 
  
        else: # (Xi == 1 and Ai == 1) 
            return -1
  
    return [a,b]
a,b=map(int,raw_input().split())
if a==0 and b==0:
    print 0
elif a==b:
    print 1
    print a
elif a>b:
    print -1
elif (b-a)%2==1:
    print -1
elif (b-a)%2==0:
    t=compute(b,a)
    if t!=-1:
        print 2
        print t[0],t[1]
    else:
        print 3
        print a,(b-a)/2,(b-a)/2
