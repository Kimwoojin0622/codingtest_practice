def solution(N, stages):
    # 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어
    # N 최대 500 , stage길이 최대 200,000
    
    tmp = []
    for i in range(1, N + 1):
        lose_player_cnt = stages.count(i) # 실패한 유저
        player_cnt = 0
        for num in stages: # 해당 스테이지 플레이한 유저
            if num >= i:
                player_cnt += 1
                
        if lose_player_cnt == 0:
            tmp.append([i, 0.0])
        else:
            tmp.append([i, lose_player_cnt / player_cnt])

    sort_result = sorted(tmp, key=lambda x:(-x[1], x[0]))
    
    result = [data[0] for data in sort_result]
    return result