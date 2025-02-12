t = int(input())

for _ in range(t): 
  c = float(input())
  cent = int(c)
  q = cent // 25
  cent %= 25
  d = cent // 10
  cent %= 10 
  n = cent // 5
  cent %= 5
  p = cent // 1 
  print(q, d, n, p)
