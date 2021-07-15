n=int(input("enter the num"))
sum=0
i=n
while n>0:
    d=n%10
    n=n//10
    sum=sum+d
if i%sum==0:
    print("harshad num")
else:
    print("not harshad num")