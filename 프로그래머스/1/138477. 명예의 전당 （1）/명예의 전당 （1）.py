def solution(k, score):
    # k - 명예의 전당 목록의 점수 개수
    # score - 1일부터 마지마 날까지 출연한 가수들의 점수
    
    # 문제 : 매일 발표된 명예의 전당의 최하위 점수를 return하는 solution 함수를 완성
    
    # 1. 명예의 전당에 들어갈 값들을 담을 winner 리스트와 각 명예의 전당의 최소값을 담을 result 리스트 선언합니다.
    
    # 2. 명예의 전당 값이 담긴 score를 for문을 돌면서 값들을 가져옵니다.
    
    # 3. 만약, 명예의 전당 값을 담을 winner 리스트에 개수가 k개보다 작다면 winner에 명예의 전당 값을 append를 합니다.
    
    # 4. 명예의 전당의 길이가 k보다 크다면 min 함수를 통해 winner의 최솟값을 구합니다.
    
    # 5. 이후 명예의 전당 값 s가 최솟값보다 클 경우에는 winner에 있는 값들 중에서 pop을 통해 마지막 값을 제거하고, 명예의 전당 값 s를 winner에 append 합니다.
    
    # 6. winner에 숫자들이 정렬이 되어야 pop와 append를 활용해서 원하는 값을 제거하고 삽입할 수 있기 때문에 winner를 내림차순 정렬을 했습니다.
    
    # 7. 이후 각 명예의 전당에서 가장 최소값을 min 함수를 통해 구하고, 이를 result에 삽입하였습니다.
    
    # 8. 최종적으로는 각 명예의 전당의 최솟값을 가진 result를 return 하였습니다.
    
    result = []
    winner = []
    
    for s in score:
        if len(winner) < k:
            winner.append(s)
        else:
            min_value = min(winner)
            if s > min_value:
                winner.pop()
                winner.append(s)
        winner = sorted(winner, reverse=True)
        result.append(min(winner))
    
    return result