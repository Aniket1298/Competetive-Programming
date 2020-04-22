for _ in range(input()):
	n,k=map(int,raw_input().split())
	l=map(int,raw_input().split())
	f=[0]*(2*k+3)
	ans=1e10
	d={}
	for i in range(n/2):
	    try:
	        d[l[i]+l[n-i-1]]+=1
	    except KeyError:
	        d[l[i]+l[n-i-1]]=1
	    a,b=min(l[i],l[n-i-1])+1,max(l[i],l[n-i-1])+k
	    f[a]+=1
	    f[b+1]-=1
	p=0
	for i in range(1,len(f)):
	    if f[i]==0:
	        f[i]=f[i-1]
	    else:
	        f[i]+=f[i-1]
	for x in range(2,2*k +1):
	    try:
	        ans=min(ans,f[x]+ n-(2*f[x])-d[x])
	    except KeyError:
	        ans=min(ans,f[x]+ n-(2*f[x]))
	print ans
