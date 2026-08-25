n=int(input())
dict1=input().split(",")[:n]
ptn=input().upper()
res=[]
for i in dict1:
    j=0
    uc=""
    while j<len(i):
        if i[j].isupper():
            uc+=i[j]
        j+=1
    if uc.startswith(ptn):
        res.append(i)
if len(res)>0:
    res.sort()
    print(*res)
else:
    print("No match found")
        
