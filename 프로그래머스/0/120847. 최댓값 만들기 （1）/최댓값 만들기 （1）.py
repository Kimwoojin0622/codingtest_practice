def solution(numbers):
    # N의 최대값이 10,000이므로 O(N^2) 가능
    # 정렬 sort를 써서 O(N log N)쓰면 더 빠를 것 같다.
    numbers_sorted = sorted(numbers)
    result = numbers_sorted[-1] * numbers_sorted[-2]
    
    return result
            