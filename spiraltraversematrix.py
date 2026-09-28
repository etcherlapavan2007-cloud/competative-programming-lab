n,m=map(int,input().split())
arr=[list(map(int,input().split()))[:m] for i in range(n)]
res=[]
top=0
bottom=n-1
left=0
right=m-1
while top<=bottom and left<=right:
    for i in range(left,right+1):
        res.append(arr[top][i])
    top+=1
    for i in range(top,bottom+1):
        res.append(arr[i][right])
    right-=1
    if top<=bottom:
        for i in range(right,left-1,-1):
            res.append(arr[bottom][i])
        bottom-=1
    if left<=right:
        for i in range(bottom,top-1,-1):
            res.append(arr[i][left])
        left+=1
print(*res)
        
        
