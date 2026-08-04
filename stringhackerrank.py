s1=input()
maxi,ct=0,0
for i in s1:
    ct=s1.count(i)
    maxi=max(maxi,ct)
print(maxi)
