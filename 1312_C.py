n=input()
a=map(int,raw_input().split())
def f(x,y):
	return (x|y)-y	
l=[]
for i in a:
	l.append([bin(i)[2:].count('1'),i])
l.sort(reverse=True)
for i in range(n):
	print l[i][1],
