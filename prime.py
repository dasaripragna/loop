n=int(input("enter the num"))
i=1
c=0
while i<=n:
    if n%i==0:
        c=c+1
    i=i+1
if c==2:
    print(n,"prime num")
else:
    print(n,"no")










