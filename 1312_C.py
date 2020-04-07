import math
def cb(n,b):
	x=int(ceil(math.log(n,b)))
	
for _ in range(input()):
	n,k=map(int,raw_input().split())
	a=map(int,raw_input().split())
	n=0
	l=[0]*10000
	f=1
	for n in a:
		while n>0 and f==1:
			x=int(math.ceil(math.log(n,k)))
			if n>=pow(k,x):
				n-=pow(k,x)
				if l[x]==0:
					l[x]=1
					x-=1
				else:
					f=0
			else:
				x-=1
				if n>=pow(k,x):
					n-=pow(k,x)
					if l[x]==0:
						l[x]=1
						x-=1
					else:
						f=0
	if f:
		print "YES"
	else:
		print "NO"
