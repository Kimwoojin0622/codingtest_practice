def solution(lines):
    tmp = []
    for data in lines: # O(3)
        f_value, s_value = data[0], data[1]
        # O (N) 최대가 200
        for i in range(f_value, s_value):
            tmp.append(i)
    
    # 중복 제거 set
    set_tmp = set(tmp)
    cnt = 0
    for n in set_tmp:
        if tmp.count(n) >= 2:
            cnt += 1
    
    return cnt