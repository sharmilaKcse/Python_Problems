n=int(input())
arr=list(map(int,input().split()))
for i in range(0,n):
    s=str(arr[i])
    r=int(s[0])
    l=int(s[-1])
    a=0;a1=0;b=0;b1=0;c=i-1;c1=i+1
    while b<r:
      if c==-1:
          c=n-1
      a=a+arr[i]
      c=c-1
      b+=1
    while b1<1:
        if c1==n:
            c1=0
        a1=a1+arr[c1]
        c1+=1
        b1+=1
    print(a+a1,end=" ")

