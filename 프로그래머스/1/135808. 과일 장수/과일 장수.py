def solution(k, m, score):
    # O(N^2) 불가
    result = 0
    sort_score = sorted(score, reverse = True)
    
    # for문 몇번 돌아야할지
    if len(sort_score) // m == 0:
        return result
    else:
        i = 0
        for _ in range(0, len(sort_score) // m):
            tmp = sort_score[i : i + m]
            i = i + m

            # 최저 사과 점수 -> 내림차순 정렬했으니, [-1]이 가장 작은값 * 사과 개수(m)
            result += tmp[-1] * m
    return result