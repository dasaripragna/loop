num=int(input("enter the num"))
num1=int(input("enter the num"))
if num>num1:
    a=num
else:
    a=num1
while True:
    if a%num==0 and a%num1==0:
        print(a)
        break
    a=a+1