# i=1
# while i<=3:
#     j=1
#     while j<=3-i:
#         print(" ",end=" ")
#         j=j+1
#     r=1
#     while r<((2*i)-1):
#         print("*",end=" ")
#         r=r+1
#     print()
#     i=i+1
# i=2
# while i>=1:
#     j=1
#     while j<=3-i:
#         print(" ",end=" ")
#         j=j+1
#     r=1
#     while r<((2*i)-1):
#         print("*",end=" ")
#         r=r+1
#     print()
#     i=i-1

r=1
while r<=5:
    c=1
    while c<=5:
        if (r==1 and(c==1 or c==2 or c==4 or c==5))or(r==2 and(c==1 or c==5))or(r==4 and(c==1 or c==5))or(r==5 and(c==1 or c==2 or c==4 or c==5)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        c=c+1
    print( )
    r=r+1