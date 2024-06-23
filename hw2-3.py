n=input("Please input the year:")
m=input("Please input the month:")
print("Sun Mon Tue Wed Thu Fri Sat")

c=int(n[0:2])
y=int(n[2:])
d=1
C=int(2*(3-(c%4)))
Y=int((y%28+(y %28/4))%7)
M=int((3.4+(int(m)-3)%12)*2.6%7)
D=int(d%7)
W=(C+Y+M+D)%7
p=(W)*4
print(p*" ",end="")

if m==str("01")or m==str('03')or m== str('05')or m==str('07')or m==str('08')or m==str('10') or m==str('12'):
	day=1
	while day<=31:
		if day<10:
			print('0'+str(day)," ",end="")
		else:
			print(day," ",end="")
		day=day+1
		if W==6:
			print("")
			W=0
			continue
		W=W+1
elif m==str("02"):
	if (int(n)%4==0 )and (int(n)%100!=0)or (int(n)%400==0):
		day=1
		while day<=29:
			if day<10:
				print('0'+str(day)," ",end="")
			else:
				print(day," ",end="")
			day=day+1
			if W==6:
				print("")
				W=0
				continue
			W=W+1
	else:
		day=1
		while day<=28:
			if day<10:
				print('0'+str(day)," ",end="")
			else:
				print(day," ",end="")
			day=day+1
			if W==6:
				print("")
				W=0
				continue
			W=W+1
else:
	day=1
	while day<=30:
		if day<10:
			print('0'+str(day)," ",end="")
		else:
			print(day," ",end="")
		day=day+1
		if W==6:
			print("")
			W=0
			continue
		W=W+1

	

		





