i=1
while i<=500:
    m=i
    sum=0
    while m>0:
        j=1
        fact=1
        rem=m%10
        while j<=rem:
            fact=fact*j
            j=j+1
        sum=sum+fact
        m//=10
    if sum==i:
        print(i,"strong number")
    i=i+1