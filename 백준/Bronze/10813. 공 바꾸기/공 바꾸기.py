n, m = map(int,input().split())

a_list = [0]*n 

for i in range(0,n):
  a_list[i] = i+1 

t = 0
for x in range(0,m):
  i,j = map(int, input().split())
  t = a_list[i-1]
  a_list[i-1] = a_list[j-1]
  a_list[j-1] =t  

for i in a_list:
  print(i,end=" ")
