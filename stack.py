a=[1,2,3,4,5]
l=5
def push(a=[]):
	global l
	if len(a)>=10:
		print 'overflow occur'
		return 0
	for i in range(6,11):
		a.append(i)
	l=l+5
def pop(a=[]):
	global l
	if len(a)<=0:
		print 'underflow occur'
		return 0
	del a[-1]
	l=l-1
def list(i):
	global l
	print a[i]
	if i == l-1:
		return 0
	else:
		list(i+1)

push(a)
push(a)
pop(a)
list(0)

