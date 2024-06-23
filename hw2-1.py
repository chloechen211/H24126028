# 假设有三个人说了真话
thief = 1
s1=thief!=1
s2=thief==3
s3=thief==4
s4=not(thief==4)

if s1+s2+s3==True:
    print("the thief is 4")
elif s1+s2+s4==True:
    print("the thief is 3")
elif s2+s3+s4==True:
    print("the thief is 1")
elif s1+s3+s4==True:
    print("the thief is 2")


