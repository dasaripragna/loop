n=int(input("enter the num"))
i=1
a=0
c=0
while n>=0:
    if n==c:
        print(a)
        break
    b=a+i
    a=i
    i=b
    c=c+1