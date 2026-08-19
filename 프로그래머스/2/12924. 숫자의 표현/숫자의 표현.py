def solution(n):
    # O(N^2) 가능
    loop = n // 2 + 1
    cnt = 0
    
    for i in range(1, loop + 1):
        check_sum = i
        for j in range(i+1, loop + 1):
            check_sum = check_sum + j
            if check_sum == n:
                cnt += 1
                break
            elif check_sum > n:
                break
    
    return cnt + 1