def solution(k, score):
    # k - 명예의 전당 목록의 점수 개수
    # score - 1일부터 마지마 날까지 출연한 가수들의 점수
    
    # 문제 : 매일 발표된 명예의 전당의 최하위 점수를 return하는 solution 함수를 완성
    
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