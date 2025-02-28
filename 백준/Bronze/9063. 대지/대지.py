n = int( input())
xList = []
yList = []

for _ in range (n):
  x,y = map(int,input().split())
  xList.append(x)
  yList.append(y)

minX = min(xList)
maxX = max(xList)

minY= min(yList)
maxY = max(yList)

result = (maxX - minX) * (maxY-minY)
print(result)