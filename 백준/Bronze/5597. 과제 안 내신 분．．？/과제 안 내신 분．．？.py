
std_list=[]
for std in range(0,28):
  std_list.append(int(input()))

n=[]
for i in range(1,31):
  if i not in std_list:
    n.append(i)
print(min(n))
print(max(n))

