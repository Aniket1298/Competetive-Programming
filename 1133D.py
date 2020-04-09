def g(n):
	s=''
	for i in range(n):
		if i%2==0:
			s+='B'
		else:
			s+='W'
	return s
for _ in range(input()):
	n,m=map(int,raw_input().split())
	if m%2==1:
		s=g(m)
		for i in range(n):
			if i==1:
				print s[0:n-1]+'W'
			else:
				print s
	else:
		s='B'*(m)
		k='W'*(m)
		if n%2==0:
			for i in range(n-1):
				if i%2==0:
					print s
				else:
					print k
			print k[0:m-1]+'B'
		else:
			for i in range(n-1):
				if i%2==0:
					print k
				else:
					print s
			print k[0:m-1]+'B'
