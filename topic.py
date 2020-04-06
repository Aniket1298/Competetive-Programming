import bisect
n=input()
a=map(int,raw_input().split())
b=map(int,raw_input().split())
x=[]
y=[]
l=[]
for i in range(n):
	l.append(a[i]-b[i])
	y.append(b[i]-a[i])
l.sort()
ans=0

for i in range(n):
	if l[i]<=0:
		x=bisect.bisect(l,-l[i])
		while x<n and l[x]+l[i]<=0:
			x+=1

		ans+=(n-x)
	else:
		
		ans+=(n-i-1)
print ans
