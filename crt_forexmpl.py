s= input('enter string')
i=0
#USING WHILE LOOP
while i<len(s):
    print(s[i],end=' ')
    i=i+1
print()
#USING FOR LOOP
for i in range(0,len(s)):
    print(s[i],end=' ')
print()
for i in s:
    print(i,end=' ')