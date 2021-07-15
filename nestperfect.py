i=1
while i<=100:
    j=1
    sum=0
    while j<i:
        if i%j==0:
            sum=sum+j
        j=j+1
    if sum==i:
        print(i,"it is a perfect")
    i=i+1
