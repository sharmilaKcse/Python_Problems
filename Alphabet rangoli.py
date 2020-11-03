def print_rangoli(size):
    # your code goes here
    char=96+size

    dash=size+(size-2)
    for row in range (size):
        for i in range (dash-(2*row)):
            print("-", end="")
        if size>1:
           for j in range(row+1):            
                print(chr(char-j),end="-")
        else:
            for j in range(row+1):            
                print(chr(char-j),end="")
        
          
        for k in range(row,0,-1):
            if row>0:
                    if k==1:
                       print(chr(char-k+1),end="")
                    else:
                       print(chr(char-k+1),end="-")
            else:
                continue
                
        if row>0:
            
           for i in range (dash-(2*row)):
                 print("-", end="")
        else:
            
           for i in range (dash-(2*row)-1):
                 print("-", end="")
        
        print()
    for row in range (1,size):
        for i in range(2*row):
           print("-", end="")
        for j in range(size,row,-1):
                print(chr(96+j),end="-")
        for k in range(row+2,size+1):
              print(chr(96+k),end="-")
        for i in range(2*row-1):
              print("-", end="")
        print()
size=int(input())
print(print_rangoli(size))

"""def print_rangoli(size):
    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    
    for i in range(size-1, -size, -1):
        x = abs(i)
        if x >= 0:
            line = myStr[size:x:-1]+myStr[x:size]
            print ("--"*x+ '-'.join(line)+"--"*x)"""
