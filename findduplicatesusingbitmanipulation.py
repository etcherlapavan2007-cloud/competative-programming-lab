n = input()
res = ""
temp = 0
dup = 0
for i in n:
    s = ord(i) - ord('a')
    bit = 1 << s
    if temp & bit:
        dup |= bit
    else:
        temp |= bit
for i in n:
    s = ord(i) - ord('a')
    bit = 1 << s
    if dup & bit:
        res += i + " "
        dup &= ~bit
print(res)
