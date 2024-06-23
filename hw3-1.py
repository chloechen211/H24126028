a=int(input('input the total numbers of students:'))
m=[]
c=1
i=0
while c<=a:
	m=m+[c]	
	c=c+1
n=m[:]
while i<len(m):
	if m[i]%3==0:
		del m[i]
	i=i+1
while len(m)>2:
	if len(n)%3==0:
		b=0
		while 2+2*b<len(m):
			del m[2+2*b]
			b=b+1
	elif len(n)%3==1:
		m=m[len(m)-1:]+m[:len(m)-1]
		b=0
		while 2+2*b<len(m):
			del m[2+2*b]
			b=b+1
	elif len(n)%3==2:
		m=m[len(m)-2:]+m[:len(m)-2]
		b=0
		while 2+2*b<len(m):
			del m[2+2*b]
			b=b+1

print(m)