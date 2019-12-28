s = str(input('enter a string'))
i = 0
a=0
count = 0
while i<len(s):
    if s[i].isdigit():
        count+=1
        a += int(s[i])
    i+=1
print('count',count,'sum of digits',a)
