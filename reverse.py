n=int(input("enter the num"))
temp=n
reversed=0
while temp>0:
    remainder=temp%10
    temp//=10
    reversed=reversed*10+remainder
print(reversed)