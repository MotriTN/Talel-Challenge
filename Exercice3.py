f = 0
z = True
h=0
while z==True:
    h+=1
    n = int(input(f"Donner le nombre n°{h} :"))
    if n!=0:
        f=f*n
    else:
        z=False
print("la somme est",f)