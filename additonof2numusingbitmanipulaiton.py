n1,n2=map(int,input().split())
while n2>0:
    c=n1&n2
    n1=n1^n2
    n2=c<<1
print(n1)
