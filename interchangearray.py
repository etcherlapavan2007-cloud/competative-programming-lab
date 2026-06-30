size=int(input())
arr=list(map(int,input().split()))
maxi=max(arr)
mini=min(arr)
i=arr.index(maxi)
j=arr.index(mini)
arr[i],arr[j]=mini,maxi
print(*arr)
