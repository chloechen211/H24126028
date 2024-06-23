#H24126028陳秀琳
#告訴python G的值
G=6.67*(10**-11)

#幫每個箱子貼上標籤
a=int(input ('Input the force:'))
b=int(input ('Input the mass of m1:'))
d=int(input ('Input the distance:'))

#帶入公式
numerator=a*(d**2)
denominator=b*G
m2=numerator/denominator

#算出來
print(m2)

#給定c
c = 299792458

#帶入公式
e2=m2*(c**2)

#算出來again
print(e2)