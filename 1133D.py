from fractions import Fraction
n=input()
a=map(int,raw_input().split())
b=map(int,raw_input().split())
d={}
mx=0
z=0
for i in range(len(a)):
	if a[i]==0 and b[i]==0:
		z+=1
	elif a[i]==0:
		pass
	else:
		try:
			d[Fraction(-b[i],a[i])]+=1
			mx=max(d[Fraction(-b[i],a[i])],mx)
		except KeyError:
			d[Fraction(-b[i],a[i])]=1
			mx=max(d[Fraction(-b[i],a[i])],mx)
print mx+z
			
