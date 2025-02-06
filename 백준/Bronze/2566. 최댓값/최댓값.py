a =[] 

for i in range(9):
  row = list(map(int, input().split()))
  a.append(row)

max_num = 0   
x,y = 0,0
for i in range(9):
  for j in range(9):
    if a[i][j] >= max_num :
      max_num = a[i][j]
      x = i+1
      y = j+1

print(max_num)
print(x, y)