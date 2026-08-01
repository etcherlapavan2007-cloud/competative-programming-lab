n=int(input())
arr=list(map(int,input().split()))
goal=int(input())
res=[]
arr.sort()
for i in range(n):
    left=i+1
    right=n-1
    if i>0 and arr[i]==arr[i-1]:
        continue
    while left<right:
        total=arr[i]+arr[left]+arr[right]
        if total==goal:
            res.append([arr[i],arr[left],arr[right]])
            left+=1
            right-=1
            while left<right and arr[left]==arr[left-1]:
                left+=1
            while left<right and arr[right]==arr[right+1]:
                right-=1
        elif total<goal:
            left+=1
        else:
            right-=1
for i in res:
    print(*i)
            
