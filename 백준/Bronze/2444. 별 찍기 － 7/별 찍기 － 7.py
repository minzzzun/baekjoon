n = int(input())


for i in range (1,n):  
  print(" "*(n-i),end="")
  print("*"*(2*i-1),end= "")
  print("")

for i in range (n, 0, -1):
  print(" "*(n-i),end="")
  print("*"*(2*i-1),end= "")
  print("")
