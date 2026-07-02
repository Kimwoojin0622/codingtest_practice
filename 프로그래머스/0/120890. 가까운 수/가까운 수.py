def solution(array, n):
    sorted_array = sorted(array) # O(N log N)
    
    min_value, tmp = 101, 0
    for num in sorted_array:
        if abs(n - num) < min_value:       
            min_value = abs(n - num)
            tmp = num
    return tmp