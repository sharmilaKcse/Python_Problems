def insertion_sort(list1):
 for index in range(1,len(list1)):
    cur_val=list1[index]
    pos=index
    while cur_val<list1[pos-1] and pos>0:
        list1[pos]=list1[pos-1]
        pos=pos-1
    list1[pos]=cur_val

list1=[2,3,1,5,6]
insertion_sort(list1)
print(list1)
