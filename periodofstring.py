n=input()
for i in range(len(n)-1):
    pd=n[:i+1]
    if len(n)%len(pd)==0 and pd*(len(n)//len(pd))==n:
        res=len(pd)
        break
print(res)
