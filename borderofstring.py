n=input()
temp=""
for i in range(1,len(n)):
    if n[:i]==n[-i:]:
        temp=n[:i]
print(temp)
