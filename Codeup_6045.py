a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = a+b+c
e = d/3
print(d,format(e, ".2f")) # 반드시 소수점 2자리가 나와야 하는 경우 format(f , ".2f")