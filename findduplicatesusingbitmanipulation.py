
n=input()
res=""
temp=0
for i in n:
    s=ord(i)-ord('a')
    if temp&(1<<s):
        res+=i
        res+=" "
        temp&=~(1<<s)
    else:
        temp|=(1<<s)
print(res)
