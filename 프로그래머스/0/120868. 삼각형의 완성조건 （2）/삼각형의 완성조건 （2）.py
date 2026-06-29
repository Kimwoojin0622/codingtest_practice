def solution(sides):
    # 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야합니다.
    max_values, min_values, cnt = max(sides), min(sides), 0
    
    # max_values가 가장 긴 변 일때
    tmp = max_values - min_values + 1
    for i in range(tmp, max_values + 1):
        cnt += 1
    
    # 다른 값이 max_values 보다 더 긴 변 일때
    tmp = max_values + min_values
    for i in range(max_values + 1, tmp):
        cnt += 1
    
    return cnt