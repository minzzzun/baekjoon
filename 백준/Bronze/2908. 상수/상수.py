a, b = input().split()

reverse_a = int(''.join(reversed(a)))
reverse_b = int(''.join(reversed(b)))

if reverse_a > reverse_b:
  print(reverse_a)
else: 
  print(reverse_b)