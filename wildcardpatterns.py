s1=input().strip()
s2=input().strip()
star=-1
t=0
i,j=0,0

while i<len(s1):
    if j<len(s2) and (s1[i]==s2[j] or s2[j]=="?"):
        i+=1
        j+=1
    elif j<len(s2) and s2[j]=="*":
        star=j
        t=i
        j+=1
    elif star!=-1:
        t+=1
        i=t
        j=star+1
    else:
        print(0)
        break
else:
    while j<len(s2) and s2[j]=="*":
        j+=1
    print(1 if j==len(s2) else 0)
