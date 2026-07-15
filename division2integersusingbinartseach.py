dividend,divisor=map(int,input().split())
negative=(dividend<0)^(divisor<0)
n1=abs(dividend)
n2=abs(divisor)
if divisor==0:
    print("division by zero is not possible")
else:
    low=0
    high=n1
    ans=0
    while low<=high:
        mid=(low+high)//2
        if mid*n2<=n1:
            ans=mid
            low=mid+1
        else:
            high=mid-1
if negative:
    print(-ans)
else:
    print(ans)
