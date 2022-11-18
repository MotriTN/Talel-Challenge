f = 0
z = True
h=0
while z==True:
    h+=1
    n = int(input(f"Donner le nombre n°{h} :"))
    if n==-1:
        z=False
    else:
        f+=n
print("la somme est",f)