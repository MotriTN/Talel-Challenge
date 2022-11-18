a=int(input("Give a number to return if it's perfect or not : "))
#perfect means that the number is the sum of their dividers
z=0
for i in range (1,a):
    if a%i==0:
        z+=i
if z==a:
    print("the number is perfect")
