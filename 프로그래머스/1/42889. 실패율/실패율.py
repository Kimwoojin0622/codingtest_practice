def solution(N, stages):
    # 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어
    # N 최대 500 , stage길이 최대 200,000
    
    tmp = []
    # step 1. 각각의 실패율을 구하자
    # step 2. N을 1부터 N+1까지 i로 돌린다.
    for i in range(1, N + 1):
        # step 3. i의 count를 세고, stages를 for문으로 돌면서 i 보다 크거나 같은 숫자를 센다.
        lose_player_cnt = stages.count(i) # 실패한 유저
        player_cnt = 0
        for num in stages: # 해당 스테이지 플레이한 유저
            if num >= i:
                player_cnt += 1
        
        # step 4. 만약 lose_player가 한 명도 없다면 실패율 0을 append
        if lose_player_cnt == 0:
            tmp.append([i, 0.0])
        # step 5. i의 count / i보다 크거나 같은 숫자 = lose_player_cnt / player_cnt
        # step 6. 실패율을 집어넣는다.
        else:
            tmp.append([i, lose_player_cnt / player_cnt])
            
    # step 7. 정렬
    sort_result = sorted(tmp, key=lambda x:(-x[1], x[0]))
    # step 8. 결과를 result 리스트에 삽입
    result = [data[0] for data in sort_result]
    return result