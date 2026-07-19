def solution(d, budget):
    # d의 길이는 100이하
    # O(N^2)
    
    # d를 작은 순서대로 정렬을 시킨다. O(N log N)
    sort_d = sorted(d)
    
    # 만약 합산이 budget 보다 크다면 return을 하고,
    # 아니면 cnt를 계속 증가한다.
    budget_sum, cnt = 0, 0
    for n in sort_d:
        budget_sum += n
        if budget_sum > budget:
            return cnt
        cnt += 1
    
    return cnt