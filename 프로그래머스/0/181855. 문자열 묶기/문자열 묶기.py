def solution(strArr):
    # N 최대치가 100,000이기에 O(N^2)은 시간 문제로 부족
    # 적어도 O(N log n)
    slen = [0 for _ in range(30)] # str의 각 원소의 길이 최대값이 30임
    
    for data in strArr:
        length = len(data) - 1
        slen[length] += 1
    
    # 가장 개수가 많은 그룹의 크기는 그냥 slen의 max값을 구하면 됨
    result = max(slen)
    return result