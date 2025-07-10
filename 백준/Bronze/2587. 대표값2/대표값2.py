a = []
for i in range(5): 
  b = int(input())
  a.append(b)


avg = sum(a) / len(a)
print(int(avg))
a.sort()
print(a[2])