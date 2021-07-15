n=int(input("enter the num"))
i=1
c1=0
while n>=0:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==2:
        if n==c1:
            print(i)
            break
        c1=c1+1
    i=i+1