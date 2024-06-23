import random
rank=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suit=['C','D','H','S']
deck=[]
for s in suit:
	for r in rank:
		deck.append(s+r)
random.shuffle(deck)
a=[]
for i in range(2):
	card=deck.pop(0)
	a=a+[card]
print(a)
if (a[0][1]=='1' or a[0][1]=='J' or a[0][1]=='Q' or a[0][1]=='K')and(a[1][1]=='1' or a[1][1]=='J' or a[1][1]=='Q' or a[1][1]=='K'):
	print('Your current value is',20)	
elif (a[0][1]=='1' or a[0][1]=='J' or a[0][1]=='Q' or a[0][1]=='K')and(a[1][1]=='A'):
	print('Your current value is',21)
elif (a[1][1]=='1' or a[1][1]=='J' or a[1][1]=='Q' or a[1][1]=='K')and(a[0][1]=='A'):
	print('Your current value is',21)
elif a[0][1]=='1' or a[0][1]=='J' or a[0][1]=='Q' or a[0][1]=='K':
	print('Your current value is',10+int(a[1][1]))
elif a[1][1]=='1' or a[1][1]=='J' or a[1][1]=='Q' or a[1][1]=='K':
	print('Your current value is',10+int(a[0][1]))
elif a[0][1]=='A':
	print('Your current value is',11+int(a[1][1]))
elif a[1][1]=='A':
	print('Your current value is',11+int(a[0][1]))
else:
	print('Your current value is',int(a[1][1])+int(a[0][1]))
if a[0][0]=='C':
	print('with the hand:',a[0][1],'-','Club',end='\n')
elif a[0][0]=='D':
	print('with the hand:',a[0][1],'-','Diamond',end='\n')
elif a[0][0]=='H':
	print('with the hand:',a[0][1],'-','Heart',end='\n')
elif a[0][0]=='S':
	print('with the hand:',a[0][1],'-','Spade',end='\n')
if a[1][0]=='C':
	print('with the hand:',a[1][1],'-','Club')
elif a[1][0]=='D':
	print('with the hand:',a[1][1],'-','Diamond')
elif a[1][0]=='H':
	print('with the hand:',a[1][1],'-','Heart')
elif a[1][0]=='S':
	print('with the hand:',a[1][1],'-','Spade')

d=False
b=int(input('Hit or Stay?(Hit=1,Stay=0):'))
while not d:
	if b==1:
		card=deck.pop(0)
		a=a+[card]
		if a[2][0]=='C':
			print('You draw:',a[2][1],'-','Club')
		elif a[2][0]=='D':
			print('You draw:',a[2][1],'-','Diamond')
		elif a[2][0]=='H':
			print('You draw:',a[2][1],'-','Heart')
		elif a[2][0]=='S':
			print('You draw:',a[2][1],'-','Spade')
	print('Your current value is:',int(a[0][1])+int(a[1][1])+int(a[2][1]))
	c=int(input('Hit or Stay?(Hit=1,Stay=0):'))
	d=(c!="1")







