import math
A,B,T=map(int,input().split())
# temp=math.gcd(A,B)
while B:
    A,B=B,A%B
if T%A==0:
    print("YES")
else:
    print("NO")
