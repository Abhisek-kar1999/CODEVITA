t=int(input())
a=[]
for j in range(t):
  cnt=0
  N=int(input())
  a=list(map(int,input().split()))
  a.insert(0,0)
  b=list(range(N+1))
  ans=b
  while True:
    c=[0]*(N+1)
    for i in range(1,N+1):
      c[a[i]]=b[i]

    cnt+=1
    if c==ans:
      print(cnt,end='')
      break
    else:
      b=c