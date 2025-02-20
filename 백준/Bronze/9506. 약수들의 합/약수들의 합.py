while True:
  
  n = int(input())
  if n == -1:
    break
  a = []
  for i in range (1, n):
    if n % i == 0:
      a.append(i)
  sum = 0 
  for i in a:
    sum += i 
  if sum != n:
      print(f"{n} is NOT perfect.")
  else: 
      print(f"{n} = {' + '.join(map(str,a))}")  