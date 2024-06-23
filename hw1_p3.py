#H24126028陳秀琳
#給定c值
c=299792458

#給箱子貼標籤
v=int(input('Input velocity:'))

#帶入公式
u=v/c

#算出來
print('Percentage of light speed=',u)

#帶入公式
l=c**2
f=v**2
k=1-(f/l)
j=k**0.5
m=1/j

#帶入數值算
n=4.3/m
print('Travel time to Alpha Centauri=',n)
s=6.0/m
print('Travel time to Barnards Star=',s)
r=309/m 
print('Travel time to Betelgeuse=',r)
x=2000000/m 
print('Travel time to Andromeda Galaxy=',s)
