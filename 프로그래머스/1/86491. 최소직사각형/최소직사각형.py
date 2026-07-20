def solution(sizes):
    # 최대 N = 10,000
    max_value, min_value = [], []
    for size in sizes:
        max_value.append(max(size))
        min_value.append(min(size))
    
    return max(max_value) * max(min_value)