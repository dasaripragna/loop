n=int(input("enter the num"))
sum=0
i=n
while i>0:
    a=1
    b=1
    rem=i%10
    while b<=rem:
        a=a*b
        b=b+1
    sum=sum+a
    i=i//10
if n==sum:
    print(n,"strong number")
else:
    print(n,"not strong ")