def solution(d, budget):
    # 예산
    
    # O(N log N)
    sorted_d = sorted(d)
    
    budget_sum = 0
    cnt = 0
    for num in sorted_d:
        budget_sum += num
        if budget_sum > budget:
            return cnt
        cnt += 1
        
    return cnt