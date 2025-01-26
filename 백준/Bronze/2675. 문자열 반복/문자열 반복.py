t = int(input())

for i in range(t):
  a,b = input().split()
  num_a = int(a)
  for i in b:
    print(i*num_a,end="")
  print()