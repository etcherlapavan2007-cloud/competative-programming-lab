n=input()
pf=[]
sf=[]
for i in range(len(n)-1):
    pf.append(n[:i+1])
for j in range(len(n)-1,0,-1):
    sf.append(n[j:])
maxi=0
i,j=0,0
while i<len(pf) and j<len(sf):
    if pf[i]==sf[i]:
        temp=pf[i]
        maxi=max(maxi,len(temp))
    i+=1
    j+=1
print(temp)
