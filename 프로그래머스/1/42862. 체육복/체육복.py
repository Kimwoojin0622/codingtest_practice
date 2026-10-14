def solution(n, lost, reserve):
    # 중복 제거
    lost_set = set(lost) - set(reserve) # 여벌 체육복을 가져온 학생이 도난 당했을 수 있음!
    reserve_set = set(reserve) - set(lost)
    
    for r in reserve_set:
        if r - 1 in lost_set:
            lost_set.remove(r-1) # remove를 사용하면 됐음!
        elif r + 1 in lost_set:
            lost_set.remove(r+1)
    
    
    return n - len(lost_set)