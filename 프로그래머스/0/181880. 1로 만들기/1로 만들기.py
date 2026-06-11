def solution(num_list):
    cnt = 0
    for num in num_list:
        i = 0
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = (num - 1) // 2
            i += 1
        cnt = cnt + i
    
    return cnt
