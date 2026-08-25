def solution(lottos, win_nums):
    # O(N^2) 가능
    # 알 수 없는 숫자의 갯수
    zero_cnt = lottos.count(0)
    
    # 맞춘 개수 count
    tmp = []
    for lotto in lottos:
        if lotto in win_nums:
            tmp.append(lotto)
    
    # 최고 번호 일치 갯수, 최소 번호 일치 갯수
    correct_max_min = [len(tmp) + zero_cnt, len(tmp)]
    
    for i in range(2):
        if correct_max_min[i] == 6:
            correct_max_min[i] = 1
        elif correct_max_min[i] == 5:
            correct_max_min[i] = 2
        elif correct_max_min[i] == 4:
            correct_max_min[i] = 3
        elif correct_max_min[i] == 3:
            correct_max_min[i] = 4
        elif correct_max_min[i] == 2:
            correct_max_min[i] = 5
        else:
            correct_max_min[i] = 6
    
    return correct_max_min