n=int(input())
k=int(input())
s1=str(bin(n))
s2=s1[::-1]
if s2[k]=='1':
    print(1)
else:
    print(0)    
