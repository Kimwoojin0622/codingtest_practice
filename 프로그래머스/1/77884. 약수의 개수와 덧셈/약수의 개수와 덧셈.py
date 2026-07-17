def solution(left, right):
    # O(N^2) 가능
    result = 0
    for i in range(left, right + 1):
        tmp = []
        for j in range(1, i + 1):
            if i % j == 0:
                tmp.append(j)
        # 약수의 개수
        if len(tmp) % 2 == 0:
            result += i
        else:
            result -= i
    
    return result
            