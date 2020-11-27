l = []
flag = 0
for k in range(int(input("Enter number"))):
               l.append(input())
for i in set(l):
    if l.count(i)%2 != 0:
        flag = 1
        break
if flag == 1:
    print("The balls are not in paired and contains",end=' ')
    for i in l:
          print(i,end=' ')
    print("paired coloured balls in the box.")
else:
    print("The balls are in paired and contains",end=' ')
    for i in l:
        print(i,end=' ')
    print("paired coloured balls in the box.")
