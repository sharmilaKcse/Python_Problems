"""list1=[10,15,4,23,0]
for j in range(len(list1)-1): #(len(list1)-1,0,-1)
    for i in range(len(list1)-1-j): #j
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
            print(list1)
        else:
            print(list1)
    print()
print(list1)"""

list1=[67,23,4,65,0]
a=len(list1)
for j in range(a-1):
   for i in range(a-1-j):#0 1 2 3 
        if list1[i]>list1[i+1]:
           list1[i],list1[i+1]=list1[i+1],list1[i]
           print(list1)
        else:
           print(list1)
   print()
print(list1)
        
