
# n,m = map(int, input().split())

# a = []

# for i in range(n):
#   a.append(int(i+1))

# # print(a)
# for x in range(m):
#   i,j = map(int,input().split())
#   t = a[i-1]
#   a[i-1] = a[j-1]
#   a[j-1] = t 

# for i in a:
#   print(i,end=" ")

n, m = map(int, input().split())

# 바구니 리스트 초기화 (1부터 N까지)
a = list(range(1, n+1))

# M번 동안 역순 정렬 수행
for _ in range(m):
    i, j = map(int, input().split())
    a[i-1:j] = reversed(a[i-1:j])  # 리스트의 부분을 역순으로 변환

# 최종 결과 출력
print(*a)
