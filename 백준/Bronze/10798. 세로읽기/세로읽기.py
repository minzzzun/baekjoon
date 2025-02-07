
a = [] 
row_lan = 0
for i in range(5):
  row = list( input())
  a.append(row)
  row_lan = len(row)


for i in range(15):
  for j in range(5):
    if i < len(a[j]):
      print(a[j][i], end="")