a=int(input('Enter the number of layers(2 to 5):'))
b=int(input('Enter the side length of the top layer:'))
c=int(input('Enter the growth of each layer:'))
d=int(input('Enter the trunk width (odd number(3 to 9):'))
e=int(input('Enter the trunk height (4 to 10):'))
if a-5<0:
	x=1
	k=0
	while k+1<a:
		while x<b+k*c:
			g= '@'*((2*x)-1)
			p=' '*((b+(a-1)*c)-x)
			print(p,'#',g,'#')
			x=x+1
		k=k+1
	a=a+1
	

