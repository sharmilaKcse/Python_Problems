t=int(input("t"))
for i in range(t):
    n=int(input("n"))#no of element
    k=int(input("k"))#rotation steps
    a=[]
    for j in range(n):
        get=int(input("get"))
        a.append(get)
    x=(a[:-k])#123
    y=(a[-k:])#45
    print(*(y+x))





    
    
        
                
