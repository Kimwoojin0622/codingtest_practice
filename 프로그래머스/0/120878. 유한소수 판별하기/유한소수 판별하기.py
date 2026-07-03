import math

def solution(a, b):
    tmp = math.gcd(a,b)
    a, b = a // tmp, b // tmp # 최대공약수 사용해서 기약분수 구하기
    
    # 1 제외, 분모의 약수 구하기
    tmp_list = []
    for i in range(2, b + 1):
        if b % i == 0:
            tmp_list.append(i)
    
    cnt = 0
    for data in tmp_list:
        if data % 2 == 0 or data % 5 == 0:
            continue
        else:
            cnt += 1
            if cnt >= 1:
                return 2
    
    return 1
