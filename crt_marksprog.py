# a,b,c = map(int,input().split())
# x=a+b+c
# print('total marks')
# avg=x/3
# if avg>30:
#     print("avg is",avg)
# elif(avg<30 and avg>45) :
#     print('D grade',avg)
# elif(avg<45 and avg>60) :
#     print('c grade',avg)
# elif(avg<60 and avg>75) :
#     print('b grade',avg)
# elif avg>75:
#     print('a grade',avg)
# else:
#     print('fail')

a,b,c =map(int,input().split())
if a>30 and b>30 and c>30:
    avg =(a+b+c)/3
if avg>75:
    print('a')
elif avg>60 and avg<75:
    print('b')
elif avg>45 and avg<60:
    print('c')
elif avg>30 and avg<45:
    print('d')
# elif avg<30:
#     print('fail')
# else:
#     print('fail')