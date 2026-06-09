def solution(num_list):
    # 첫 번째 원소가 0이 아닌 1번 원소라고 할 때,,,
    chk = [0, 0]
    for i in range(len(num_list)):
        if i % 2 == 0:
            chk[0] += num_list[i]
        else:
            chk[1] += num_list[i]
    
    return max(chk)