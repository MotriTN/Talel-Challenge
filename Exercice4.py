a=int(input("Give a : "))
b=int(input("Give b : "))
if a>b :
    z=a
    e=b
else:
    z=b
    e=a
while e!=0:
    r=z%e
    z=e
    e=r
print(z)
