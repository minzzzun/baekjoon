n,m = map(int,input().split())

b = [0]*(n+1)


for x in range(m):
  i,j,k = map(int,input().split())
  for y in range (i, j+1):
    b[y] = k

for i in range(1,n+1):
  print(b[i],end=" ")