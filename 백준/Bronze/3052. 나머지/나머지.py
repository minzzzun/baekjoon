a = []
remain = []
for i in range(10):
  a.append(int(input()))

for num in a:
  remain.append(num%42)

print(len(set(remain)))