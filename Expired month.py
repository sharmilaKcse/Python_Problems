n=list(map(int,input().split("-")))
a=int(input())
n[0]=n[0]+a%12
n[1]=n[1]+a//12
if(n[0]>12):
    n[1]+=1
    n[0]-=12
print("%02d-%d"%(n[0],n[1]))
  
