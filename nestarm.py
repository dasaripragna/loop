i=100
while i<=500:     
    j=i
    sum=0
    while j>0:
        digit=j%10
        sum+=digit**3
        j//=10
    if i==sum:
        print(i,"its a arm strong num")
    i=i+1