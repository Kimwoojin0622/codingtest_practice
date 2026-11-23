def solution(sizes):
    max_values = 0
    min_values = 0
    for size in sizes:
        if max(size) > max_values:
            max_values = max(size)
        if min(size) > min_values:
            min_values = min(size)
    
    return max_values * min_values