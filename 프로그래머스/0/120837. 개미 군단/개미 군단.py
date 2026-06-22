def solution(hp):
    # 장군개미는 5, 병정개미는 3, 일개미는 1
    cnt = 0
    while hp != 0:
        if hp >= 5:
            cnt = cnt + hp // 5
            hp = hp % 5
        elif hp >= 3:
            cnt = cnt + hp // 3
            hp = hp % 3
        else:
            cnt = cnt + hp // 1
            hp = hp % 1
    
    return cnt
            
    