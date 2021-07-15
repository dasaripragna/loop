n=int(input("enter the num"))
i=n
sum=0
while i>0:
    digit=i%10
    sum+=digit**3
    i//=10
if n==sum:
    print("arm strong")
else:
    print("not arm strong") 
