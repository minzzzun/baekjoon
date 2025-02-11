n,b = map(int,input().split())

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = ''

while n!= 0 : 
    s += number[n%b]
    n //= b

print(''.join(reversed(s)))