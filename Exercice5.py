a=int(input("Give a number to return their dividers : "))
c=""
for i in range (1,(a//2)+1):
    if a%i==0:
        c=c+(str(i))+","
print(c)