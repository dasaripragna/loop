i=1
ip=0
while i<=100:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==2:
        print(i,"prime num")
        ip=ip+1
    i=i+1
print(ip)