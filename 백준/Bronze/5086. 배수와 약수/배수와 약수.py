while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    if a % b == 0:  # b는 a의 약수
        print("multiple")
    elif b % a == 0:  # a는 b의 약수
        print("factor")
    else:
        print("neither")