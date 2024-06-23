#H24126028陳秀琳
#給定一個g值
g=9.8

#給箱子貼標籤
h=int(input("Input the height of the 1st ball:"))
m1=int(input("Input the mass of the 1st ball:"))
m2=int(input("Input the mass of the 2nd ball:"))

#帶入公式
U=m1*g*h 
u1=((2*U)/m1)**0.5

#算出來
print("The velocity of the 1st ball after slide=",u1)

#帶入公式
k=(m1+m2)
v2=(2*m1*u1)/k

#再算出來
print("The velocity of the 2nd ball after collision:",v2)


