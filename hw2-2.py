n = int(input('Input the range number:'))
print("perfect numbers:")
a = 1
while a <= n:
    total = 0  
    b = 1
    while b < a:
        if a % b == 0:
            total += b
        b = b + 1
    
    if total == a:
        print(a,  end="\n") 
    a = a + 1