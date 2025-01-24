n = int(input())

for i in range(n):
  a,b = map(int,input().split())
  print("Case #",end="")
  print(i+1,end="")
  print(":",end=" ")
  print(a+b)
  