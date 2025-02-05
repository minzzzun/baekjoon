n, m = map(int, input().split())

arrA,arrB= [],[]
for i in range (n): 
  arrA.append(list(map(int,input().split())))
    
for i in range (n): 
  arrB.append(list(map(int,input().split())))

for i in range(n):
  for j in range(m):
    result = arrA[i][j] + arrB[i][j]
    print(result,end= " ")
  print()