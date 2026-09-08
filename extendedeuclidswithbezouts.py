import math
def extended_gcd(a,b):
    if b==0:
        return a,1,0
    g,x1,y1=extended_gcd(b,a%b)
    x=y1
    y=x1-(a//b)*y1
    return g,x,y
A,B=map(int,input().split())
c=math.gcd(A,B)
g,x,y=extended_gcd(A,B)
if c%g!=0:
    print("No values")
else:
    x=x*(c//g)
    y=y*(c//g)
print(x,y,g)


