a = [1,2,3,4,5,6,7,8,9]
def swap(s, n1, n2):
	nloop = min(n1, n2)
	for i in range(nloop):
		x = a[s]
		a[s] = a[s+n1]
		a[s+n1] = x
		s+=1
	return s

def hello(n, d):
	s = 0
	n1 = d
	n2 = n - d
	while(n1 and n2):
		s = swap(s, n1, n2)
		print(s)
		if n1>n2:
			n1 -= n2
		else:
			n2 -= n1

hello(9, 3)
print(a)