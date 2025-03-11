n = int(input())

result = 0 

for i in range(1,n+1):
  nums= list(map(int,str(i))) # 숫자 문자열로 만든뒤 각 자리 별로 분해 245 -> '245' -> [2,4,5]
  result = sum(nums) + i
  if result == n:
    print(i)
    break
  if i == n :
    print(0)

