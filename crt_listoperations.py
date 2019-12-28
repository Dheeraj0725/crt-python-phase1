# list1=[34,45,56,67,22,221]
# print('before adding ele',list1)
# list1.append(200)
# print('after adding ele',list1)
# list1.insert(1,400)
# list1.pop(2)
# list1.remove(56)
# list1.clear()
# print('ele in list',list1)
#------------------------------------------------
# #SORTING OF LIST
# list1=list1.sort()
# print(list1)
#------------------------------------------------
# #REVERSING A LIST
# list1 = [435,274,243,454,65]
# list1.reverse()
# print(list1)
#------------------------------------------------
# #COUNT-FREQUENCY
# list1.count(65)
#------------------------------------------------
# #COPY
# list3=list1.copy()
# print(list3)
#------------------------------------------------

# #SQUARE THE ELEMENTS OF LIST
# lista=[2,4,5,7,8]
# listb=[]
# listc=[]
# #USING RANGE
# for i in range(0,len(lista)):
#     listb.append(lista[i]**2)
# print(listb)
# #WITHOUT USING RANGE
# for i in lista:
#     listc.append(i**2)
#     print(listc)
#-----------------------------------------------
#PRINT ONLY EVEN NUMBERS IN LIST
# l1=[2,4,5,7,8]
# l4=[]
# for i in l1:
#     if i%2==0:
#         l4.append(i)
# print(l4)
#------------------------------------------------
# #ACCEPT RUNTIME AT RUN TIME AND SUM OF ALL ELEMENTS OF LIst
l1=[]
n = int(input('enter noof ele'))
for i in range(n):
    print('elements in list are')
    l1.append(int(input()))
print(sum(l1))