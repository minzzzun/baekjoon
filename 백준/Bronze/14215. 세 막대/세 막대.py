a,b,c = map(int,input().split())

if max((a,b,c)) < sum((a,b,c)) - max((a,b,c)):
  print(sum((a,b,c)))
else:
  print(2*(sum((a,b,c)) - max((a,b,c)))-1)




