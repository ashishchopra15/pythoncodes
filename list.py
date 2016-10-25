a=[1,2,3,4,5,6]
def list(i):
	print a[i]
	if i == -6:
		return 0
	else:
		list(i-1)
list(-1)
